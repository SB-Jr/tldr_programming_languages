#!/usr/bin/env python3

"""Q: Generate all strings of length n drawn from 0....{k-1}
"""

import sys

def k_string(k:int, n:int):
    #base case
    if n==0:
        return []
    elif n==1:
        return [i for i in range(k)]
    #recursion case
    n_1_k_string = k_string(k, n-1)
    n_string = []
    for i in range(k):
        for j in n_1_k_string:
            n_string.append(str(i) + str(j))
    return n_string

print(k_string(int(sys.argv[1]), int(sys.argv[2])))