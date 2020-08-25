#!/usr/bin/env python3

# Linked list

from typing import TypeVar
from typing import Generic
from typing import Optional
from node import Node
from typing import overload

T = TypeVar('T')

class LinkedList(Generic[T]):
    # Constructor
    def __init__(self, data:T=None):
        if data == None:
            self.head = None
            self.len = 0
        else:
            self.insert_at_begenning(data)

    def get_len(self) -> int:
        return self.len

    def get_head_node(self) -> Node:
        return self.head()

    def get_node_at_pos(self, pos:int) -> Node:
        if pos >= self.len:
            raise Exception('Invalid Position: It is greater than the length of the Linked List')
        else:
            if self.len == 0:
                raise Exception('Linked List is empty')
            if pos == 0:
                return self.head
            else:
                cur_node = self.head
                for _ in range(pos):
                    cur_node = cur_node.get_next()
                return cur_node

    def get_data_at_pos(self, pos:int) -> T:
            if pos == None or pos > self.len or self.len == 0:
                raise Exception('Position is greater than the length of Linked List')
            if pos == 0:
                return self.head.get_data()
            else:
                return self.get_node_at_pos(pos).get_data()

    def insert_at_end(self, data:T) -> Node:
        return self.insert_at_pos(data, self.len-1, True)
        
    def insert_at_begenning(self, data:T):
        self.insert_at_pos(data, 0)

    def insert_at_pos(self, data:T, pos:[int, Node], at_end:bool = False) -> Node:
        if type(pos) == int:
            return self.__insert_at_pos_index(data, pos, at_end)
        elif type(pos) == Node:
            return self.__insert_at_pos_node(data, pos)
        else:
            raise Exception('Invalid type of position argument passed')


    def __insert_at_pos_node(self, data:T, node:Node) -> Node:
        if node is None:
            raise Exception('Invalid Node')
        if data is None:
            raise Exception('Invalid Data')
        node_new = Node(data)
        node_next = node.get_next()
        node.set_next(node_new)
        node_new.set_next(node_next)
        self.len +=1
        return node_new

    def __insert_at_pos_index(self, data:T, pos:int, at_end = False) -> Node:
        if data == None:
            raise Exception('Invalid Data')
        if pos != 0 and (pos >= self.len or pos < 0):
            raise Exception('Invalid position mentioned')
        node = Node(data, self.head)
        if at_end:
            pos = pos + 1
        if pos == 0:
            node.set_next(self.head)
            self.head = node
        else:
            node_pos_prev = self.get_node_at_pos(pos-1)
            node_pos = node_pos_prev.get_next()
            node_pos_prev.set_next(node)
            node.set_next(node_pos)
        self.len += 1
        return node

    def delete_at_begenning(self) -> T:
        val = self.delete_at_pos(0)
        return val

    def delete_at_pos(self, pos) -> T:
        if self.len == 0 or pos < 0 or (self.len != 0 and pos >= self.len):
            raise Exception('Invalid position')
        if pos == 0:
            val = self.head.get_data()
            self.head = self.head.get_next()
        else:
            node_prev = self.get_node_at_pos(pos-1)
            node_pos = node_prev.get_next()
            val = node_pos.get_data()
            node_next = node_pos.get_next()
            node_prev.set_next(node_next)
        self.len -=1
        return val

    def delete_at_end(self) -> T:
        val  = self.delete_at_pos(self.len-1)
        return val

    def display_list(self) -> str:
        if len == 0:
            return "List Empty"
        cur_node = self.head
        ret_str = '[H]'
        while cur_node != None:
            ret_str = ret_str +'->' +  str(cur_node.get_data())
            cur_node = cur_node.get_next()
        return ret_str

    def clear(self):
        self.head = None
        self.len = 0

