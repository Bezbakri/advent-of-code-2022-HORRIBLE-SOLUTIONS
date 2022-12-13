# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 00:09:35 2022

@author: bezbakri
"""

import ast

def comparable(a, b) -> int:
    if type(a) is int and type(b) is int:
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0
    elif type(a) is int and type(b) is list:
        a = [a]
    elif type(a) is list and type(b) is int:
        b = [b]
    for x, y in zip(a, b):
        possibleReturn = comparable(x, y)
        if possibleReturn != 0:
            return possibleReturn
    if len(a) > len(b):
        return 1
    elif len(a) == len(b):
        return 0
    else:
        return -1

with open("input13") as f:
    rawList = [(ast.literal_eval(x.split("\n")[0]), ast.literal_eval(x.split("\n")[1])) for x in f.read().strip().split("\n\n")]
packets = []
for a, b in rawList:
    packets.append(a)
    packets.append(b)
packets.append([[2]])
packets.append([[6]])
for j in range(1, len(packets)):
    key = packets[j]
    i = j - 1
    while ((i > -1) and comparable(packets[i], key) > 0):
        packets[i + 1] = packets[i]
        i -= 1
    packets[i + 1] = key
x = y = 0
for i in range(len(packets)):
    if packets[i] == [[2]]:
        x = i
    if packets[i] == [[6]]:
        y = i
print(packets)
print((x + 1) * (y + 1))
    