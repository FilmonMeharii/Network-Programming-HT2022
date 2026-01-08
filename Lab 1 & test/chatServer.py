import socket

T_PORT = 80
TCP_IP = '127.0.0.1'

BUF_SIZE = 30
# create a socket object name 'k'
f = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
f.bind((TCP_IP, T_PORT))
f.listen(1)
con, addr = f.accept()
print ('Connection Address is: ' , addr)

while True :
    data = con.recv(BUF_SIZE)
    if not data:
        break
print ("Received data", data)
con.send(data)
con.close()