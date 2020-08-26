#!/usr/bin/env python3

"""
Q: For a given array of no. find the maximum span for an integer in the array, i.e. find the maximum of j-i where all A[i] < A[j]
eg: A = [6,3,4,5,2] here at j = 3, A[j] = 5 and the maximum span is [3,4,5] i.e. at j=3, there are maximum continious A[i] < A[j]



==============================================================
Soln: loop through the array, and insert a tuple into a stack where the tuple will contain the i-th integer and the max no of span it has come across since the last no. If the top of the stack has integer <= the i-th integer then the span for A[i] will be 1+ span(top of stack integer)
"""

from linked_list_stack import LinkeListStack
from typing import List
from typing import Tuple

def maximum_span(arr:List[int]) -> Tuple[int, int]:
    if arr == None or len(arr) == 0:
        return (-1, -1)
    s = LinkeListStack[Tuple[int, int]]()
    for a in arr:
        if s.is_empty():
            s.push((a, 1))
        elif a >= s.top()[0]:
            s.push((a, s.top()[1]+1))
        else:
            s.push((a, 1))
    max_int = -1
    max_span = -1
    while not s.is_empty():
        a, span = s.pop()
        if span == max_span and a > max_int:
            max_int = a
            max_span = span
        if span > max_span:
            max_int = a
            max_span = span
    return (max_int, max_span)


if __name__ == "__main__":
    arr = [6, 3, 4, 5, 2]
    (max_int, max_span) = maximum_span(arr)
    if max_int == 5 and max_span == 3:
        print('=================Passed=====================')
    else:
        print('==================Failed======================')
