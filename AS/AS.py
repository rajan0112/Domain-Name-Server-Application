from socket import *
import json

port= 53533
ok_stat = str(201)
fail_stat="400: Incorrect message format"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('', port))
ip_maps={}

while True:
    initial_message, address = s.recvfrom(2048)
    decoded_message = initial_message.decode()
    main_message = json.loads(decoded_message)

    if len(main_message) == 4:
        ip_maps = {main_message["NAME"]: main_message}
        reg_file = open("register.json", "w")
        json.dump(ip_maps, reg_file)
        reg_file.close()
        s.sendto(ok_stat.encode(), address)
    elif len(main_message) == 2:
        with open("register.json", "r") as reg_file:
            mdict = json.load(reg_file)
        response_dns = mdict[main_message["NAME"]]
        obj_dns = json.dumps(response_dns)
        s.sendto(obj_dns.encode(),address)
    else:
        s.sendto(fail_stat.encode(),address)
