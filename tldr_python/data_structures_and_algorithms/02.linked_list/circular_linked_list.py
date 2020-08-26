#~/usr/bin/env python3

# Circular Linked List

from typing import Generic
from typing import TypeVar
from linked_list import LinkedList

T = TypeVar('T')

class CLinkedList(LinkedList[T]):
    def __init__(self, data):
        super.__init__(data)
        if data != None:
            self.head.set_next(self.head)
    
    # get_len in parent
    # get head_node in parent
    # get_node_at_pos in parent
    # get_data_at_pos in parent
    # insert_at_end in parent
    # insert_at_begenning in parent
    def insert_at_pos(self, data:T, pos):
        super.insert_at_pos(self, data, pos)
        if pos == 0 or pos == self.len -2:
            #previously the pos for tail was len-1 but after insert it is len-2
            tail = self.get_node_at_pos(self.len-1)
            tail.set_next(self.head)

    # delete_at_begenning in parent
    # delete_at_end in parent
    def delete_at_pos(self, pos) -> T:
        super.delete_at_pos(pos)
        if pos == 0:
            tail = self.get_node_at_pos(self.len-1)
            tail.set_next(self.head)

    def display(self) -> str:
        ret_str = super.display()
        ret_str = ret_str + '->[H]'
        return ret_str
    
    def clear(self):
        tail = self.get_node_at_pos(self.len-1)
        tail.set_next(None)
        super.clear()
