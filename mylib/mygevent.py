# coding=utf8

from greenlet import greenlet
import gevent
from gevent import select
import time

def fun1(x, y):
    z = g2.switch(x+y)
    print(z)
def fun2(u):
    print(u)
    g1.switch(42)
g1 = greenlet(fun1)    
g2 = greenlet(fun2)
def test01():
    g1.switch('hi', 'lina')

start = time.time()
tic = lambda: 'at %1.1f seconds' % (time.time()-start)
def gr1(num):
    print('start poll... %s\t%s' % (num, tic()))    
    select.select([], [], [], num)
    print('start end... %s\t%s' % (num, tic()))    
def gr3():
    print("Hey lets do some stuff while the greenlets poll, %s" % tic())
    gevent.sleep(1)
def test02():
    gevent.joinall([
        gevent.spawn(gr1, 2), 
        gevent.spawn(gr1, 3),
        gevent.spawn(gr3)    
    ])

from gevent.queue import Queue, Empty
import random
from gevent import monkey
monkey.patch_all()
tasks = Queue(maxsize=3)
def worker(name):
    try:
        while True:
            #gevent.sleep(random.random())
            time.sleep(random.random())
            task = tasks.get(timeout=1)
            print('worker %s get task %s' % (name, task))
            gevent.sleep(0)
    except Empty:
        print('Quit')
def boss():
    for i in range(1, 10):
        tasks.put(i)
    print('Assigned all work in iteration 1')
    for i in range(10, 20):
        tasks.put(i)
    print('Assigned all work in iteration 2')
def test03():
    gevent.joinall([
        gevent.spawn(boss),
        gevent.spawn(worker, 'A'),
        gevent.spawn(worker, 'B'),
        gevent.spawn(worker, 'C'),
    ])


if __name__ == '__main__':
    #test01()
    #test02()
    test03()

