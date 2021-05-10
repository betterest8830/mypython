# coding=utf8
# python3 + linux

import os, time
from threading import Thread
import threading

def fun1(name='python'):
    for i in range(2):
        print('hello', name)
        time.sleep(0.1)
def test01():
    t1 = Thread(target=fun1)
    t2 = Thread(target=fun1, args=('java',))
    t1.start()
    t2.start()

class MyThread(Thread):
    def __init__(self, name='python'):
        super().__init__()
        self.name = name
    
    def run(self):
        for i in range(2):
            print('hello', self.name)
            time.sleep(0.5)
def test02():
    t1 = MyThread()
    t2 = MyThread(name='c++')
    t1.start()
    t2.start()

def loop():
    print('thread %s is running ...' % threading.current_thread().name)
    n = 0
    while n < 3:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)
def test03():
    print('thread %s is running...' % threading.current_thread().name)
    t1 = Thread(target=loop, name='LoopThread')
    t2 = Thread(target=loop)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('thread %s ended.' % threading.current_thread().name)    

if __name__ == '__main__':
    #test01()
    #test02()
    test03()

