# -*-   coding:utf-8    -*-
'''
作者（author）：张佳旺（Jiawang Zhang）
日期（date）：2020-09-29
'''

d=2
class A():
    a=d
    def __init__(self):
        self.c=d
    def info(self):
        print('self.c:',self.c)
        print('A.a:',A.a)
def b():
    m=d
    print('d:',d)

if __name__=='__main__':
    # d = 2
    A().info()
    b()