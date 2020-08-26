#!/usr/bin/env python3
"""Q: Given a linked list(only access to head), find whether 
the linked list has a loop or not i.e. the end of the linked 
list points to an internal node or not using no other data 
structures.



=================================================
Soln: We take 2 references, 1 is made to skip/hop 1 node at a 
time i.e. normal linked list traversal, and another is made to 
hop 2 nodes at a time, i.e. it skips 1 node and points to the 
2nd node in each itteration. If a loop exists then both the 
node will be pointing to the same node at some point.
"""

from node import Node
from linked_list import LinkedList

def loop_exists(head:Node) -> bool:
    ref1 = head
    ref2 = head
    loop_exists = False

    while ref1 != None and ref2 != None:
        ref1 = ref1.get_next()
        ref2 = ref2.get_next()
        if ref2 == None:
            break
        ref2 = ref2.get_next()
        if ref2 == ref1:
            loop_exists = True
            break

    return loop_exists


if __name__ == '__main__':
    ll = LinkedList()
    for i in range(20):
        ll.insert_at_begenning(i)
    loop_node = ll.get_node_at_pos(13)
    tail_node = ll.get_node_at_pos(ll.len-1)
    tail_node.set_next(loop_node)
    if loop_exists(ll.head):
        print('===========Passed============')
    else:
        print('============Failed============')