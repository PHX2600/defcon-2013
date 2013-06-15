#!/usr/bin/python

import socket

# Initilize socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('diehard.shallweplayaga.me', 4001))

# Go to jug problem room
s.send('n\n')
s.send('n\n')
s.send('n\n')
s.send('n\n')
s.send('n\n')
s.send('n\n')
s.send('e\n')
s.send('n\n')
s.send('w\n')
s.send('n\n')
s.send('n\n')

print s.recv(4096)
