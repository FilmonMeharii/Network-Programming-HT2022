import socket 

clientPoint = 0
serverPoint = 0
PORT = 60003

def serversideGetplaySocket():
    serverIP = "127.0.0.1"
    sockServer = socket.socket()
    sockServer.bind((serverIP, PORT))

    sockServer.listen(2)
    print("\n Server listening ...\n")

    (sockClient, addr) = sockServer.accept()
    print('connection from {}'.format(addr))

    while True:
        clientData = sockClient.recv(1024).decode('ASCII')
        if not clientData:
            break
        serverMove = input(' ({}, {})'.format(serverPoint, clientPoint) + ' You Move: ')
        while serverMove not in {'R', 'S', 'P'}:
            serverMove = input(' Wrong entry! Please enter R, S or P. Your move again:')
        print('Oppenents turn:', clientData)
        winRSP(clientData, serverMove)
        print('({},{})'.format(serverPoint, clientPoint) + 'It is oppenents turn now.')
        sockClient.sendall(bytearray(serverMove, 'ASCII'))

    if clientPoint > serverPoint:
        print('You lost with {} against {}'.format(serverPoint,clientPoint))
    else:
        print('You won with {} against {}'.format(serverPoint,clientPoint))
    sockClient.close()
    input("Press enter to exit")

def clientGetplaySocket(host):
    maxPoints = 3
    sockClient = socket.socket()
    sockClient.connect((host, PORT))

    while clientPoint < maxPoints and serverPoint < maxPoints:
        clientMove = input(' ({},{})'.format(clientPoint,serverPoint) + " Your move: ")
        while clientMove not in {'R', 'S', 'P'}:
            clientMove = input("Wrong entry! Please choose from (P,S or R). Your move again: ")
        sockClient.sendall(bytearray(clientMove, 'ASCII'))

        serverMove = sockClient.recv(1024).decode('ASCII')
        winRSP(clientMove, serverMove)
        print(' (Oppenents move:' + serverMove + ')')
    if clientPoint > serverPoint:
        print (' You won with {} against {}'.format(clientPoint, serverPoint))
    else:
        print (' You lost with {} against {}'.format(clientPoint, serverPoint))
    sockClient.close()
    input("Press enter to exit")

def winRSP(clientMove, serverMove):
    global clientPoint, serverPoint
    play = (clientMove, serverMove)
    if play[0]==play[1]:
        pass
    elif(play==('R', 'S')) or (play==('P','R')) or(play==('S', 'P')):
        clientPoint +=1
    else:
        serverPoint +=1

def theProgram():
    ans = "?"
    while ans not in {"C", "S"}:
        ans = input("Do you want to be server (S) or client (C):")
    if ans =="S":
        serversideGetplaySocket()
    else:
        host = input("Enter the server's name or IP: ")
        clientGetplaySocket(host)
theProgram()

 