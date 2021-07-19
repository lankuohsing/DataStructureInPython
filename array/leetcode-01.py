# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 22:47:32 2021

@author: lankuohsing
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index={}
        for i in range(0,len(nums)):
            num_index[nums[i]]=i
        for i in range(0,len(nums)):
            temp=target-nums[i]
            if temp in num_index.keys() and i!=num_index[temp]:
                return [i,num_index[temp]]