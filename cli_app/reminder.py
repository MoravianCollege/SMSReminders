#!/usr/bin/python3

import sys
import requests

if (len(sys.argv) == 1):
    r = requests.get('http://localhost:5000')
    print(r.text)
elif (len(sys.argv) == 3):
    data = {'time':sys.argv[1], 'message':sys.argv[2]}
    requests.post('http://localhost:5000', data=data)
else:
    print('Incorret number of arguments, must be date:time and message')
