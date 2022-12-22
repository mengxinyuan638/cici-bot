import random

ratio = {10:'a',30:'b',60:'c',100:'d'}
def choujiang1():
    #生成一个1-100的随机整数
    x = random.randint(1,100)
    #生成一个1-100的数组
    mother = [x for x in range(1,101,1)]
    #判断x在数组的什么位置
    x_position = mother.index(x)
    pre_number = 0
    for key in ratio.keys():
        if x_position - pre_number>=0 and x_position-int(key)<0:
            return ratio[key]
        if pre_number == 0:
            pre_number=int(key)
    return -1


