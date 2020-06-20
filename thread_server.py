"""
重点代码！
多线程并发模型
步骤 ： 原理基本同多进程并非
"""

from socket import *
from threading import Thread
import sys

# 全局变量
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST,PORT)

# 处理客户端请求
def handle(connfd):
    while True:
        data = connfd.recv(1024).decode()
        if not data:
            break
        print("客户端:",data)
        connfd.send(b"OK")
    connfd.close()

def main():
    # tcp套接字
    s = socket()
    s.bind(ADDR)
    s.listen(3)

    print("Listen the port %d..." % PORT)

    # 循环接收客户端的连接请求
    while True:
        try:
            c,addr = s.accept()
            print("Connect from ",addr)
        except KeyboardInterrupt :
            s.close()
            sys.exit("服务端退出") # 进程退出

        # 创建线程处理客户端连接
        t = Thread(target=handle,args=(c,))
        t.start()

if __name__ == '__main__':
    main()

