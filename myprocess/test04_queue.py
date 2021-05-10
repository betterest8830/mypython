# encoding=utf8
# python3 + linux

from multiprocessing import Process, Queue, Pipe
import os, time, random

def write(q, urls):
    print('Process(%s) is writing...' % os.getpid())
    for url in urls:
        q.put(url)
        time.sleep(random.random())
def read(q):
    print('Process(%s) is reading...' % os.getpid())
    while True:
        url = q.get(True)
        print('Get %s from queue.' % url)
def test01():
    q = Queue()
    urls1 = ['url_1', 'url_2', 'url_3']
    urls2 = ['url_4', 'url_5', 'url_6']
    w1 = Process(target=write, args=(q, urls1))
    w2 = Process(target=write, args=(q, urls2))
    r = Process(target=read, args=(q,))
    w1.start()
    w2.start()
    r.start()
    w1.join()
    w2.join()
    r.terminate()

def talk(pipe):
    pipe.send(dict(name='Bob', spam=42))
    reply = pipe.recv()
    print('talker got:', reply)
def test02():
    parent, child = Pipe()
    c = Process(target=talk, args=(child,))
    c.start()
    print('parent got:', parent.recv())
    parent.send({x*2 for x in 'spam'})
    c.join()
    print('parent exit')

if __name__ == '__main__':
    #test01()
    test02()
    
