# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 11:56:37 2022

@author: bezbakri
"""

with open("input4") as f:
    rawTextList = f.read().strip().split("\n")
    fullyContainedNumbers = 0
    for item in rawTextList:
        firstRange, secondRange = item.split(",")
        firstRange, secondRange = firstRange.strip(), secondRange.strip()
        firstRangeNumOne, firstRangeNumTwo = firstRange.split("-")
        secondRangeNumOne, secondRangeNumTwo = secondRange.split("-")
        firstRangeNumOne, firstRangeNumTwo = int(firstRangeNumOne), int(firstRangeNumTwo)
        secondRangeNumOne, secondRangeNumTwo = int(secondRangeNumOne), int(secondRangeNumTwo)
        if firstRangeNumOne <= secondRangeNumTwo and firstRangeNumTwo >= secondRangeNumOne:
            fullyContainedNumbers += 1
    print(fullyContainedNumbers)
        