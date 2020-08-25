#!/usr/bin/env python3

"""
A curcular list implementation for Queues
"""

from queue import Queue
from typing import Generic
from typing import TypeVar

T = TypeVar('T')

class CircularListQueue(Queue, Generic[T]):
    def __init__(self, limit:int):
        self.list = [0] * limit
        self.limit = limit
        self.head = 0
        self.tail = 0
        self.len = 0
    
    def enqueue(self, data:T):
        if self.len > self.limit -1:
            raise Exception('Queue full')
        self.list[self.tail] = data
        self.len +=1
        self.tail  = (self.tail + 1) % self.limit

    def dequeue(self) -> T:
        if self.len == 0:
            raise Exception('Queue empty')
        val = self.list[self.head]
        self.len -=1
        self.head = (self.head + 1) % self.limit
        return val        

    def is_empty(self) -> bool:
        return self.len == 0

    def __len__(self) -> int:
        return self.len

    def top_data(self):
        if self.len == 0:
            return None
        return self.list[self.head]