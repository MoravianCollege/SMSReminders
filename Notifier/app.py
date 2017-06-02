from twilio.rest import Client
from redis import Redis
import time

r = Redis(host='redis', port='6379')

secrets = []
f_in = open('twilio_secrets.txt', 'rt')
for line in f_in:
    secret = line.strip()
    secrets.append(secret)
f_in.close()

account_sid = secrets[0]
auth_token = secrets[1]
sending_number = secrets[2]
client = Client(account_sid, auth_token)


def run_process():
    while True:
        send_notifications()
        time.sleep(10)


def send_notifications():
    for msg_and_num, send_time in r.zscan_iter('reminders'):
        if send_time > int(time.time()):
            return
        else:
            temp = msg_and_num.decode('UTF-8').split(",")
            message = temp[0]
            receive_number = '+1' + temp[1]
            client.messages.create(to=receive_number, from_=sending_number, body=message)
            r.zrem('reminders', msg_and_num)

run_process()
