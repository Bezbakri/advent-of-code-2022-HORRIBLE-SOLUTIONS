# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 12:46:07 2022

@author: bezbakri
"""

def moveHead(headPos : tuple, letter : str) -> tuple:
    moveMap = {"U" : (0, 1), "D" : (0, -1), "L" : (-1, 0), "R" : (1, 0)}
    headPos = (headPos[0] + moveMap[letter][0], headPos[1] + moveMap[letter][1])
    return headPos

def follow(tailPos : tuple, headPos : tuple) -> tuple:
    if abs(tailPos[0] - headPos[0]) <= 1 and abs(tailPos[1] - headPos[1]) <= 1:
        return tailPos
    (tailX, tailY), (headX, headY) = tailPos, headPos
    if tailX == headX:
        tailY += int(tailY < headY) * 2 - 1
    elif tailY == headY:
        tailX += int(tailX < headX) * 2 - 1
    else:
        tailX += int(tailX < headX) * 2 - 1
        tailY += int(tailY < headY) * 2 - 1
    tailPos = (tailX, tailY)    
    return tailPos

with open("input9") as f:
    instructions = [{x[0]: int(x[2:4])} for x in f]
    
    startPos = (0, 0)
    head, one, two, three, four, five, six, seven, eight, nine = startPos, startPos, startPos, startPos, startPos, startPos, startPos, startPos, startPos, startPos
    tailPosSet = set()
    for inst in instructions:
        for letter in inst:
            for i in range(inst[letter]):
                head = moveHead(head, letter)
                one = follow(one, head)
                two = follow(two, one)
                three = follow(three, two)
                four = follow(four, three)
                five = follow(five, four)
                six = follow(six, five)
                seven = follow(seven, six)
                eight = follow(eight, seven)
                nine = follow(nine, eight)
                
                
                tailPosSet.add(nine)
    print(len(tailPosSet))
    
                

    
    