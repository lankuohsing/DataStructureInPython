# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 22:07:40 2021

@author: lankuohsing
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        fast=head
        slow=head
        meet=None
        is_meet=False
        while slow is not None:
            slow=slow.next
            if slow is None:
                return None
            fast=fast.next
            if fast is None:
                return None
            fast=fast.next
            if fast is None:
                return None
            if fast==slow:
                meet=slow
                is_meet=True
                break
        if is_meet:
            slow=head
            fast=meet
            while slow!=fast:
                slow=slow.next
                fast=fast.next
            return slow
        return None
