from socket import *

s = socket(AF_INET, SOCK_STREAM)
print("Socket is created")
host = '127.0.0.1'
port = 40674
s.connect((host, port))

while True:
    data_received = s.recv(1024)
    print("Received data:", data_received.decode())
    if not data_received:
        break

s.close()