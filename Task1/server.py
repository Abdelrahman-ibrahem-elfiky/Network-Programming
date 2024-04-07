
from socket import *

s = socket(AF_INET, SOCK_STREAM)
print("Socket is created")
host = '127.0.0.1'
port = 40674

s.bind((host, port))
print("Socket binded to ", port)
s.listen(5)
print("Socket is listening")

c, addr = s.accept()
print('Get connection from', addr)
c.send(b'Welcome')
c.close()

