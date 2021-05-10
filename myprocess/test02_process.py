# coding=utf8

# python3 + linux
import os, time
from multiprocessing import Process


def action(name, *add):
    time.sleep(0.5+name)
    print(name)
    for arc in add:
        print('%s---pid=%s' % (arc, os.getpid()))
def test01():
    my_tuple = ("http://c.biancheng.net/python/",\
                "http://c.biancheng.net/shell/",\
                "http://c.biancheng.net/java/")
    process_l = []
    for i in range(2):
        p = Process(target=action, args=(i, *my_tuple))
        p.start()
        process_l.append(p)
    for i in range(2):
        process_l[i].join()
    print('main end')
#test01(), wins下,Process 来创建并启动进程时，程序必须先判断 if __name__=='__main__':,但是linux下不用

class MyProcess(Process):
    def __init__(self, name, *add):
        super().__init__()
        self.name = str(name)
        self.add = add
    def run(self):
        time.sleep(0.5+int(self.name))
        print(self.name)
        for arc in self.add:
            print('%s***pid=%s' % (arc, os.getpid()))
def test02():
    my_tuple = ("http://c.biancheng.net/python/",\
                "http://c.biancheng.net/shell/",\
                "http://c.biancheng.net/java/")
    process_l = []
    for i in range(2):
        p = MyProcess(i, *my_tuple)
        p.start()
        process_l.append(p)
    for i in range(2):
        process_l[i].join()
    print('main end')
def test03():
    my_tuple = ("http://c.biancheng.net/python/",\
                "http://c.biancheng.net/java/")
    process_l = []
    for i in range(2):
        p = MyProcess(i, *my_tuple)
        # 如果子进程的任务在主进程任务结束后就没有存在的必要了，那么该子进程应该在开启前就被设置成守护进程。
        p.daemon = True
        p.start()
        process_l.append(p)
        print('daemon:', p.daemon)
    '''
    for i in range(2):
        process_l[i].join()
    '''    
    print('main end')
        
    
if __name__ == '__main__':
    #test01()
    #test02()
    test03()
    
