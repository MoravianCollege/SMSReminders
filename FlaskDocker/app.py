from flask import Flask, request
import time
from redis import Redis

app = Flask(__name__)
r = Redis(host='redis', port='6379')

@app.route('/', methods=['GET', 'POST'])
def save_notification():
    if request.method == 'POST':
        receive_notification()
    else:
        ret_str = ''
        for reminder, time_to_send in r.zscan_iter('reminders'):
            ret_str += reminder.decode('UTF-8')
            ret_str += ' ' + str(int(time_to_send) - int(time.time())) + '\n'
        return ret_str

def receive_notification():
    time_to_send = request.form['time']
    message = request.form['message']
    curr_time = int(time.time())
    exp_time = int(time_to_send) + curr_time
    r.zadd('reminders', message, exp_time)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
