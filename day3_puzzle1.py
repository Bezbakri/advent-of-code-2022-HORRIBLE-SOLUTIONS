# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:19:14 2022

@author: bezbakri
"""

scoreMap = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8, "i" : 9, "j" : 10,
            "k" : 11, "l" : 12, "m" : 13, "n" : 14, "o" : 15, "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20,
            "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25, "z" : 26}

with open("input3") as f:
    rawTextList = f.readlines()
    score = 0
    for rawLine in rawTextList:
        lessRawLine = rawLine.strip("\n")
        firstpart, secondpart = lessRawLine[:len(lessRawLine)//2], lessRawLine[len(lessRawLine)//2:]
        for letter in firstpart:
            if letter in secondpart:
                if letter.islower():
                    score += scoreMap[letter]
                else:
                    score += scoreMap[letter.lower()] + 26
                break
            
    print(score)
    