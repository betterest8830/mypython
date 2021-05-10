# coding=utf8
# python3 + linux

from multiprocessing import Process, Lock, RLock, Value
import time

# 进程1和进程2在相互抢着使用共享内存v
def job1(v, num):
    for _ in range(5):
        time.sleep(0.5)
        v.value += num
        #print(v.value, end=',')
        print(v.value)
def test01():
    v = Value('i', 0)
    p1 = Process(target=job1, args=(v, 1))
    p2 = Process(target=job1, args=(v, 100))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

#lock = Lock()
lock = RLock()
def job2(v, num, lock):
    lock.acquire()
    for _ in range(5):
        time.sleep(0.5)
        v.value += num
        print(v.value)
    lock.release()
def test02():
    v = Value('i', 0)
    p1 = Process(target=job2, args=(v, 1, lock))
    p2 = Process(target=job2, args=(v, 100, lock))
    p1.start()
    p2.start()
    p1.join()
    p2.join()


if __name__ == '__main__':
    #test01()
    test02()

