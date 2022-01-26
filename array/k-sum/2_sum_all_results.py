# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 21:19:33 2021

@author: lankuohsing
"""

class Solution1:
    def twoSum(self, nums, target: int):
        results=[]
        num_index={}
        set_second_ele=set()
        for i in range(0,len(nums)):
            num_index[nums[i]]=i
        for i in range(0,len(nums)):
            temp=target-nums[i]
            if temp in num_index.keys() and i!=num_index[temp] and not temp in set_second_ele:
                results.append([nums[i],temp])
                set_second_ele.add(nums[i])
        return results
class Solution2:
    def twoSum(self, nums, target: int):
        results=[]
        num_index={}
        set_second_ele=set()
        for i in range(0,len(nums)):
            num_index[nums[i]]=i
        for i in range(0,len(nums)):
            temp=target-nums[i]
            if temp in num_index.keys() and i!=num_index[temp] and not nums[i] in set_second_ele and not temp in set_second_ele:
                results.append([nums[i],temp])
                set_second_ele.add(nums[i])
        return results

if __name__=="__main__":
    nums1=[1,2,3,4,5,6,7,8,9,10]
    target=11
    solution1=Solution1()
    results1=solution1.twoSum(nums1,target)
    print(results1)
    nums=[1,1,3,4,5,6,7,8,10,10]
    target=11
    solution2=Solution2()
    results2=solution2.twoSum(nums,target)
    print(results2)