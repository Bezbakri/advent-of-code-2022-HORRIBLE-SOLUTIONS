# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 23:41:39 2022

@author: bezbakri
"""

with open("index2") as f:
    rawList = f.readlines()
    score = 0
    for line in rawList:
        if "A" in line:
            if "Y" in line:
                score += 8
            elif "X" in line:
                score += 4
            else:
                score += 3
        elif "B" in line:
            if "Z" in line:
                score += 9
            elif "Y" in line:
                score += 5
            else:
                score += 1
        else:
            if "X" in line:
                score += 7
            elif "Z" in line:
                score += 6
            else:
                score += 2
    print(score)