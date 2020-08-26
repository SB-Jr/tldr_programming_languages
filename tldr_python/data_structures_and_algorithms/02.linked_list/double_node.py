#!/usr/bin/env python3

# Class for doubly linked list

from typing import Generic
from typing import TypeVar
from node import Node

T = TypeVar('T')

class DNode(Node[T]):
    def __init__(self, data:T, prev_node:DNode = None, next_node:DNode=None):
        super.__init__(data, next_node)
        self.prev = prev_node
        if prev_node != None:
            prev_node.set_next(self)
    
    def set_prev(self, prev_node:DNode):
        self.prev = prev_node

    def get_prev(self) -> DNode:
        return self.prev

    def has_prev(self) -> bool:
        return self.get_prev() != None