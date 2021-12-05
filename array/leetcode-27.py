# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 20:43:19 2021

@author: lankuohsing
"""

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j=0
        for i in range(0,len(nums)):
            if nums[i]!=val:
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
                j+=1
        return j