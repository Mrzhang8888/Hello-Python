from socket import *

HOST = '127.0.0.1'
PORT = 9000
BUFSIZ = 1024
ADDR = (HOST, PORT)

tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
    print('请按照格式输入：GET filename or POST filename xxxxxx')
    msg = input('请输入：')
    tcpCliSock.send(msg.encode())
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode())
tcpCliSock.close()
