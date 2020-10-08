# -*-   coding:utf-8    -*-
'''
作者（author）：张佳旺（Jiawang Zhang）
日期（date）：2020-10-08
'''
def fanshu(number):
    sum=0
    for i in number:
        sum+=i*i
    return(sum)
print(fanshu([1,2,3]))
print(fanshu((1,2,3)))

# def fanshu(*number):
#     sum=0
#     for i in number:
#         sum+=i*i
#     return(sum)
#
# a=(1,2,3)
# print(fanshu(*a))