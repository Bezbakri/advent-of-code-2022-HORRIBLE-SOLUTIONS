# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 16:56:40 2022

@author: bezbakri
"""

import collections

starter = (500, 0)
T = collections.defaultdict(lambda: True)
with open("input14") as f:
    lines = [x.strip().split("->") for x in f]
for line in lines:
    pairs = [tuple(map(int, pair.split(','))) for pair in line]
    for (a, b), (c, d) in zip(pairs, pairs[1:]):
        for i in range(min(a, c), max(a, c)+1):
            for j in range(min(b, d), max(b, d)+1):
                T[i, j] = False
maxy = max(y for _, y in T)

def solve(fn):
    p = lambda x, y: (x, y) if T[x, y] and y < maxy+2 else None
    for i in range(100000):
        x, y = starter
        while True:
            nx, ny = p(x, y+1) or p(x-1, y+1) or p(x+1, y+1) or (None, None)
            if nx is None: break
            x, y = nx, ny
        if fn(x, y): return i
        T[x, y] = False
        
total1 = solve(lambda x, y: y > maxy)
total2 = total1 + solve(lambda x, y: (x, y) == (500, 0)) + 1
print(total1, total2)