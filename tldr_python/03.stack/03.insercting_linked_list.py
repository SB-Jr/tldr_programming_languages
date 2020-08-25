#!/usr/bin/env python3

"""
Q: Given head of 2 linked list, which might or might not intersect at some point, determine the node where they intersect.



============================================
Soln: Here we can use a 2 stacks to push the elements of each linked list into and then pop out until the top of stack is not same. If the stack top is not same for the first itteration itself then we can say that the linked list never intersected, else the node just poped out after which the top is different is the node where the linked list intersect. 
"""

from node import Node
from linked_list import LinkedList
from linked_list_stack import LinkeListStack


def check_linked_list_intersection(head1: Node, head2: Node) -> Node:
    if head1 == None or head2 == None:
        return None
    s1 = LinkeListStack[Node]()
    s2 = LinkeListStack[Node]()
    ref1 = head1
    ref2 = head2
    while ref1 is not None:
        s1.push(ref1)
        ref1 = ref1.get_next()

    while ref2 is not None:
        s2.push(ref2)
        ref2 = ref2.get_next()

    if s1.top() != s2.top():
        return None
    else:
        prev_node = None
        while s1.top()  == s2.top():
            prev_node = s1.top()
            s1.pop()
            s2.pop()
        return prev_node


if __name__ == '__main__':
    ll1 = LinkedList()
    ll2 = LinkedList()
    ll3 = LinkedList()
    for i in range(10):
        ll1.insert_at_begenning(i)
    
    for i in range(30, 45):
        ll2.insert_at_begenning(i)

    for i in range(70,80):
        ll3.insert_at_begenning(i)

    if check_linked_list_intersection(ll1.head, ll2.head) == None:
        print('===========Passed===============')
    else:
        print('===========Failed=================')

    node_ll1 = ll1.get_node_at_pos(ll1.len-1)
    node_ll1.set_next(ll3.head)
    node_ll2 = ll2.get_node_at_pos(ll2.len-1)
    node_ll2.set_next(ll3.head)

    print(ll1.display_list())
    print(ll2.display_list())

    if check_linked_list_intersection(ll1.head, ll2.head) == ll3.head:
        print('Merge found at '+ str(ll3.head.get_data()))
        print('===========Passed===============')
    else:
        print('===========Failed=================')