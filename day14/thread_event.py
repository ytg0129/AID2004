"""
event 线程同步互斥方法示例
"""

from threading import Thread,Event

s = None # 线程通信变量
e = Event() # event对象

# 线程函数
def 杨子荣():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    e.set() # 解除主线程阻塞


t = Thread(target=杨子荣)
t.start()

# 主线程做验证
print("数对口令就是自己人")
e.wait() # 阻塞等待验证通知
if s == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神，你是对的人")
else:
    print("打死他.... 无情啊....")

t.join()
