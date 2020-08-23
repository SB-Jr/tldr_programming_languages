#!/usr/bin/env python3

"""Q: Reverse a single linked list without using any kind of data structure.





========================================
Soln: We will here use 3 references. At any 
given point the linked list will have 2 
sections, 1st will be the reverse order upto 
that point and the 2nd will be the existing 
correct ordered linked list. When we are at 
the i-th node, the first 2 reference nodes 
will be used to reverse the order for (i-1) 
and (i-2) th node and 3rd reference will be 
pointing to i th node to continue the process. 
"""

from node import Node
from linked_list import LinkedList
import sys


def rev_linked_list(head:Node) -> Node:
    # ref1 will point to node that needs to be rearranged
    ref1 = head
    if ref1 == None:
        return head
    # ref2 will point to the new head of reversed linked list
    ref2 = ref1.get_next()
    if ref2 == None:
        return head
    # ref3 is a reference to cary out the operation on the remaining of the linked list
    ref3 = ref2.get_next()
    # initial swapping
    ref2.set_next(ref1)
    ref1.set_next(None)
    ref1 = ref3
    while ref1 != None:
        # swap nodes
        ref3 = ref3.get_next()
        ref1.set_next(ref2)
        ref2 = ref1
        ref1 = ref3
    return ref2


if __name__ == '__main__':
    ll = LinkedList()
    n = int(sys.argv[1]) if sys.argv[1] is not None else 10
    for i in range(n):
        ll.insert_at_begenning(i)
    print(ll.display_list())
    new_head = rev_linked_list(ll.head)
    ll.head = new_head
    print(ll.display_list())