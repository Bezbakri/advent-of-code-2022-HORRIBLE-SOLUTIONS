# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 23:10:20 2022

@author: bezbakri
"""

test_input = """addx 15
addx -11
addx 6
addx -3
addx 5
addx -1
addx -8
addx 13
addx 4
noop
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx 5
addx -1
addx -35
addx 1
addx 24
addx -19
addx 1
addx 16
addx -11
noop
noop
addx 21
addx -15
noop
noop
addx -3
addx 9
addx 1
addx -3
addx 8
addx 1
addx 5
noop
noop
noop
noop
noop
addx -36
noop
addx 1
addx 7
noop
noop
noop
addx 2
addx 6
noop
noop
noop
noop
noop
addx 1
noop
noop
addx 7
addx 1
noop
addx -13
addx 13
addx 7
noop
addx 1
addx -33
noop
noop
noop
addx 2
noop
noop
noop
addx 8
noop
addx -1
addx 2
addx 1
noop
addx 17
addx -9
addx 1
addx 1
addx -3
addx 11
noop
noop
addx 1
noop
addx 1
noop
noop
addx -13
addx -19
addx 1
addx 3
addx 26
addx -30
addx 12
addx -1
addx 3
addx 1
noop
noop
noop
addx -9
addx 18
addx 1
addx 2
noop
noop
addx 9
noop
noop
noop
addx -1
addx 2
addx -37
addx 1
addx 3
noop
addx 15
addx -21
addx 22
addx -6
addx 1
noop
addx 2
addx 1
noop
addx -10
noop
noop
addx 20
addx 1
addx 2
addx 2
addx -6
addx -11
noop
noop
noop"""

with open("input10") as f:
    instructions = [x.split() for x in f]
    list_of_signal_strengths = []
    x = 1
    cycle = 0
    funny_cycle_numbers = [20, 60, 100, 140, 180, 220]
    for instruction in instructions:
        cycle += 1
        if cycle in funny_cycle_numbers:
            list_of_signal_strengths.append(cycle * x)
            print(instruction, "part 1")
            print(cycle, x * cycle)
        if instruction[0] == "noop":
            continue
        else:
            cycle += 1
            if cycle in funny_cycle_numbers:
                list_of_signal_strengths.append(cycle * x)
                print(instruction)
                print(cycle, x * cycle)
            x += int(instruction[1])
            
        
    print(sum(list_of_signal_strengths))