# coding=utf8
# python3 + linux

import threading

local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))
def process_thread(name):
    local_school.student = name
    process_student()
def test01():
    t1 = threading.Thread(target=process_thread, args=('Alice',), name='TA')
    t2 = threading.Thread(target=process_thread, args=('Bob',), name='TB')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    pass


if __name__ == '__main__':
    test01()
