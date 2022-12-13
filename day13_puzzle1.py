# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 23:08:43 2022

@author: bezbakri
"""

import ast

def comparable(a, b) -> int:
    for i in range(min(len(a), len(b))):
        if type(a[i]) != type(b[i]):
            if type(a[i]) is int:
                a[i] = [a[i]]
            else:
                b[i] = [b[i]]
        if type(a[i]) is int:
            if a[i] < b[i]:
                return -1
            elif a[i] > b[i]:
                return 1
        else:
            possibleReturn = comparable(a[i], b[i])
            if possibleReturn:
                return possibleReturn
    if len(a) == len(b):
        return 0
    elif len(a) < len(b):
        return -1
    else:
        return 1

with open("input13") as f:
    rawList = [(ast.literal_eval(x.split("\n")[0]), ast.literal_eval(x.split("\n")[1])) for x in f.read().strip().split("\n\n")]
    answer = 0
    for i, (a, b) in enumerate(rawList):
        if comparable(a, b) == -1:
            answer += i + 1
    print(answer)