# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 22:17:27 2021

@author: lankuohsing
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        p1=head
        p2=head.next
        while p2 is not None:
            head.next=p2.next
            p2.next=p1
            p1=p2
            p2=head.next

        return p1