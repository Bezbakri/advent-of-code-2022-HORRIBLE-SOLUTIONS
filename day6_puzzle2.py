# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 14:56:20 2022

@author: bezbakri
"""

with open("input6") as f:
    rawText = f.read().strip()
    first3ofMarker = rawText[0:13]
    for i in range(13, len(rawText)):
        curChar = rawText[i]
        if curChar in first3ofMarker:
            first3ofMarker = first3ofMarker[1:] + curChar
            print(first3ofMarker)
        else:
            if len(set(first3ofMarker)) < len(first3ofMarker):
                first3ofMarker = first3ofMarker[1:] + curChar
                print(first3ofMarker)
            else:
                print(i + 1)
                break