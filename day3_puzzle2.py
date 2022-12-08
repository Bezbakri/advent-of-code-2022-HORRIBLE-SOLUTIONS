# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 11:47:40 2022

@author: bezbakri
"""

scoreMap = {"a" : 1, "b" : 2, "c" : 3, "d" : 4, "e" : 5, "f" : 6, "g" : 7, "h" : 8, "i" : 9, "j" : 10,
            "k" : 11, "l" : 12, "m" : 13, "n" : 14, "o" : 15, "p" : 16, "q" : 17, "r" : 18, "s" : 19, "t" : 20,
            "u" : 21, "v" : 22, "w" : 23, "x" : 24, "y" : 25, "z" : 26}

with open("input3") as f:
    rawTextList = f.readlines()
    score = 0
    for i in range(len(rawTextList)):
        if i % 3 == 0:
            rawLine1, rawLine2, rawLine3 = rawTextList[i].strip("\n"), rawTextList[i + 1].strip("\n"), rawTextList[i + 2].strip("\n")
            for letter in rawLine1:
                if letter in rawLine2 and letter in rawLine3:
                    if letter.islower():
                        score += scoreMap[letter]
                    else:
                        score += scoreMap[letter.lower()] + 26
                    break
    print(score)