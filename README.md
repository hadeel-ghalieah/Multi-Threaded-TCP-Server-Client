# Multi-Threaded-TCP-Server-Client
using python socket module i made multi-thread tcp server/clients that makes a new thread whenever a new client is accepted
the 5 ^th accepted client wins a gift, the server congratulates the client and send him a list of previously accepted clients(IP,Port)
the client read "student name " from user input to send it to the server
the server recieves the message and returns " student mark" from its stored object " Dictionary or jason file or database" to the client
the client receives server reply and prints (student, student mark)
the client repeats sending and receiving until user input == 'exit'
when server receives exit msg from client it closes that current client socket and continue serving other connected clients
