#!/usr/bin/env python3

"""Q: Given the head of 2 linked list, and said that the 
linked list might merge at some point i.e. the ending k nodes 
of the linked list are same, and the k-th node from the end is 
the merging point, find the merging point in linear time.





=================================================
Soln: Traverse the first list and keep inserting the elements 
from the list into a set. Now traverse the 2nd list, and start 
inserting the elements of the 2nd list into the set. The node 
for which the insertion will fail(set can't contain duplicate 
items), is the mergin point of both the linked list.
"""


from node import Node
from linked_list import LinkedList

def get_merge_point(head1: Node, head2: Node) -> Node:
    s = set()
    ref1 = head1
    while ref1 is not None:
        s.add(ref1)
        ref1 = ref1.get_next()
    
    ref2 = head2
    while ref2 is not None:
        if ref2 in s:
            break
        ref2 = ref2.get_next()
    return ref2



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

    node_ll1 = ll1.get_node_at_pos(ll1.len-1)
    node_ll1.set_next(ll3.head)
    node_ll2 = ll2.get_node_at_pos(ll2.len-1)
    node_ll2.set_next(ll3.head)

    print(ll1.display_list())
    print(ll2.display_list())

    if get_merge_point(ll1.head, ll2.head) == ll3.head:
        print('Merge found at '+ str(ll3.head.get_data()))
        print('===========Passed===============')
    else:
        print('===========Failed=================')
