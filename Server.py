import socket
import os
from _thread import *

ServerSocket = socket.socket()
host = '127.0.0.1'
port = 1233
ThreadCount = 0
ips_ports = []
name_password_dic = {"HadeelGhalieah": "99", "Razan": "80", "Amir": "70",
                     "Akram": "60", "Wafaa": "00000"}


try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(5)


def threaded_client(connection):

    if ThreadCount == 5:
        MESSAGE = "Python server : Congratulation you are the 5th client and those are the  clients" + str(
            ips_ports)
        connection.send(MESSAGE.encode())
    else:
        connection.send(str.encode('Welcome to the Server'))

    while True:

        data = connection.recv(4096)
        if data.decode('utf-8') == 'exit':
            break
        else:
            resp = name_password_dic[data.decode('utf-8')]
            reply = resp
        if not data:
            break
        connection.sendall(str.encode(reply))
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    ips_ports.append((address[0], address[1]))
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
    
ServerSocket.close()



