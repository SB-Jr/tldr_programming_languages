#! /usr/bin/env python3

"""Q: Generate all binary strings for a given string length 'n' also known as the 
k-ary String generation""" 

import sys

def k_ary_strings(n: int):
    # base case
    if n == 0:
        return []
    elif n == 1:
        return ['0', '1']
    # recursion case
    binary_string_n_1 = k_ary_strings(n-1)
    binary_string_n = ['0'+i for i in binary_string_n_1] + ['1' + i for i in binary_string_n_1]
    return binary_string_n

print(k_ary_strings(int(sys.argv[1])))