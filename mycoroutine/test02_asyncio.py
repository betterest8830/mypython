# coding=utf8
# python3 + linux

import asyncio
from collections.abc import Coroutine, Generator
import time

async def hello(name):
    print('hello,', name)
def test01():
    coroutine = hello('world')
    print(isinstance(coroutine, Coroutine))
def test02():
    coroutine = hello('world')
    loop = asyncio.get_event_loop()
    task = loop.create_task(coroutine)
    loop.run_until_complete(task)

async def _sleep(x):
    time.sleep(2)
    return '暂停了{}秒！'.format(x)
def test03():
    coroutine = _sleep(2)
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(coroutine)
    loop.run_until_complete(task)
    print('返回结果：{}'.format(task.result())) 
def callback(future):
    print('这里是回调函数，获取返回结果是：', future.result())
def test04():
    coroutine = _sleep(2)
    loop = asyncio.get_event_loop()
    task = asyncio.ensure_future(coroutine)
    task.add_done_callback(callback)
    loop.run_until_complete(task)

async def do_some_work(x):
    print('waiting:', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)
def test05():
    cro1 = do_some_work(1)
    cro2 = do_some_work(2)
    cro3 = do_some_work(4)
    tasks = [asyncio.ensure_future(cro) for cro in (cro1, cro2, cro3)]
    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))
    for task in tasks:
         print('Task ret: ', task.result())

if  __name__ == '__main__':
    #test01()
    #test02()
    #test03()
    #test04()
    test05()
