# coding=utf8
# linux + python3

import multiprocessing
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('Run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*5)
    diff = time.time() - start
    print('Task %s run %0.2f seconds' % (name, diff))
    return diff
def test01():
    print('parent pid=%s' % os.getpid())
    p = Pool(4)
    results = []
    for i in range(5):
        #p.apply_async(long_time_task, args=(i,)) # 非阻塞
        #p.apply(long_time_task, args=(i,)) # 阻塞
        results.append(p.apply_async(long_time_task, args=(i,))) # 关注结果
    time.sleep(0.1)
    print('waiting for all subprocesses done ...')
    p.close()
    p.join()
    for res in results:
        print(':::=', res.get())
    print('all sub done.')   

def create_logger(i):
    print(i**2)
class CreateLogger:
    def __init__(self, func):
        self.func = func
def test02():
    ll = range(8)
    c1 = CreateLogger(create_logger)
    pool = Pool(multiprocessing.cpu_count())
    pool.map(c1.func, ll)


if __name__ == '__main__':
    #test01()
    test02()

