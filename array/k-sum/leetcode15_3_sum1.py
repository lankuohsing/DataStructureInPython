# -*- coding: utf-8 -*-
"""
Created on Wed Jan 26 22:30:33 2022

@author: lankuohsing
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results=[]
        nums.sort()
        third_index_start=len(nums)-1
        for first_index in range(0,len(nums)):
            if first_index==0 or nums[first_index]!=nums[first_index-1]:
                target1=-nums[first_index]
                third_index=third_index_start
                for second_index in range(first_index+1,len(nums)):
                    if second_index==first_index+1 or nums[second_index]!=nums[second_index-1]:
                        target2=target1-nums[second_index]
                        if target2>nums[third_index_start]:
                            continue
                        while third_index>second_index and target2<nums[third_index]:
                            third_index-=1
                        if third_index==second_index:
                            break
                        if target2==nums[third_index]:
                            results.append([nums[first_index],nums[second_index],nums[third_index]])
        return results