# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 19:54:40 2022

@author: lankuohsing
"""
# In[]
graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['A','D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}

def find_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not start in graph.keys():
            return None
        for node in graph[start]:
            if node not in path:#防止出现无限递归的情况
                newpath = find_path(graph, node, end, path)
                if newpath: return newpath
        return None

path=find_path(graph,'A','D') # ['A', 'B', 'C', 'D']
# In[]
def find_all_paths(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if not start in graph.keys():
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                newpaths = find_all_paths(graph, node, end, path)
                paths=paths+newpaths#等价于下面的两行
#                for newpath in newpaths:
#                    paths.append(newpath)
        return paths
paths=find_all_paths(graph,'A','D')

# In[]
def find_shortest_path(graph, start, end, path=[]):
        path = path + [start]
        if start == end:
            return path
        if not start in graph.keys():
            return None
        shortest = None
        for node in graph[start]:
            if node not in path:
                newpath = find_shortest_path(graph, node, end, path)
                if newpath:
                    if not shortest or len(newpath) < len(shortest):
                        shortest = newpath
        return shortest
shortest_path=find_shortest_path(graph, 'A', 'D')