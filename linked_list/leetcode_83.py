# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 21:24:58 2021

@author: lankuohsing
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        cur=head
        while cur.next is not None:
            if cur.val==cur.next.val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return head