import socket

ClientSocket = socket.socket()
host = '127.0.0.1'
port = 1233

print('Waiting for connection')
try:
    ClientSocket.connect((host, port))
except socket.error as e:
    print(str(e))

Response = ClientSocket.recv(1024)
print(Response.decode('utf-8'))
while True:
    Input = input('Type in the student\'s name:  ')
    if Input == 'exit':
        break
    ClientSocket.send(str.encode(Input))
    Response = ClientSocket.recv(1024)
    print(Input + " has scored " + Response.decode('utf-8'))

ClientSocket.close()


