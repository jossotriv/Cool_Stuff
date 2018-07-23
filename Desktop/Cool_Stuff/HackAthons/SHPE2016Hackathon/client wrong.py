#!/usr/bin/python           # This is client.py file

import socket               # Import socket module

s = socket.socket()         # Create a socket object
host = socket.gethostname() # Get local machine name
port = 8080# Reserve a port for your service.
message = str(3)
c, addr = s.accept()
s.connect((host, port))
s.sendto(message.encode(),(host, port))

s.close                     # Close the socket when done
