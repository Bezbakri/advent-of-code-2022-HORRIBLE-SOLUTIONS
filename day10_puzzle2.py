# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 23:30:37 2022

@author: bezbakri
"""

with open("input10") as f:
    instructions = [x.split() for x in f]
    list_of_display_values = []
    x = 1
    cycle = 0
    curString = ""
    for instruction in instructions:
        cycle += 1
        if cycle in range(x - 1, x + 2):
            curString += "#"
        else:
            curString += "."
        if cycle == 40:
            cycle = 0
            list_of_display_values.append(curString)
            curString = ""
        if instruction[0] == "noop":
            continue
        else:
            cycle += 1
            if cycle in range(x - 1, x + 2):
                curString += "#"
            else:
                curString += "."
            if cycle == 40:
                cycle = 0
                list_of_display_values.append(curString)
                curString = ""
            x = (x + int(instruction[1]))
            print(x, instruction[1])
    for i in list_of_display_values:
        print(i)
    print(curString)