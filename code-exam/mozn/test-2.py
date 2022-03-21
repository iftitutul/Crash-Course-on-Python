# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import collections

def solution(S):
    # write your code in Python 3.6
    con = collections.defaultdict(int);        
    for c in S:
       con[c] += 1
    return min(con['B'], con['A'], con['L']//2, con['O']//2, con['N'])