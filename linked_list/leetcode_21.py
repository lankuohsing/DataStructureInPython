# -*- coding: utf-8 -*-
"""
Created on Thu Jul  1 21:24:30 2021

@author: lankuohsing
"""
"""
将两个升序链表合并为一个新的 升序 链表并返回。
新链表是通过拼接给定的两个链表的所有节点组成的.
输入：l1 = [1,2,4], l2 = [1,3,4]
输出：[1,1,2,3,4,4]
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        start=None
        if l2.val <= l1.val:
            cur=l2
            l2=l2.next
        else:
            cur=l1
            l1=l1.next
        start=cur
        while l1 is not None and l2 is not None:
            if l2.val <= l1.val:
                cur.next=l2
                l2=l2.next
            else:
                cur.next=l1
                l1=l1.next
            cur=cur.next
        if l1 is not None:
            cur.next=l1
        else:
            cur.next=l2
        return start

if __name__ == '__main__':
    node1=ListNode(val=1)
    node2=ListNode(val=2)
    node3=ListNode(val=4)
    node4=ListNode(val=1)
    node5=ListNode(val=3)
    node6=ListNode(val=4)
    node1.next=node2
    node2.next=node3
    node4.next=node5
    node5.next=node6
    solution=Solution()
    node=solution.mergeTwoLists(node1,node5)
    while node is not None:
        print(node.val)
        node=node.next