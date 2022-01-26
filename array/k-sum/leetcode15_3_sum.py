# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 23:00:45 2021

@author: lankuohsing
"""

class Solution:
    def threeSum(self, nums):
        results=[]
        num_index={}
        for i in range(0,len(nums)):
            num_index[nums[i]]=set()
        for i in range(0,len(nums)):
            num_index[nums[i]].add(i)
        for index_a, a in enumerate(nums):
#            print("index_a,a: ",index_a,a)
            if index_a>0 and a==nums[index_a-1]:
                continue
            for index_b in range(index_a+1,len(nums)):
                b=nums[index_b]
#                print("index_b,b: ",index_b,b)
                if index_b==index_a:
                    continue
                temp=0-a-b
#                print("temp: ",temp)
                if temp in num_index.keys():
                    if index_a in num_index[temp] and index_b in num_index[temp] and len(num_index[temp])==2:
#                        print("11111")
                        continue
                    if (index_a in num_index[temp] or index_b in num_index[temp]) and len(num_index[temp])<=1:
#                        print("22222")
                        continue
                    flag=False
                    for index_c in num_index[temp]:
                        if index_c>index_b:
#                            print("33333")
                            flag=True
                            break
                    if not flag:
                        continue
#                    print("44444")
                    result=[a,b,temp]
                    results.append(result)
        return results
if __name__=="__main__":
    nums = [-1,0,1,2,-1,-4]
    nums.sort()
    solution=Solution()
    results=solution.threeSum(nums)
    print(results)