"""
线程属性示例
"""
from threading import Thread
from time import sleep

def fun():
    sleep(3)
    print("线程属性测试")

t = Thread(target = fun)

t.setName("Tarena")
print("Name:",t.getName()) # 获取线程名称

# 主线程退出分支线程也退出
t.setDaemon(True)

t.start()

print("is alive:",t.is_alive())

