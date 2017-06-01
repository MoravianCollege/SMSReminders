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

account_sid = str(secrets[0])
print(account_sid)
auth_token = str(secrets[1])
print(auth_token)
sending_number = secrets[2]
client = Client(account_sid, auth_token)

def run_process():
    while True:
        send_notifications()
        time.sleep(10)

# currently you will have to input the phone number
# you wish to send to within this method
def send_notifications():
    for message, send_time in r.zscan_iter('reminders'):
        if send_time > int(time.time()):
            return
        else:
            client.messages.create(to='', from_=sending_number, body=message)
            r.zrem('reminders', message)

run_process()
