# Network Programming
# https://www.py4e.com/lessons/network

#!/usr/bin/env python3

import socket

 

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

mysock.send(cmd)

 

while True:

    data = mysock.recv(512)

    if len(data) < 1:

        break

    print(data.decode())

 

mysock.close()

1. You will see a blank black screen after you enter telnet commands.

2. Type         GET http://data.pr4e.org/intro-short.txt HTTP/1.0 

3. You will not see what you are typing but if you write it correctly it will work.

4. Hit enter after you type GET http://data.pr4e.org/intro-short.txt HTTP/1.0 

5. type socket1.py