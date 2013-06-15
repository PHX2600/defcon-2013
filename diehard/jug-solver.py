#!/usr/bin/python

import socket, time

# Initilize socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('diehard.shallweplayaga.me', 4001))

# Go to jug problem room
s.send('n\n')
time.sleep(.1)
s.send('n\n')
time.sleep(.1)
s.send('n\n')
time.sleep(.1)
s.send('n\n')
time.sleep(.1)
s.send('n\n')
time.sleep(.1)
s.send('n\n')
time.sleep(.1)
s.send('e\n')
time.sleep(.1)
s.send('n\n')
time.sleep(.1)
s.send('w\n')
time.sleep(.1)
s.send('n\n')
time.sleep(.1)
s.send('n\n')
time.sleep(.1)

print s.recv(4096)

# Get red jug value
s.send('look red jug\n')
red = s.recv(1024)

# Get blue jug value
s.send('look blue jug\n')
blue = s.recv(1024)
