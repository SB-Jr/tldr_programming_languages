#!/usr/bin/env python3

"""
Implement Queue using 2 Stacks
"""

from queue import Queue
from linked_list_stack import LinkeListStack
from typing import Generic
from typing import TypeVar

T = TypeVar('T')

class StackQueue(Queue, Generic[T]):
    def __init__(self):
        self.primary_stack = LinkeListStack[T]()
        self.secondary_stack = LinkeListStack[T]()

    def enqueue(self, data):
        self.primary_stack.push(data)
    
    def dequeue(self) -> T:
        if self.primary_stack.is_empty():
            return None
        while not self.primary_stack.is_empty():
            self.secondary_stack.push(self.primary_stack.pop())
        var = self.secondary_stack.pop()
        while not self.secondary_stack.is_empty():
            self.primary_stack.push(self.secondary_stack.pop())
        
        return var

    def __len__(self):
        return len(self.primary_stack) + len(self.secondary_stack)

    def is_empty(self):
        return self.primary_stack.is_empty()
    
    def top_data(self) -> T:
        if self.primary_stack.is_empty():
            return None
        while not self.primary_stack.is_empty():
            self.secondary_stack.push(self.primary_stack.pop())
        var = self.secondary_stack.top()
        while not self.secondary_stack.is_empty():
            self.primary_stack.push(self.secondary_stack.pop())
        return var