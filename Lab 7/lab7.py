import socket
import select

port = 60003

listOfSockets = []

def chatServer():
    sockL = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockL.bind(('', port))
    sockL.listen(1)

    print("Chat server started on port " + str(port))

    listOfSockets.append(sockL)

    print(" Listening... on port {}".format(port), "\n\n\n")

    while True:
        tup = select.select(listOfSockets, [], [])
        sock = tup[0][0]
        if sock == sockL:
            (sockClient, addr) = sockL.accept()
            listOfSockets.append(sockClient)
            print('[{}: {}]'.format(sockClient.getpeername()[0], sockClient.getpeername()[1]), "(Connected)")
            message = (' [{}: {}]'.format(sockClient.getpeername()[0], sockClient.getpeername()[1]) + "(Connected)").encode('ASCII')
            broadcastConnection(sockL, sockClient, message)
        
        else:
            data = sock.recv(2048)
            if data:
                print(' [ {}: {}]'.format(sock.getpeername()[0], sock.getpeername()[1], data.decode()))

                broadcast(sockL, sock, " [{}: {}] {}".format(sock.getpeername()[0], sock.getpeername()[1], data.decode()).encode('ASCII'))

            else:
                print(' [{}: {}]'.format(sock.getpeername()[0],sock.getpeername()[1]), "(Disconnected)")
                message = (' [{}: {}]'.format(sock.getpeername()[0], sock.getpeername()[1])+ "(Disconnected)").encode('ASCII')
                broadcastConnection(sockL, sock, message)
                sock.close()
                listOfSockets.pop(listOfSockets.index(sock))
    sockL.close()

def broadcast(sockS, sockC, message):

    for i in range(len(listOfSockets)):
        if listOfSockets[i] != sockS:
            try:
                listOfSockets[i].send(message)
            except:
                print(' Socket-{}. [{}: {}]'.format(i, listOfSockets[i].getpeername()[0], listOfSockets[i].getpeername()[1]), "Not Connected")
                listOfSockets[i].close()
                listOfSockets.pop(listOfSockets.index(sockC))


def broadcastConnection(sockS, sockC, message):

    for i in range(len(listOfSockets)):
        if listOfSockets[i] != sockS and listOfSockets[i] != sockC:
            try:
                listOfSockets[i].send(message)
            except:
                print(' Socket.{}. [{}: {}]'.format(i, listOfSockets[i].getpeername()[0], listOfSockets[i].getpeername()[1]), "Not Connected")
                listOfSockets[i].close()

chatServer()