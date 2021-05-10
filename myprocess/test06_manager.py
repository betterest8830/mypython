# coding=utf8
# python3 + linux

from multiprocessing import Process, Array, Manager

# 进程各自持有一份数据，默认无法共享数据
lst = []
def fun1(i):
    lst.append(i)
    print('say hi', lst)
def test01():
    for i in range(5):
        p = Process(target=fun1, args=(i,))
        p.start()

def fun2(a):
    for i in range(len(a)):
        a[i] = -a[i]
def test02():
    arr = Array('i', range(4))
    p = Process(target=fun2, args=(arr,))
    p.start()
    p.join()
    print(arr[:])

def fun3(d, l):
    d[1] = '1'
    d[2] = '2'
    l.reverse()
def test03():
    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(3))
        p = Process(target=fun3, args=(d, l))
        p.start()
        p.join()
        print(d)
        print(l)

if __name__ == '__main__':
    #test01()
    #test02()
    test03()
