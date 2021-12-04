# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 18:18:41 2021

@author: lankuohsing
"""

class Solution:
    island_num=0
    def dfs(self,grid,visited,directions,i,j):
        # 边界条件
        if i>=len(grid) or j>=len(grid[0]) or i<0 or j<0:
            return
        # 访问过的结点，跳过
        if visited[i][j]==1:
            return
        # 为0 的结点跳过，这里记不记录被访问其实无所谓
        if grid[i][j]=="0":
            #visited[i][j]=1
            return
        else:
            # 是否将该节点作为新发现的岛屿线索
            is_island=1
            for k, direction in enumerate(directions):#看看它是否是已经属于某个岛屿
            #边界条件
                if i+direction[0]>=len(grid) or j+direction[1]>=len(grid[0]) or i+direction[0]<0 or j+direction[1]<0:
                    continue
                #如果它的上下左右是岛屿的一部分，且已经被访问过，则它不能算新发现的岛屿
                if grid[i+direction[0]][j+direction[1]]=="1":
                    if visited[i+direction[0]][j+direction[1]]==1:
                        is_island=0
                        break
                    else:
                        # 剪枝，如果当前结点是新发现的岛屿，则将其上下左右的非水区域标记为访问过
                        visited[i+direction[0]][j+direction[1]]==1
            self.island_num+=is_island
            visited[i][j]=1
            for k, direction in enumerate(directions):
                self.dfs(grid,visited,directions,i+directions[k][0],j+directions[k][1])
    def numIslands(self, grid: List[List[str]]) -> int:
        visited=[[0 for e in grid[0]] for e in grid]
        directions=[(-1,0),(1,0),(0,-1),(0,1)]# 上，下，左，右
        for i in range(0,len(grid)):
            for j in range(0,len(grid[i])):
                self.dfs(grid,visited,directions,i,j)
        return self.island_num
