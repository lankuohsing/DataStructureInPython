# -*- coding: utf-8 -*-
"""
Created on Fri Apr 30 23:11:27 2021

@author: lankuohsing
"""

class BinTreeNode:
    def __init__(self, data, left=None, right=None):
        self.data=data
        self.left=left
        self.right=right
        return
class BinTree:
    def __init__(self):
        self.root=None
        return

"""
递归方式前序遍历
"""
def pre_order_recursive(node: BinTreeNode):
    if node is None:
        return
    print(node.data)
    temp=node.left
    pre_order_recursive(temp)
    temp=node.right
    pre_order_recursive(temp)
    return
"""
非递归方式前序遍历
"""
def pre_order_no_recursive(node: BinTreeNode):
    nodes_stack=[]
    while True:
        if node is None:
            if len(nodes_stack)==0:
                break
            else:
                node=nodes_stack.pop().right
        else:
            print(node.data)
            nodes_stack.append(node)
            node=node.left


# In[]
"""
              node1
             /     \
        node2       node3
       /     \     /     \
   node4   node5 node6   node7
"""
if __name__ == '__main__':
    node4=BinTreeNode(data=4,left=None,right=None)
    node5=BinTreeNode(data=5,left=None,right=None)
    node6=BinTreeNode(data=6,left=None,right=None)
    node7=BinTreeNode(data=7,left=None,right=None)
    node2=BinTreeNode(data=2,left=node4,right=node5)
    node3=BinTreeNode(data=3,left=node6,right=node7)
    node1=BinTreeNode(data=1,left=node2,right=node3)
    print("递归方式前序遍历：")
    pre_order_recursive(node1)
    print("非递归方式前序遍历：")
    pre_order_no_recursive(node1)



