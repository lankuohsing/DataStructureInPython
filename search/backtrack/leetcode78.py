# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 15:11:53 2021

@author: lankuohsing
"""
import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        decisions=[True,False]
        def backtrack(index: int, nums: List[int], one_result:[],results:[[]])->None:
            if index==len(nums):
                results.append(copy.deepcopy(one_result))
                return
            else:
                for choice in decisions:
                    if choice:
                        one_result.append(nums[index])
                    backtrack(index+1,nums,one_result,results)
                    if choice:
                        one_result.remove(nums[index])
        one_result=[]
        results=[]
        backtrack(0,nums,one_result,results)
        return results

if __name__=="__main__":
    nums=[1,2,3]
    solution=Solution()
    print(solution.subsets(nums))