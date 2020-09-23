"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
import sys
sys.path.append('singly_linked_list/')
from singly_linked_list import LinkedList, Node

sys.path.append('queue/')

class Queue:
    
    class Node:
        def __init__(self, value = None, next_node = None):
            self.value = value
            self.next_node = next_node

        def get_value(self):
            return self.value

        def get_next(self):
            return self.next_node 

        def set_next(self, new_next):
            self.next_node = new_next

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0

    def enqueue(self, value):
        new = self.Node(value, None)  # enqueue at the back. New tail node, points to None
        if self.is_empty():
            self.head = new
        else: 
            self.tail.next_node = new
        self.tail = new
        self.size +=1

    def dequeue(self):
        if self.is_empty():
            return None
            #raise IsEmptyError("This queue is empty, can't dequeue")
        result = self.head.value
        self.head = self.head.next_node
        self.size -=1

        if self.is_empty():
            self.tail = None
        return result

    def peek(self):
        if self.is_empty():
            return None
            #raise IsEmptyError('Nothing in the queue')
        return self.head.value

q = Queue()
q.enqueue(100)
q.enqueue(101)
q.enqueue(105)
print(q.dequeue())
print(q.peek())