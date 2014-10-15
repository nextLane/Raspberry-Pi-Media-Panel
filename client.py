#! /usr/bin/python

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host =socket.gethostname()
port =12345

s.connect((host,port))


#r = input()

r = raw_input('Set theme: ')

s.send(r.encode())

s.close ()

