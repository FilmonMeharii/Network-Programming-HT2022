import socket 

def initiateServer():
    sock = socket.socket()
    sock.bind(('localhost', 80) )
    sock.listen(1)
    print("\n Server listening...\n")

    while True:
        (sockClient, addr) = sock.accept()
        sockClient.sendall(bytearray('<html><h1> Your browser sent the followingrequest: </h1>\n', "ASCII"))
        sockClient.sendall(bytearray("HTTP/1.1 200 ok\n", "ASCII"))
        sockClient.sendall(bytearray("\n","ASCII"))
        sockClient.sendall(bytearray("<pre>\n", "ASCII"))
        clientReq = sockClient.recv(1024).decode('ASCII')
        req = clientReq.split('\n')
        if(len(req) > 0):
            for i in range(len(req)):
                print(req[i])
                sockClient.sendall((req[i]).encode('ASCII'))
        sockClient.sendall(bytearray("</pre> </html> \n", "ASCII"))
        sockClient.close()
        sock.close()

initiateServer()