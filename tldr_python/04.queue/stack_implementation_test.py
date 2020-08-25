#!/usr/bin/env python3

"""
Test for Linked List Queue implementation
"""

import unittest
from stack_queue import StackQueue

class TestStackQueue(unittest.TestCase):
    def setUp(self):
        self.q = StackQueue[int]()
    
    def test_linkq_len0(self):
        self.assertTrue(self.q.is_empty(), 'Queue should be empty if no number is given as input')

    def test_enque(self):
        for i in range(100):
            self.q.enqueue(i)
        self.assertEqual(len(self.q), 100, 'Enqued 100 integers but the length is not 100')

    def test_dequeue(self):
        for i in range(100):
            self.q.enqueue(i)
        for i in range(50):
            l = self.q.dequeue()
            self.assertEqual(l, i, 'Dequeued number dont match \n Expected {} but found {}'.format(i, l))
        
    def test_dequeue_empty(self):
        for i in range(100):
            self.q.enqueue(i)
        for i in range(50):
            l = self.q.dequeue()
        for i in range(50):
            l = self.q.dequeue()
            self.assertEqual(l, 50+i, 'Dequeued number dont match\n Expected {} but found {}'.format(50+i, l))
        self.assertTrue(self.q.is_empty(), 'Queue not empty after thoroughly dequeuing')
        deq = self.q.dequeue()
        self.assertIsNone(deq, 'Queue didnt returned None when dequeued when empty\n Expected None type object but found {}'.format(type(deq)))


if __name__ == "__main__":
    unittest.main()