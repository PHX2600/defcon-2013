#!/usr/bin/python

import socket, time, re

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

# Set room number
room = 1

out = s.recv(4096)

while ('hexidecimal' not in out):

    print '***** NOW ENTERING ROOM ' + str(room) + ' *****'

    # Get blue jug value
    s.send('look blue jug\n')
    time.sleep(.1)
    out = s.recv(1024)
    blue = [int(i) for i in out.split() if i.isdigit()]

    blueMax = blue[1]

    print blueMax


    # Get red jug value
    s.send('look red jug\n')
    time.sleep(.1)
    out = s.recv(1024)
    red = [int(i) for i in out.split() if i.isdigit()]

    redMax = red[1]

    print redMax


    # Get target value
    s.send('look inscription\n')
    time.sleep(.1)
    out = s.recv(1024)
    targetArray = [int(i) for i in out.split() if i.isdigit()]

    target = targetArray[0]

    print target


    # Pick up the goddamn jugs
    s.send('get blue jug\n')
    time.sleep(.1)
    s.send('get red jug\n')
    time.sleep(.1)


    # Set small and large values
    if (blueMax < redMax):

        small = 'blue'
        smallCurrent = blue[0]

        large = 'red'
        largeCurrent = red[0]

    elif (redMax < blueMax):

        small = 'red'
        smallCurrent = red[0]

        large = 'blue'
        largeCurrent = blue[0]

    else:

        exit(1)

    print str(smallCurrent) + '/' + str(largeCurrent) + '\t' + str(target)


    while (smallCurrent != target and largeCurrent != target):

        if (smallCurrent == 0):

            # Fill the small jug
            s.send('fill ' + small + ' jug\n')
            time.sleep(.1)
            s.recv(1024)

            # Pour small into large
            s.send('pour ' + small + ' jug into ' + large + ' jug\n')
            time.sleep(.1)
            s.recv(1024)

        else:

            # Dump large jug
            s.send('empty ' + large + ' jug\n')
            time.sleep(.1)
            s.recv(1024)

            # Pour small into large
            s.send('pour ' + small + ' jug into ' + large + ' jug\n')
            time.sleep(.1)
            s.recv(1024)

        # Get small jug current value
        s.send('look ' + small + ' jug\n')
        time.sleep(.1)
        out = s.recv(1024)
        outArray = [int(i) for i in out.split() if i.isdigit()]

        smallCurrent = outArray[0]

        # Get large jug current value
        s.send('look ' + large + ' jug\n')
        time.sleep(.1)
        out = s.recv(1024)
        outArray = [int(i) for i in out.split() if i.isdigit()]
        largeCurrent = outArray[0]

        print str(smallCurrent) + '/' + str(largeCurrent) + '\t' + str(target)

    # Put large jug on scale
    s.send('put ' + large + ' jug onto scale\n')
    time.sleep(.1)
    out = s.recv(1024)

    print out

    # Drop yo shit
    s.send('drop ' + small + ' jug\n')
    s.recv(1024)

    # Find exit and go
    s.send('look\n')
    time.sleep(.1)
    out = s.recv(1024)

    print out

    strPos = out.find('Exits:');

    print strPos

    start = strPos + 8
    end = strPos + 9

    door = out[strPos + 8:strPos + 9]

    print door

    exit(1)

    s.send('n\n')
    time.sleep(.1)
    out = s.recv(1024)

    print out

    room = room + 1

print out

exit(0)
