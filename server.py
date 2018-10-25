import os
from socket import *
import time
import threading
HOST = ''  # 对bind（）方法的标识，表示可以使用任何可用的地址
PORT = 9000  # 设置端口
BUFSIZ = 1024  # 设置缓存区的大小
ADDR = (HOST, PORT)
tcpSerSock = socket(AF_INET, SOCK_STREAM)   # 定义了一个套接字
tcpSerSock.bind(ADDR)  # 绑定地址
tcpSerSock.listen(5)     # 规定传入连接请求的最大数，异步的时候适用


def tcplink(tcpCliSock, addr):
        while True:
            data = tcpCliSock.recv(BUFSIZ)
            data = data.decode()
            print(data)
            if not data:
                break
            elif data[0] == 'G':
                filename = data.split(' ')[1]
                fp = 'C:/homepage/' + filename  # 文件完整路径
                if os.path.exists(fp):
                    with open(fp, 'r') as f:
                        content = f.read()
                    reply = '200\n' + content
                else:
                    reply = '404\nfile not found'
                tcpCliSock.send(reply.encode())

            elif data[0] == 'P':
                datalist = data.split(' ') # 切片处理
                filename = datalist[1]
                filecontent = datalist[2]
                fp = "C:/homepage/" + filename
                f = open(fp, 'a+')
                f.write(filecontent)
                f.close()
                filesize = os.path.getsize(fp)
                print(filesize)
                reply = '200\n' + str(filesize)
                tcpCliSock.send(reply.encode())
            else:
                msg = 'error'
                tcpCliSock.send(msg.encode())
        tcpCliSock.close()


while True:
    tcpCliSock, addr = tcpSerSock.accept()  # 等待接受连接
    tcplink(tcpCliSock, addr)
tcpSerSock.close()

