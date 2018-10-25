from socket import *

host = '127.0.0.1'  #本地服务器地址
port = 12345  #客户端端口(确保和服务器的端口一致
bufsiz = 2048 #缓存大小
addc = (host, port) #地址+端口

udpclisock = socket(AF_INET, SOCK_DGRAM)  #创建UDP的套接字类型。

while True:
    msg = input('客户端说：')    #输入数据
    udpclisock.sendto(msg.encode('utf-8'), addc)
    data, adds = udpclisock.recvfrom(bufsiz)
    print('服务器回答：', data.decode('utf-8'))



    
udpclisock.close()
