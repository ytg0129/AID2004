"""
lock 锁示例
"""
from threading import Thread,Lock

lock = Lock() # 线程锁

# 共享资源
a = b = 0

def value():
    while True:
        lock.acquire() # 上锁
        if a != b:
            print("a = %d,b = %d"%(a,b))
        lock.release() # 解锁

t = Thread(target=value)
t.start()

while True:
    with lock:  # 上锁
        a += 1
        b += 1
                # 解锁

t.join()