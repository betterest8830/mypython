# coding=utf8
# python3 + linux

import asyncio
import time
import threading
import random

async def hello():
    print("Running in the loop...")
    flag = 0
    while flag < 100000:
        with open('testa.txt', 'a') as f:
            f.write('======\n')
        flag += 1
    print("Stop the loop")
def test01():
    coroutine = hello()
    loop = asyncio.get_event_loop()
    task = loop.create_task(coroutine)
    
    print(task)
    try:
        t1 = threading.Thread(target=loop.run_until_complete, args=(task,))
        t1.start()
        time.sleep(1)
        print(task)
        t1.join()
    except KeyboardInterrupt as e:
        task.cancel()
        print(task)
    finally:
        print(task)

async def coro(tag):
    await asyncio.sleep(random.uniform(0.5, 5))
def test02():
    loop = asyncio.get_event_loop()
    tasks = [coro(i) for i in range(1, 11)]
    dones, pendings = loop.run_until_complete(asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED))
    print('first: ', len(dones))    
    dones2, pendings2 = loop.run_until_complete(asyncio.wait(pendings, timeout=1))
    print('first: ', len(dones2))    
    dones3, pendings3 = loop.run_until_complete(asyncio.wait(pendings2))
    print('first: ', len(dones3))    

if __name__ == '__main__':
    #test01()
    test02()
