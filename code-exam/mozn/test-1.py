#!/usr/bin/env python3

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    up = 0
    down = 0
    left = 0
    right = 0
    mx = 0

    for c in S:
        if c == '^':
            up += 1
        elif c == 'v':
            down += 1
        elif c == '>':
            left += 1
        elif c == '<':
            right += 1
        
        mx = max(max(up, down), max(left, right))

    directions = [up , down, left, right]
    maximum_index = 0
    maximum = 0
    lowet_sum = 0
    for i in range(0, 4):
        if(directions[i] > maximum):
            maximum = directions[i]
            maximum_index = i

    for i in range(0, 4):
        if(maximum_index != i):
            lowet_sum = lowet_sum + directions[i]

    return  lowet_sum
