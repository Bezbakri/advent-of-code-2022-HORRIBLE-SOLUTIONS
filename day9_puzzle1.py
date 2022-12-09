# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 11:19:55 2022

@author: bezbakri
"""

with open("input9") as f:
    instructions = [{x[0]: int(x[2:4])} for x in f]
    moveMap = {"U" : (0, 1), "D" : (0, -1), "L" : (-1, 0), "R" : (1, 0)}
    startPos = [0, 0]
    headPos, tailPos = startPos, startPos
    tailPosSet = set(startPos)
    for inst in instructions:
        for letter in inst:
            for i in range(inst[letter]):
                prevHeadPos = headPos
                headPos = [headPos[0] + moveMap[letter][0], headPos[1]+ moveMap[letter][1]]
                tailPos = tailPos if abs(tailPos[0] - headPos[0]) <= 1 and abs(tailPos[1] - headPos[1]) <= 1 else prevHeadPos
                tailPosSet.add(tuple(tailPos))
                
    print(len(tailPosSet))