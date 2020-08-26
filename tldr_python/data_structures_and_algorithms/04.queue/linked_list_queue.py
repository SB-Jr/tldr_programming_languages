#!/usr/bin/env python3

"""
Linked List implementation of Queue
"""

from queue import Queue
from typing import Generic
from typing import TypeVar
from linked_list import LinkedList

T = TypeVar('T')

class LinkedListQueue(Queue, Generic[T]):
    def __init__(self):
        self.list = LinkedList[T]()
        self.tail = self.list.head
    
    def enqueue(self, data):
        if self.tail is None:
            self.list.insert_at_begenning(data)
            self.tail = self.list.head
        else:
            self.tail = self.list.insert_at_pos(data, self.tail)
    
    def dequeue(self) -> T:
        if self.list.head is not None:
            val = self.list.delete_at_begenning()
            if self.list.head is None:
                self.tail = None
            return val
        return None

    def __len__(self):
        return self.list.len
    
    def is_empty(self):
        if self.list.head is None:
            return True
        else:
            return False

    def top_data(self) -> T:
        if self.list.head == None:
            return None
        return self.list.head.get_data()