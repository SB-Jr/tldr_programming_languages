#!/usr/bin/env python3

"""
Interface for Stack
"""

from typing import Generic
from typing import TypeVar
from abc import ABC
from abc import abstractclassmethod

T = TypeVar('T')

class Stack(ABC, Generic[T]):
    
    @abstractclassmethod
    def __init__(self):
        pass

    @abstractclassmethod
    def push(self, data:T):
        pass

    @abstractclassmethod
    def pop(self) -> T:
        pass

    @abstractclassmethod
    def top(self) -> T:
        pass

    @abstractclassmethod
    def is_empty(self) -> bool:
        pass

    @abstractclassmethod
    def __len__(self) -> int:
        pass

