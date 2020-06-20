"""
练习1 ： 模拟售票系统
模拟会场的出票系统，现有入场票 500张 记为 T1--T500
由于涉及座位排布 票必须按照顺序卖出
有10个窗口同时买票 （w1--w10），每个窗口买一张票需要0.1秒 sleep(0.1)
按照上面的描述 使用10个线程模拟10个窗口，完成售票过程

思路 ： 先将500张票生成放入到一个列表中，卖出的票打印一下即刻

       w1 ---- T128
"""

from threading import Thread
from time import sleep

ticket = ["T%d" % x for x in range(1, 501)]

# 模拟每个窗口的买票过程
def sell(w):
    while ticket:
        print("%s 窗口卖出：%s"%(w,ticket.pop(0)))
        sleep(0.1)

jobs = []
for i in range(1,11):
    t = Thread(target=sell,args=("w%d"%i,))
    jobs.append(t)
    t.start()

[i.join() for i in jobs]










