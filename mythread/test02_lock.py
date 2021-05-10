# coding=utf8
# python3 + linux

import time
from threading import Thread, Lock
import threading

balance = 0
lock = Lock()
def change_it(n):
    global balance
    balance += n
    balance -= n
def loop(num):
    for i in range(1000000):
        change_it(num)
def loop_lock(num):
    for i in range(1000000):
        lock.acquire()
        try:
            change_it(num)
        finally:
            lock.release()
def test01():
    #t1 = Thread(target=loop, args=(3,))
    #t2 = Thread(target=loop, args=(5,))
    t1 = Thread(target=loop_lock, args=(3,))
    t2 = Thread(target=loop_lock, args=(5,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('res=', balance)

def rlock():
    n = 0
    lock = threading.RLock()
    with lock:
        for i in range(10):
            n += 1
            with lock:
                print(n)
def test02():
    t1 = threading.Thread(target=rlock)
    t1.start()


if __name__ == '__main__':
    #test01()
    test02()    
