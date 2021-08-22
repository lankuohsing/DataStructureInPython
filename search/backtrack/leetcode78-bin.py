# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 23:45:09 2021

@author: lankuohsing
"""

n=3
for i in range(0,1<<n):# 2^n个子集，并且用二进制表示
    for j in range(0,n):# 遍历每个元素
        if i&(1<<j):# 该元素是否在这个子集里面出现
            print(j,end="")
    print("\n")