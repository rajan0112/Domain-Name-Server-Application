from flask import Flask, request, abort
from flask_api import status
import socket
import requests
import json

app = Flask(__name__)
@app.route('/fibonacci', methods = ['GET'])

ok_stat= status.HTTP_200_OK
fail_stat= 'bad format', status.HTTP_400_BAD_REQUEST

def US():
    host = request.args.get('hostname')
    as_ip_address = request.args.get('as_ip')
    port = request.args.get('fs_port')
    as_port = request.args.get('as_port')
    as_port = int(as_port)
    num = request.args.get('number')

    if host == '' :
        return 
    elif as_ip_address == '':
        return fail_stat
    elif port == '':
        return fail_stat
    elif as_port == '':
        return fail_stat
    elif num == '':
        return fail_stat
    elif num.isnumeric == False:
        return fail_stat
    
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    idict = {'hostname': host, 'type': "A"}
    s.sendto(json.dumps(idict).encode(), (as_ip_address, as_port))
    reply, address = s.recvfrom(2048)
    temp_response = reply.decode()
    final_response = json.loads(temp_response)
    path_ip = final_response["ip"]
    final_path = 'http://' + path_ip + ':' + port + '/fibonacci?' + 'number=' + num
    result = requests.get(final_path)
    output = result.text
    return output, ok_stat

app.run(host='0.0.0.0', port=9090, debug=True)