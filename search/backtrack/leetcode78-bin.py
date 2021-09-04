# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 23:45:09 2021

@author: lankuohsing
"""

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        for i in range(0,1<<len(nums)):# 2^n个子集，并且用二进制表示
            temp=[]
            for j in range(0,len(nums)):# 遍历每个元素
                if i&(1<<j):# 该元素是否在这个子集里面出现
                    temp.append(nums[j])
            result.append(temp)
        return result
