# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 18:21:58 2021

@author: lankuohsing
"""

# 统计字符出现频率，生成映射表
def count_frequency(ori_list):
    chars = []
    ret = []

    for char in ori_list:
        if char in chars:
            continue
        else:
            chars.append(char)
            ret.append((char, ori_list.count(char)))

    return ret


# 节点类
class Node:
    def __init__(self, frequency):
        self.left = None
        self.right = None
        self.father = None
        self.frequency = frequency

    def is_left(self):
        return self.father.left == self


# 创建叶子节点
def create_leaves(frequency_list):
    return [Node(frequency) for frequency in frequency_list]


# 创建Huffman树
def create_huffman_tree(leaves):
    queue = leaves[:]
    queue.sort(key=lambda item: item.frequency,reverse=True)
    while len(queue) > 1:
        node_left = queue.pop(-1)
        node_right = queue.pop(-1)
        node_father = Node(node_left.frequency + node_right.frequency)
        node_father.left = node_left
        node_father.right = node_right
        node_left.father = node_father
        node_right.father = node_father
        len_queue=len(queue)
        if len_queue==0:
            queue.append(node_father)
            break
        if node_father.frequency>queue[0].frequency:
            queue.insert(0,node_father)
            continue
        for i in range(0,len_queue):
            if node_father.frequency<=queue[len_queue-1-i].frequency:
                queue.insert(len_queue-1-i+1,node_father)
                break
    queue[0].father = None
    return queue[0]


# Huffman编码，得到{char:code}字典
def huffman_encoding(leaves, root,char_frequency):
    char_to_code={}
    code_to_char={}
    for char,frequency in char_frequency:
        char_to_code[char]=""
    for i in range(len(leaves)):
        leaf = leaves[i]
        while leaf != root:
            if leaf.is_left():
                char_to_code[char_frequency[i][0]] = '0' + char_to_code[char_frequency[i][0]]
            else:
                char_to_code[char_frequency[i][0]] = '1' + char_to_code[char_frequency[i][0]]
            leaf = leaf.father
    for char, code in char_to_code.items():
        code_to_char[code]=char
    return char_to_code,code_to_char

# 编码整个字符串
def encode_func(ori_list, char_to_code):
    ret = []
    for char in ori_list:
        ret.append(char_to_code[char])

    return ret


# 解码整个字符串
def decode_func(encoded_list, code_to_char):
    ret = []
    for code in encoded_list:
        ret.append(code_to_char[code])

    return ret

# In[]
if __name__ == '__main__':
#    ori_list = input('The ori_list to encode:')
    ori_list=["A","F","T","E","R","D","D","A","T","A","E","A","R","A","R","E","A","R","T","A","R","E","A"]
    char_frequency = count_frequency(ori_list)#[(char,freq)]
    leaves = create_leaves([item[1] for item in char_frequency])
    root = create_huffman_tree(leaves)
    char_to_code,code_to_char = huffman_encoding(leaves, root,char_frequency)
    encoded_list = encode_func(ori_list, char_to_code)

    decoded_list = decode_func(encoded_list, code_to_char)

    print('Encode result:', encoded_list,"length: ",len(encoded_list))
    print('Decode result:' , decoded_list)