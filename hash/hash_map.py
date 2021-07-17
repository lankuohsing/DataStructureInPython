# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 22:27:52 2021

@author: lankuohsing
"""

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.base=769
        self.data=[[]]*self.base
    def hash(self,key:int,base:int):
        return key%base


    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index=self.hash(key,self.base)
        for i in range(0,len(self.data[index])):
            if self.data[index][i][0]==key:
                self.data[index][i]=(key,value)
                return
        self.data[index].append((key,value))


    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index=self.hash(key,self.base)
        for i in range(0,len(self.data[index])):
            if self.data[index][i][0]==key:
                return self.data[index][i][1]
        return -1


    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index=self.hash(key,self.base)
        for i in range(0,len(self.data[index])):
            if self.data[index][i][0]==key:
                self.data[index].pop(i)
                return



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)