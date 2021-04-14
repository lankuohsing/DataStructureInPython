# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 22:39:02 2021

@author: lankuohsing
"""
# 统计字符出现频率，生成映射表
def count_frequency(text):
    chars = []
    ret = []

    for char in text:
        if char in chars:
            continue
        else:
            chars.append(char)
            ret.append((char, text.count(char)))

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
def huffman_encoding(leaves, root):
    char_to_code={}
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

    return char_to_code


# 编码整个字符串
def encode_str(text, char_to_code):
    ret = ''
    for char in text:
        ret +=char_to_code[char]

    return ret


# 解码整个字符串
def decode_str(huffman_str, char_to_code):
    ret = ''
    while huffman_str != '':
        i = 0
        for char,code in char_to_code.items():
            if code in huffman_str and huffman_str.index(code) == 0:
                ret += char
                huffman_str = huffman_str[len(code):]
            i += 1

    return ret

# In[]
if __name__ == '__main__':
#    text = input('The text to encode:')
    text="AFTERDDATAEARAREARTAREA"
    char_frequency = count_frequency(text)#[(char,freq)]
    leaves = create_leaves([item[1] for item in char_frequency])
    root = create_huffman_tree(leaves)
    char_to_code = huffman_encoding(leaves, root)
    huffman_str = encode_str(text, char_to_code)
    origin_str = decode_str(huffman_str, char_to_code)

    print('Encode result:' + huffman_str,"length: ",len(huffman_str))
    print('Decode result:' + origin_str)