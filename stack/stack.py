# -*- coding: utf-8 -*-
"""
Created on Sat May  1 14:47:23 2021

@author: lankuohsing
"""
"""
python中的栈是用list来实现的。
NoneType append(obj): 入栈，以列表尾部为栈顶
obj pop([index=-1]): 移除列表汇总的某一个元素（默认最后一个元素），并且返回该元素的值
"""
# In[]
stack=[]
for i in range(0,10):
    stack.append(i)
for i in range(0,len(stack)):
    print(stack.pop())