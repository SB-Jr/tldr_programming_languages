#!/usr/bin/env python3

"""
Q: Given a series of continuous no (eg: 1,2,3,4,5,6) predict whether a permutation of the input is possible by push and pop operation using 1 stack. If possible, then state the order in which the numbers have to be pushed and poped out from the stack. Use 'S' for push and 'X' for pop.


========================================================================================
Soln: As we encounter the numbers in the permutation string we can either check if the number is top of the stack or if the number can be encountered using push operation on the input. If the input stream ends by mulitple pushing and the top of the stack never points to the permutation digit then we can declare that the permutation is not possible. 
"""

from linked_list_stack import LinkeListStack


def check_permutation(n:int, perm:str) -> str:
    op = ''
    if len(perm) != n:
        return None
    if n == 0:
            op = ''
            return op
    if n == 1:
        if len(str) == 1 and perm[0] == '1':
            op = 'SX'
            return op
        else:
            return None

    s = LinkeListStack[str]()
    inp = [str(i) for i in range(1, n+1)]
    for p in perm:
        if int(p) > n:
            return None 
        if not s.is_empty() and s.top() == p:
            op = op + 'X'
            s.pop()
        else:
            if len(inp) == 0:
                return None
            while len(inp) != 0:
                s.push(inp[0])
                inp.remove(inp[0])
                op = op + 'S'
                if s.top() == p:
                    s.pop()
                    op = op + 'X'
                    break
    if not s.is_empty():
        return None
    return op


if __name__ == '__main__':
    n = 6
    expected_op = 'SSSXXSSXSXXX'
    inp =  '325641'
    op = check_permutation(n,inp)
    if  op == expected_op:
        print('=============Passed================')
    else:
        print('Expected: '+expected_op)
        print('But got: '+ op)
    inp = '154623'
    op = check_permutation(n, inp)
    if op == None:
        print('=============Passed================')
    else:
        print('Expected None as permutation is wrong')
        print('But got: '+op)