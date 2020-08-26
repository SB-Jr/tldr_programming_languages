#!/usr/bin/env python3

"""
Q: Given an expression check whether the brackets are properly opened and closed.



====================================================================
Soln: For each bracket opened push it into a stack and while closing check whether 
the proper openeing bracket is on the top of the stack.
"""
from linked_list_stack import LinkeListStack


def check_brackets(expression: str) -> bool:
    if len(expression) < 3:
        return True
    stack = LinkeListStack[str]()
    bracket_relation = {
        '[': ']',
        '{': '}',
        '(': ')'
    }
    opening_bracket = ['[', '{', '(']
    closing_bracket = [']', '}', ')']
    for s in expression:
        if s in closing_bracket:
            if stack.is_empty():
                return False
            elif stack.top() == s:
                stack.pop()
            else:
                return False
        if s in opening_bracket:
            stack.push(bracket_relation.get(s))
    return True if stack.is_empty() else False


if __name__ == '__main__':
    expr1 = '(1+5)'
    if check_brackets(expr1) == True:
        print('==========Passed===========')
    else:
        print('==========Failed============')

    expr2 = '[1 + x + y + (2 + y)^3+ {(xy + 4)(2+x)}]'
    if check_brackets(expr2) == True:
        print('===========Passed===========')
    else:
        print('==========Failed=============')

    expr3 = '(2+4})]'
    if check_brackets(expr3) == False:
        print("============Passed============")
    else:
        print('=========Failed===============')