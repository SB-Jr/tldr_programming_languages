#!/usr/bin/env python3

"""Q: Find the max length of connected 1's in a given matrix of 0's and 1's. (connected cells are cells with 1's and are either adjecent to each other horizonatally or vertically or diagonally)
eg: 1 1 0 0 0
       0 1 0 0 0
       0 1 0 0 0
       0 0 1 1 0
       0 0 0 1 0
       Answer:= 7
"""
import sys
from typing import List


def start_graph_traversal(arr:List[list]) -> int:
    # get graph dimensions
    (has_dim, n, m) = get_graph_dimensions(arr)
    if not has_dim:
        return 0
    else:
        # check if graph has only 1 cell
        if n == 1:
            if m == 1:
                return arr[0][0]
        #visited = [[0]*m]*n
        # the above way to create 2D array has a big caveat 
        # that all the sub-arrays share same address as a
        #  result, changing 1 value will change all the values 
        # of all the arrays
        visited = [[0 for i in range(m)] for j in range(n)]
        max_len = 0
        for i in range(n):
            for j in range(m):        
                cur_len = get_max_length(n, m, arr, i, j, visited)
                max_len = cur_len if cur_len > max_len else max_len
        return max_len

def get_graph_dimensions(arr:List[list])->(bool, int, int):
    n = len(arr)
    if n >= 0:
        m = len(arr[0])
        return (True, n, m)
    else:  #return length 0 is graph has no rows
        return (False, 0 ,0)

def get_max_length(n, m, arr:List[list], row:int, col:int, visited_arr:List[list]) -> int:
    #base case
    # check if current cell is out of the graph
    if row >= n or col >= m or col < 0 or row < 0:
        return 0
    # check if current cell has been traversed
    if visited_arr[row][col] == 1:
        return 0
    # Dont calculate further if current cell is 0
    if arr[row][col] == 0:
        return 0

    # recursive case
    visited_arr[row][col] = 1
    max_len = 0
    # lock the current cell to break infinite looping
    len_right = get_max_length(n, m, arr, row, col+1, visited_arr)
    len_left = get_max_length(n, m, arr, row, col-1, visited_arr)
    len_down = get_max_length(n, m, arr, row+1, col, visited_arr)
    len_diagonal = get_max_length(n, m, arr, row+1, col+1, visited_arr)

    max_len = max([len_left, len_right, len_down, len_diagonal])
    # release current cell so that others can count it if required
    visited_arr[row][col] = 0
    return max_len + 1


# Read file for input
if len(sys.argv) != 2:
    print('Enter 1 file name for input, only!!')
    exit

file_obj = open(sys.argv[1],  'r')
line_arr = file_obj.read().split('\n')
arr = []
for line in line_arr:
    temp_arr = line.split(' ')
    try:
        arr.append([int(i) for i in temp_arr])
    except Exception as e:
        pass

print('Entered Graph:')
for row in arr:
    print(row)

print(start_graph_traversal(arr))