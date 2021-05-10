# coding=utf8
# python3 + linux

import threading, time
from threading import Thread, Event
from queue import Queue

class MyThread(Thread):
    def __init__(self, name, event):
        super().__init__()
        self.name = name
        self.event = event
    def run(self):
        print('Thread: {} start at {}'.format(self.name, time.ctime(time.time())))
        self.event.wait()
        print('Thread: {} finish at {}'.format(self.name, time.ctime(time.time())))
def test01():
    threads = []
    event = Event()
    [threads.append(MyThread(str(i), event)) for i in range(1, 5)]
    event.clear()
    [t.start() for t in threads]
    print('等待5s...')
    time.sleep(5)
    print('唤醒所有线程...')    
    event.set()

class Student(Thread):
    def __init__(self, name, que):
        super().__init__()
        self.name = name
        self.que = que
    def run(self):
        while True:
            msg = self.que.get()
            if msg == self.name:
                print('{}: 到！'.format(self.name))
class Teacher:
    def __init__(self, que):
        self.que = que           
    def call(self, std_name):
        print("老师：{}来了没？".format(std_name))
        self.que.put(std_name)
def test02():
    que = Queue()
    teacher = Teacher(que)
    s1 = Student('AAA', que)
    s2 = Student('BBB', que)
    s1.start()
    s2.start()
    print('开始点名~')
    teacher.call('AAA')
    time.sleep(1)
    teacher.call('BBB')
    

if __name__ == '__main__':
    #test01()
    test02()
    
