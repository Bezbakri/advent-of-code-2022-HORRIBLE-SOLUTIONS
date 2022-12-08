# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 21:13:07 2022

@author: bezbakri
"""

class Directory:
    def __init__(self, name, parent = None):
        self.name = name
        self.parent = parent
        self.files = {}
        self.directories = []
        
    def addDir(self, dir_name):
        if dir_name not in [i.getName() for i in self.directories]:
            directory = Directory(dir_name, self)
            self.directories.append(directory)
    
    def getName(self) -> str:
        return self.name
    
    def addFile(self, fName, fSize):
        if fName not in self.files:
            self.files[fName] = fSize
    
    def goUp(self):
        return self.parent
    
    def getSize(self) -> int:
        size = 0
        size += sum(self.files[x] for x in self.files)
        size += sum(x.getSize() for x in self.directories)
        return size
    
def parseInstructions(rawText):
    
    lines = rawText.split("\n")
    root = Directory("/")
    cwd = root
    for line in lines:
        words = line.split(" ")
        if words[0] == "$":
            if words[1] == "ls":
                continue
            else:
                if words[2] == "/":
                    cwd = root
                elif words[2] == "..":
                    cwd = cwd.goUp()
                else:
                    for subDir in cwd.directories:
                        if subDir.getName() == words[2]:
                            cwd = subDir
        elif words[0] == "dir":
            cwd.addDir(words[1])
        elif words[0].isnumeric():
            cwd.addFile(words[1], int(words[0]))
    return root

def smallestBigDir(directory : Directory, target : int) -> int:
    if directory.getSize() < target:
        return None
    size = directory.getSize()
    for subDir in directory.directories:
        subSize = smallestBigDir(subDir, target)
        if subSize:
            size = subSize if not size else min(size, subSize)
    return size

with open("input7") as f:
    rawText = f.read()
    parsed = parseInstructions(rawText)
    target = 30000000 - (70000000 - parsed.getSize())
    print(smallestBigDir(parsed, target))