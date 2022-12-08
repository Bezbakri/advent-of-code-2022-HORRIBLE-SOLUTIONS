# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 19:48:22 2022

@author: bezbakri
"""

with open("input5") as f:
    rawTextLines = f.read().split("\n")
    matrix = []
    countOfRows = 0
    for i in rawTextLines:
        if "[" in i:
            countOfRows += 1
        else:
            break
    rawMatrix = rawTextLines[:countOfRows]
    instructions = rawTextLines[countOfRows + 2: -1]
    
    number_of_columns = int(rawTextLines[countOfRows].strip()[-1])
    for i in range(number_of_columns):
        matrix.append([])
    for i in rawMatrix[-1: : -1]:
        columnNumber = 0
        for j in range(0, len(i), 4):
            if i[j + 1] != " ":
                matrix[columnNumber].append(i[j + 1])
            columnNumber += 1
            
    instructionsList = []
            
    for line in instructions:
        rawLineList = line.strip().split(" ")
        lineList = []
        for word in rawLineList:
            if word.isnumeric():
                lineList.append(int(word))
        instructionsList.append(lineList)
        
    for inst in instructionsList:
        stuff = []
        for i in range(inst[0]):
            stuff.append(matrix[inst[1] - 1].pop())
        for i in range(len(stuff)):
            matrix[inst[2] - 1].append(stuff.pop())
    for column in matrix:
        print(column[-1], end = "")