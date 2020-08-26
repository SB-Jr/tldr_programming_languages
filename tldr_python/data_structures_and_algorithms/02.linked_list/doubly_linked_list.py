#!/usr/bin/env python3

# Doubly linked list class

from linked_list import LinkedList
from double_node import DNode
from typing import Generic
from typing import TypeVar

T = TypeVar('T')

class DLinkedList(LinkedList[T]):
    # init handled by Parent Class
    
    #get_len handled by PC
    
    # get_head_node handled by PC
    
    # get_node_at_pos handled by PC

    # get_data_at_pos HBPC

    # insert_at_begening HBPC

    def insert_at_pos(self, data:T, pos:int):
        if pos < 0 or pos > self.len:
            raise Exception('Invalid position')
        if pos == 0:
            self.insert_at_begenning(data)
        cur_node = self.head
        for _ in range(pos):
            cur_node = cur_node.get_next()
        prev_node = cur_node.get_prev()
        node = DNode(data, prev_node, cur_node)
        self.len += 1

    def insert_at_end(self, data:T):
        self.insert_at_pos(data, self.len-1)

    def delete_at_begning(self) -> T:
        if self.head == None:
            raise Exception('Doubly Linked List already empty')
        head_next = self.head.get_next()
        val = head_next.get_data()
        head_next.set_prev(None)
        self.head = head_next
        return val

    def delete_at_pos(self, pos) -> T:
        node_pos = self.get_node_at_pos(pos)
        node_prev = node_pos.get_prev()
        node_next = node_pos.get_next()
        val = node_pos.get_data()
        node_next.set_prev(node_prev)
        node_prev.set_next(node_next)
        return val

    def delete_at_end(self) -> T:
        self.delete_at_pos(self.len-1)

    # display HBPC

    # clear HBPC