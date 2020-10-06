# -*-   coding:utf-8    -*-
'''
作者（author）：张佳旺（Jiawang Zhang）
日期（date）：2020-10-06
'''
# a=[0]*8
# print(a)
a=[0]*10
print(id(a))
a[0]=1
print(id(a))
a=[1+a[i-1] for i in range(1,10)]
print(id(a))
print(a)