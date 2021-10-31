# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 18:57:47 2021

@author: lankuohsing
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        matrix=[[i+j for j in range(len(word2)+1)] for i in range(len(word1)+1)]

        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    matrix[i][j]=matrix[i-1][j-1]
                else:
                    matrix[i][j]=matrix[i-1][j-1]+1
                matrix[i][j]=matrix[i-1][j]+1 if matrix[i-1][j]+1<matrix[i][j] else matrix[i][j]
                matrix[i][j]=matrix[i][j-1]+1 if matrix[i][j-1]+1<matrix[i][j] else matrix[i][j]
        # print(matrix)
        return matrix[-1][-1]