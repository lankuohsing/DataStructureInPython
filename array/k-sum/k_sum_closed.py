# -*- coding: utf-8 -*-
"""
Created on Sat Jan 29 19:35:25 2022

@author: lankuohsing
"""

class Solution:
    def recursive(self,start_index,current_cycle,target):
        if current_cycle==self.total_cycle-1:
            for second_index in range(start_index+1,self.n):
                if second_index==start_index+1 or self.nums[second_index]!=self.nums[second_index-1]:
                    third_index=self.last_index#注意不能放到前面了，必须放在这里，因为没有剪枝操作，需要完成second_index的循环。每轮迭代需要将third_index重置
                    target2=target-self.nums[second_index]
                    while third_index>second_index:
                        cur_dev=target2-self.nums[third_index]
                        if abs(cur_dev)<self.deviation:
                            self.deviation=abs(cur_dev)
                            self.result=self.target-cur_dev
                        third_index-=1
            return
        else:
            for first_index in range(start_index+1,self.n):
                if first_index==start_index+1 or self.nums[first_index]!=self.nums[first_index-1]:
                    target1=target-self.nums[first_index]
                    self.recursive(first_index,current_cycle+1,target1)
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        self.deviation=99999999
        self.target=target
        nums.sort()
        self.nums=nums
        print(nums)
        self.n=len(nums)
        self.last_index=self.n-1
        self.result=0
        self.total_cycle=3-1
        start_index=-1
        current_cycle=0
        self.recursive(start_index,current_cycle,self.target)
        return self.result