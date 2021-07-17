# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 22:25:59 2021

@author: lankuohsing
"""

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base=769
        self.data=[[]]*self.base
    def hash(self,key:int,base:int):
        return key%base

    def add(self, key: int) -> None:
        index=self.hash(key,self.base)
        for e in self.data[index]:
            if e==key:
                return
        self.data[index].append(key)
        return



    def remove(self, key: int) -> None:
        index=self.hash(key,self.base)
        for i in range(0,len(self.data[index])):
            if self.data[index][i]==key:
                self.data[index].pop(i)
                return

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        index=self.hash(key,self.base)
        for i in range(0,len(self.data[index])):
            if self.data[index][i]==key:
                return True
        return False



# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)