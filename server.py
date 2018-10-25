from socket import *

host = ''  # 服务器地址
port = 12345  # 服务器端口
bufsiz = 2048  # 缓存大小
adds = (host, port)  # 地址+端口

udpsersock = socket(AF_INET, SOCK_DGRAM)  # 创建UDP的套接字类型。
udpsersock.bind(adds)  # 绑定到地址和端口

while True:

    data, addc = udpsersock.recvfrom(bufsiz)
    if not data: break
    print('客户端回答：', data.decode('utf-8'))
    msg = input('服务器说：')  # 输入数据
    udpsersock.sendto(msg.encode('utf-8'), addc)

udpsersock.close()
