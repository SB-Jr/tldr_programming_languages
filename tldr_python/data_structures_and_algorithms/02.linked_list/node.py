#!/usr/bin/env python3
# Node for linked list

from typing import Generic
from typing import TypeVar
from typing import Optional

T = TypeVar('T')

class Node(Generic[T]):
    # constructor
    def __init__(self, data:Optional[T]=None, next:Optional['Node']=None):
        self.data = data if data != None else None
        self.next = next

    # getters and setters
    def set_data(self, data:T):
        self.data = data
    
    def get_data(self) -> T:
        return self.data

    def set_next(self, next:'Node'):
        self.next = next

    def get_next(self) -> 'Node':
        return self.next
    
    def has_next(self) -> bool:
        return self.next != None