# coding=utf8
import os
import time
#python2 + linux
# Only works on Unix/Linux/Mac:

def test01():
    # print once
    print 'Process (%s) start ...' % os.getpid()
    pid = os.fork()
    # print twice
    print 'Before fork process pid=%s, ppid=%s' % (os.getpid(), os.getppid())
    if pid == 0:
        print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
        time.sleep(3)
    else:
        time.sleep(1)
        print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)
        time.sleep(3)
    # print twice
    print 'After fork process pid=%s, ppid=%s' % (os.getpid(), os.getppid())


def child(i):
    print '%s: Hello from child=%s, parent=%s' % (i, os.getpid(), os.getppid())
def test02():
    for i in range(3):
        pid = os.fork()
        if pid == 0:
            child(i)
            #break  #2
        else:
            # 如果父进程结束了子进程没有结束，那么子进程就会寄托给pid为1的进程来管理。
            time.sleep(0.1)
            # think the difference under three situations
            break  #3
            print 'Hello from parent ', os.getpid(), pid  #1
            pass

if __name__ == '__main__':
    #test01()
    test02()

