#!/usr/bin/python

import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("pieceofeight2.shallweplayaga.me", 8273))