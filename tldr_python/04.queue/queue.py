#!/usr/bin/env python3

"""
Queue ADT
"""

from abc import ABC
from abc import abstractclassmethod
from typing import TypeVar
from typing import Generic

T = TypeVar('T')

class Queue(ABC, Generic[T]):
    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def enqueue(self, data:T):
        pass

    @abstractclassmethod
    def dequeue(self) -> T:
        pass

    @abstractclassmethod
    def __len__(self):
        pass

    @abstractclassmethod
    def is_empty(self):
        pass

    @abstractclassmethod
    def top_data(self) -> T:
        pass