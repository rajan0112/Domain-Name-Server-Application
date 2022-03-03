from flask import Flask, request
from socket import *
import requests
import json

ok_stat = 201
fail_stat="Error"

app = Flask(__name__)

@app.route('/fibonacci', methods = ['GET'])

def cal_fib(input_num):
    number = int(input_num)
    if number >= 3:
        return cal_fib(number-1) + cal_fib(number-2)
    else:
        return 1

def fib_server():
    initial_num = request.args['number']
    num = int(initial_num)
    num_fib = cal_fib(num)
    final_output = str(num_fib)
    return final_out

@app.route('/register', methods = ['PUT'])

def register():
    details = request.get_json()
    ip_address = details.get('ip')
    as_ip_address = details.get('as_ip')
    host_name = details.get('hostname')
    as_port = details.get('as_port')
    as_port = int(as_port)
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    info_dict = {"TYPE": "A", "NAME": host_name, "VALUE": ip_address, "TTL": 10}
    obj_fs = json.dumps(info_dict)
    s.sendto(obj_fs.encode(), (as_ip_address, as_port))
    response, address = s.recvfrom(2048)
    return_code = response.decode('utf-8')
    if return_code != '201':
        return fail_stat
    else:
        return ok_stat

app.run(host='0.0.0.0', port=9090, debug=True)