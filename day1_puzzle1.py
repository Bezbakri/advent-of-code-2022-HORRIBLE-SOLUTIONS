# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 14:56:40 2022

@author: bezbakri
"""

with open("index") as f:
    rawText = f.read()
    rawList = rawText.split("\n")
    sum = 0
    sumList = []
    for i in rawList:
        if i != "":
            sum += int(i)
        else:
            sumList.append(sum)
            sum = 0
    sumList.sort()
    lastIndex = len(sumList) - 1
    top3sum = 0
    for i in range(3):
        top3sum += sumList[lastIndex]
        lastIndex -= 1
    print(top3sum)