# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 19:35:07 2022

@author: lankuohsing
"""

class Solution:
    def recursive(self,start_index,current_cycle,target):
        if current_cycle==self.total_cycle-1:
            third_index=self.last_index#放到这里可减少一些操作
            for second_index in range(start_index+1,self.n):
                if second_index==start_index+1 or self.nums[second_index]!=self.nums[second_index-1]:
                    self.temp_result[current_cycle]=self.nums[second_index]
                    target2=target-self.nums[second_index]
                    if target2>self.nums[self.last_index]:
                        continue#剪枝
                    while third_index>second_index and target2<self.nums[third_index]:
                        third_index-=1
                    if third_index==second_index:
                        break#剪枝
                    if target2==self.nums[third_index]:                        self.temp_result[self.total_cycle]=self.nums[third_index]
                        self.results.append([ele for ele in self.temp_result])
            return
        else:
            for first_index in range(start_index+1,self.n):
                if first_index==start_index+1 or self.nums[first_index]!=self.nums[first_index-1]:
                    self.temp_result[current_cycle]=self.nums[first_index]
                    target1=target-self.nums[first_index]                    self.recursive(first_index,current_cycle+1,target1)

    def kSum(self, nums: List[int], target: int, k: int) -> List[List[int]]:
        nums.sort()
        self.nums=nums
        self.n=len(nums)
        self.last_index=self.n-1
        self.results=[]
        self.total_cycle=k-1
        self.temp_result=[0]*(self.total_cycle+1)
        start_index=-1
        current_cycle=0
        #print(self.nums)
        self.recursive(start_index,current_cycle,target)
        return self.results