"""
GIL下线程效率测试
"""
"""
编写一个函数求100000以内质数之合 --》 统计函数执行时间（装饰器）
"""

import time
from threading import Thread

# 求一个函数运行时间
def timeis(f):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = f(*args,**kwargs)
        end_time = time.time()
        print("函数执行时间:",end_time - start_time)
        return res
    return wrapper

# 判断一个数是不是质数
def isPrime(n):
    if n <= 1:
        return  False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

# @timeis
# def no_process():
#     prime = []
#     for i in range(1,100001):
#         if isPrime(i):
#             prime.append(i)
#     print(sum(prime))
#
# no_process() # 函数执行时间: 26.272788524627686

# 自定义进程类
class Prime(Thread):
    def __init__(self,begin,end):
        super().__init__()
        self.begin = begin
        self.end = end

    # 求从beign 到 end之间的质数之和
    def run(self):
        prime = []
        for i in range(self.begin,self.end):
            if isPrime(i):
                prime.append(i)
        print(sum(prime))
#
# @timeis
# def thread_4():
#     jobs = []
#     for i in range(1,100001,25000):
#         t = Prime(i,i+25000) # 使用自定义的进程类创建进程
#         jobs.append(t)
#         t.start()
#     for i in jobs:
#         i.join()

# 函数执行时间: 14.806529998779297
# thread_4()  #函数执行时间: 26.336495637893677


@timeis
def thread_10():
    jobs = []
    for i in range(1,100001,10000):
        t = Prime(i,i+10000) # 使用自定义的进程类创建进程
        jobs.append(t)
        t.start()
    for i in jobs:
        i.join()

# 函数执行时间: 26.10117244720459
thread_10() # 函数执行时间: 14.109814643859863





