#!/usr/bin/env python3

"""
Q: Implement Stack usign Queues.



=================================
Soln: We can use 2 queues, 1 to store the data when pushing, and another to temporarily 
holding the datas as we dequeue them out of the 1st queue to get the tail item(tail item 
is the top of the stack) and then we can use the temporary qeueue as the primary and the 
primary queue which is now empty as the secondary temporary queue.
"""


from linked_list_queue import LinkedListQueue
from typing import Generic
from typing import TypeVar
from stack import Stack

T = TypeVar('T')

class QueueStack(Stack, Generic[T]):

    def __init__(self):
        self.primary_q = LinkedListQueue[T]()
        self.secondary_q = LinkedListQueue[T]()
    
    def __len__(self):
        return len(self.primary_q)

    def is_empty(self):
        return self.primary_q.is_empty()

    def push(self, data:T):
        self.primary_q.enqueue(data)
    
    def pop(self) -> T:
        while len(self.primary_q) != 1:
            self.secondary_q.enqueue(self.primary_q.dequeue())
        var = self.primary_q.dequeue()
        temp_q = self.primary_q
        self.primary_q = self.secondary_q
        self.secondary_q = temp_q
        return var
    
    def top(self) -> T:
        val = self.pop()
        self.push(val)
        return val

if __name__ == "__main__":
    s = QueueStack[int]()
    for i in range(10):
        s.push(i)
    if s.top() != 9:
        raise Exception('Issue in implementation')
    for i in range(5):
        s.pop()
    if s.top() != 4:
        raise Exception('Issue in implementation')
    for i in range(5):
        s.pop()
    if s.is_empty() is not True:
        raise Exception('Issue in implementation')

    print('============Passed======================') 
