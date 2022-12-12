# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 23:14:04 2022

@author: bezbakri
"""

def parseInput(rawText : str) -> tuple:
    grid = [list(x) for x in rawText.split("\n")]
    for i, row in enumerate(grid):
        for j, letter in enumerate(row):
            if letter == "S":
                startPos = (i, j)
                grid[i][j] = "a"
            elif letter == "E":
                endPos = (i, j)
                grid[i][j] = "z"
                
    return grid, startPos, endPos

def distFinder(grid : list, start : tuple, end : tuple) -> int:
    dumbList = list()
    dumbList.append((start, 0))
    beenTo = set()
    while True:
        curPos, dist = dumbList.pop(0)
        if curPos == end:
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
    

with open("input12") as f:
    rawText = f.read().strip()
    grid, startPos, endPos = parseInput(rawText)
    print(distFinder(grid, startPos, endPos))