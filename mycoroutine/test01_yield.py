# coding=utf8
# python3 + linux

def jump_range(n):
    idx = 0
    while idx < n:
        jump = yield idx
        if jump is None:
            jump = 1
        idx += jump
def test01():
    gen = jump_range(10)
    print(next(gen))
    print(gen.send(2))
    print(next(gen))
    print(gen.send(-1))
def average_gen():
    total, count, average = 0, 0, 0
    while True:
        new_num = yield average
        if new_num is None:
            break    
        count += 1
        total += new_num
        average = total / count
    return total, count, average
def proxy_gen():
    while True:
        total, count, average = yield from average_gen()
        print("计算完毕！！\n总共传入 {} 个数值， 总和：{}，平均数：{}".format(count, total, average))
def test02():
    calc_average = proxy_gen()
    print(next(calc_average))
    print(calc_average.send(10))
    print(calc_average.send(20))
    print(calc_average.send(30))
    print(calc_average.send(None))

if __name__ == '__main__':
    #test01()
    test02()
    

