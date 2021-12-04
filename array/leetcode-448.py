# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 23:09:35 2021

@author: lankuohsing
"""

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i in range(0,len(nums)):
            if nums[nums[i]-1]<=0:
                continue
            nums[nums[i]-1]-=len(nums)
        results=[]
        for i in range(0,len(nums)):
            if nums[i]>0:
                results.append(i+1)
        return results
