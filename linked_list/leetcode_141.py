# -*- coding: utf-8 -*-
"""
Created on Sat Jul 24 00:05:48 2021

@author: lankuohsing
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast=head
        while fast is not None:
            head=head.next
            if head is None:
                return False
            fast=fast.next
            if fast is None:
                return False
            fast=fast.next
            if fast==head:
                return True
        return False
