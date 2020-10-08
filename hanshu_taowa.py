# -*-   coding:utf-8    -*-
'''
作者（author）：张佳旺（Jiawang Zhang）
日期（date）：2020-10-08
'''
def fact(n):
    if n==1 or n==0:
        return(1)
    return(n*fact(n-1))

print(fact(5))