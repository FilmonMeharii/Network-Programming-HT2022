"""
import socket

def initiateServer():
    sock =socket.socket()
    sock.bind(('localhost', 80))
    sock.listen(1)
    """

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 8080

s.bind(("", port))

s.listen(8)

while(True):
    c, a =s.accept()
    print("Recieved message from " + str(a))
    c.send(b"Hello in server")
    c.close()