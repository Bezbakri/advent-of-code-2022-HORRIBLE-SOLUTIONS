# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 00:00:00 2022

@author: bezbakri
"""

with open("index2") as f:
    rawList = f.readlines()
    score = 0
    for line in rawList:
        if "A" in line:
            if "X" in line:
                score += 3
            elif "Y" in line:
                score += 4
            else:
                score += 8
        elif "B" in line:
            if "X" in line:
                score += 1
            elif "Y" in line:
                score += 5
            else:
                score += 9
        else:
            if "X" in line:
                score += 2
            elif "Y" in line:
                score += 6
            else:
                score += 7
    print(score)