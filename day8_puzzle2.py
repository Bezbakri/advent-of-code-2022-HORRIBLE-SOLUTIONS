# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 19:39:57 2022

@author: bezbakri
"""

with open("input8") as f:
    tree_matrix = [list(map(int, x.strip())) for x in f]
    rows, columns = len(tree_matrix), len(tree_matrix[0])
    visibility = 0
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                continue
            curTree = tree_matrix[i][j]
            
            treesU = 0
            treesD = 0
            treesL = 0
            treesR = 0
            
            for n in range(i - 1, -1, -1):
                treesU += 1
                if tree_matrix[n][j] >= curTree:
                    break
                    
                       
                
            for n in range(i + 1, rows):
                treesD += 1
                if tree_matrix[n][j] >= curTree:
                    break
                    
            
            for n in range(j - 1, -1, -1):
                treesL += 1
                if tree_matrix[i][n] >= curTree:
                    break
                    
            
            for n in range(j + 1, columns):
                treesR += 1
                if tree_matrix[i][n] >= curTree:
                    break
                    
                    
            curVisibility = treesU * treesD * treesL * treesR
            
            
            visibility = curVisibility if curVisibility > visibility else visibility
            
    print(visibility)