# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 00:31:16 2022

@author: bezbakri
"""

from collections import deque

def parseInput(rawText : str) -> tuple:
    grid = [list(x) for x in rawText.split("\n")]
    aList = []
    for i, row in enumerate(grid):
        for j, letter in enumerate(row):
            if letter == "S":
                aList.append((i, j))
                grid[i][j] = "a"
            elif letter == "E":
                endPos = (i, j)
                grid[i][j] = "z"
            elif letter == "a":
                aList.append((i, j))
                
    return grid, aList, endPos

def distFinder(grid : list, start : tuple, end : tuple) -> int:
    dumbList = deque()
    dumbList.append((start, 0))
    beenTo = set()
    while dumbList:
        curPos, dist = dumbList.popleft()
        if curPos == end:
            print(1)
            return dist
        if curPos in beenTo:
            continue 
        beenTo.add(curPos)
        x, y = curPos
        for dx, dy in ((0, 1), (1, 0), (0, -1), (-1, 0)):
            if (
                0 <= x + dx < len(grid)
                and 0 <= y + dy < len(grid[0])
                and ord(grid[x + dx][y + dy]) - ord(grid[x][y]) <= 1
            ):
                dumbList.append(((x + dx, y + dy), dist + 1))
    return float("inf")
    

with open("input12") as f:
    rawText = f.read().strip()
    grid, aList, endPos = parseInput(rawText)
    print(aList)
    print(min(distFinder(grid, a, endPos) for a in aList))