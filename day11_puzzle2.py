# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 00:44:27 2022

@author: bezbakri
"""

# I REFUSE TO PARSE THIS ONE

monkeyDict = {0: {"items" : [99, 63, 76, 93, 54, 73], "operation" : "old * 11", "test" : "new % 2 == 0", True : 7, False : 1, "inspections" : 0},
              1 : {"items" : [91, 60, 97, 54], "operation" : "old + 1", "test" : "new % 17 == 0", True : 3, False : 2, "inspections" : 0}, 
              2 : {"items" : [65], "operation" : "old + 7", "test" : "new % 7 == 0", True : 6, False : 5, "inspections" : 0}, 
              3 : {"items" : [84, 55], "operation" : "old + 3", "test" : "new % 11 == 0", True : 2, False : 6, "inspections" : 0}, 
              4 : {"items" : [86, 63, 79, 54, 83], "operation" : "old * old", "test" : "new % 19 == 0", True : 7, False : 0, "inspections" : 0}, 
              5 : {"items" : [96, 67, 56, 95, 64, 69, 96], "operation" : "old + 4", "test" : "new % 5 == 0", True : 4, False : 0, "inspections" : 0}, 
              6 : {"items" : [66, 94, 70, 93, 72, 67, 88, 51], "operation" : "old * 5", "test" : "new % 13 == 0", True : 4, False : 5, "inspections" : 0}, 
              7 : {"items" : [59, 59, 74], "operation" : "old + 8", "test" : "new % 3 == 0", True : 1, False : 3, "inspections" : 0}}


funnyModulo = 1

for monkey in monkeyDict:
    funnyModulo *= int(monkeyDict[monkey]["test"].split()[2])
    
print(funnyModulo)


for i in range(10000):
    for monkey in monkeyDict:
        curList = monkeyDict[monkey]["items"].copy()
        for old in curList:
            new = eval(monkeyDict[monkey]["operation"]) % funnyModulo
            monkeyDict[monkey]["inspections"] += 1
            monkeyToGetItem = monkeyDict[monkey][eval(monkeyDict[monkey]["test"])]
            monkeyDict[monkey]["items"].remove(old)
            monkeyDict[monkeyToGetItem]["items"].append(new)
    


inspectionsList = []

for monkey in monkeyDict:
    inspectionsList.append(monkeyDict[monkey]["inspections"])
    
inspectionsList.sort()
print(inspectionsList[-1] * inspectionsList[-2])