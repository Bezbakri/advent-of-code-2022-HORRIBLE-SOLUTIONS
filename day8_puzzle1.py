# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 18:55:00 2022

@author: bezbakri
"""

with open("input8") as f:
    tree_matrix = [list(map(int, x.strip())) for x in f]
    visible_trees = set()
    rows, columns = len(tree_matrix), len(tree_matrix[0])
    for i in range(rows):
        for j in range(columns):
            curTree = tree_matrix[i][j]
            if i == 0 or i == rows - 1 or j == 0 or j == columns - 1:
                visible_trees.add((i, j))
                continue

            checkL = True
            checkR = True
            checkU = True
            checkD = True
            for n in range(i - 1, -1, -1):
                if tree_matrix[n][j] >= curTree:
                    checkU = False
                    break
                       
                
            for n in range(i + 1, rows):
                if tree_matrix[n][j] >= curTree:
                    checkD = False
                    break
            
            for n in range(j - 1, -1, -1):
                if tree_matrix[i][n] >= curTree:
                    checkL = False
                    break
            
            for n in range(j + 1, columns):
                if tree_matrix[i][n] >= curTree:
                    checkR = False
                    break
            
            if checkL or checkR or checkU or checkD:
                visible_trees.add((i, j))
    print(len(visible_trees))
    
    