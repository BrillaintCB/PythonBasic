import socket

s = socket.socket()
host = "192.168.200.205"
port = 5555

s.connect((host,port))
print(s.recv(1024)) #s.recv() This method receives TCP message


s.close()