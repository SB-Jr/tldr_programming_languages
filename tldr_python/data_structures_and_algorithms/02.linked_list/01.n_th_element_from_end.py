#!/usr/bin/env python3

"""Q: Find the n th element from the end of a
linked list, in just 1 scan i.e. we can 
traverse the list only once. The length of 
the linked list is not known, we only have 
the access to the head of the linked list.


==========================================
Solution: This can be done by using 2 
reference to the same linked list, both 
referring to the head of linked list. The 
first reference will be used to traverse the 
list and when it will reach the n th element, 
theron the other reference will also be 
updated to move ahead with each move made by 
the initial reference. This way when the 
first reference will reach the end of the 
linked list, the other reference would have 
reached the n the element from end.  
"""


from linked_list import LinkedList
from node import Node

def n_th_element_from_end(head: Node, n:int) -> Node:
    ref1 = head
    ref2 = head
    counter = 1
    if ref1.get_next() == None and n == 1:
        return head.get_data()
    while ref1.get_next() != None:
        if counter >= n:
            ref2 = ref2.get_next()
        ref1 = ref1.get_next()
        counter +=1
    if counter >= n:
        return ref2.get_data()
    else:
        raise Exception('n greater than length of linked list')


if __name__ == '__main__':
    ll = LinkedList()
    for i in range(10):
        ll.insert_at_begenning(i)
    n = 4
    ans = n_th_element_from_end(ll.head, n)
    actual_answer = ll.get_data_at_pos(ll.get_len() - n)
    if ans == actual_answer:
        print("========Passed===========")
    else:
        print(ll.display_list())
        print('Actual anser: ' + str(actual_answer))
        print('Your answer: '+str(ans))