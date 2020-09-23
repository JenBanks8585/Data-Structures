"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
import sys
sys.path.append('singly_linked_list/')
from singly_linked_list import LinkedList, Node


class IsEmptyError(Exception):
    pass

class Stack:
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
        self.storage = LinkedList()
        self.head = None

    def __len__(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0

    def push(self, value):
        self.head = self.Node(value, self.head)
        self.size +=1

    def pop(self):
        if self.is_empty():
            return None
            # IsEmptyError(" Sorry no element here, nothing to pop")
        result = self.head.value
        self.head = self.head.next_node
        self.size -=1
        return result

    def peek(self):
        if self.is_empty():
            return None
            #raise IsEmptyError('Nothing to peek')
        return self.head
        

#stack =Stack()
#stack.push(2)
#stack.push(70)
#stack.push(4)
#stack.pop()
#print(len(stack))
#print(stack.peek())

