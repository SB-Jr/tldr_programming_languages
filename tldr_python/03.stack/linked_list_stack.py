#!/usr/bin/env python3

"""
Stack implementation using linked list
"""

from stack import Stack
from linked_list import LinkedList
from typing import Generic
from typing import TypeVar

T = TypeVar('T')

class LinkeListStack(Stack[T]):

    def __init__(self):
        self.linked_list = LinkedList[T]()
    
    def push(self, data:T):
        self.linked_list.insert_at_begenning(data)
    
    def pop(self) -> T:
        return self.linked_list.delete_at_begenning()

    def top(self) -> T:
        return self.linked_list.head.get_data()

    def is_empty(self) -> bool:
        return True if  self.linked_list.head == None else False

    def __len__(self):
        return self.linked_list.get_len()