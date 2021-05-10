# coding=utf8
# python3 + linux

import time
import threading
from concurrent.futures import ThreadPoolExecutor
from queue import Queue

def target1():
    for i in range(5):
        print('running thread-{}:{}'.format(threading.get_ident(), i))
        time.sleep(1)
def test01():
    pool = ThreadPoolExecutor(3)
    for i in range(4):
        pool.submit(target1)

def target(q):
    while True:
        msg = q.get()
        for i in range(5):
            print('running thread-{}:{}'.format(threading.get_ident(), i))
            time.sleep(1)
def pool(workers,queue):
    for n in range(workers):
        t = threading.Thread(target=target, args=(queue,))
        t.daemon = True
        t.start()
def test02():
    queue = Queue()
    pool(3, queue)
    for i in range(4):
        queue.put("start")
    queue.join()    

if __name__ == '__main__':
    test01()
    #test02()
