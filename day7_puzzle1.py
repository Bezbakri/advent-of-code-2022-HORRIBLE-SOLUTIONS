# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 14:17:40 2022

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
        print(cwd.getName(), cwd.getSize())
    return root

def getSizeIfLessThan100000(directory : Directory) -> int:
    sum = directory.getSize() if directory.getSize() <= 100000 else 0
    for subDir in directory.directories:
        sum += getSizeIfLessThan100000(subDir)
    return sum

with open("input7") as f:
    rawText = f.read()
    parsed = parseInstructions(rawText)
    print(getSizeIfLessThan100000(parsed))
        

        