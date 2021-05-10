# coding=utf8
import os
import time
import signal
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

def task(i):
    print 'work %d' % i
def test03():
    var = 10
    pid = os.fork()
    if pid == 0:
        var = 9
        print 'i am child(%s), var=%s' % (os.getpid(), var)
    else:
        time.sleep(100)
        print 'i am father, var=', var

def chldhandler(signum, stackframe):
    while 1:
        try:
            result = os.waitpid(-1, os.WNOHANG)
        except:
            break
        print 'Reaped child process %d' % result[0]
    signal.signal(signal.SIGCHLD, chldhandler)
def test04():
    signal.signal(signal.SIGCHLD, chldhandler)
    print 'Before the fork my pid =',os.getpid()
    pid = os.fork()
    if pid:
        print 'from the parent the child pid =',pid
        print 'parent sleep 100s'
        time.sleep(100)
        print 'sleep done'
    else:
        print 'child sleep 5s'
        time.sleep(5)


if __name__ == '__main__':
    #test01()
    #test02()
    #test03()
    test04()

