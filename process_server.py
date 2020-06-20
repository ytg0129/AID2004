"""
重点代码！！
多进程tcp并发模型

步骤：
创建网络套接字用于接收客户端请求
等待客户端连接
客户端连接，则创建新的进程具体处理客户端请求
主进程继续等待其他客户端连接
如果客户端退出，则销毁对应的进程
"""

from socket import *
from multiprocessing import Process
from signal import *
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

    print("Listen the port %d..."%PORT)
    # 处理僵尸进程
    signal(SIGCHLD,SIG_IGN)

    # 循环连接客户端
    while True:
        try:
            c,addr = s.accept()
            print("Connect from",addr)
        except KeyboardInterrupt as e:
            s.close()
            sys.exit("服务端退出！！")

        # 创建子进程处理客户端具体请求事务
        p = Process(target = handle,args=(c,))
        p.daemon = True  # 如果父进程退出，所有服务立即终止则可以加
        p.start()

if __name__ == '__main__':
    main()








