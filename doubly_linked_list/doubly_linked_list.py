"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value
    
    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next


"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        # wrap the iput in a node
        new_node = ListNode(value)
        self.length += 1
        # check if the list is empty
        if not self.head and not self.tail:
            # if the list is empty, set both head and tail as new node
            self.head = new_node
            self.tail = new_node
        # we have a non-empty list, add the new node to the head
        else:
            #set the new node's next to refer to current head
            new_node.next =self.head
            #set the current's head'd prv to refer to the new node
            self.head.prev = new_node
            #set the list's head reference to the new node
            self.head = new_node
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        if not self.head and not self.tail:
            return None
        # if head has no next, there is a single elemnet in the linked list
        elif not self.head.get_next():
            head = self.head
            self.head = None
            self.tail = None
            return head.value
        value = self.head.value
        self.head = self.head.get_next()
        return value
        
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_node = ListNode(value)
        self.length += 1
        if not self.head and not self.tail:            
            self.head = new_node
            self.tail = new_node
        else:            
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = None

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # if there is no node at all
        if not self.head and not self.tail:
            return None
        
        #elif only one node
        elif not self.tail.prev:
            tail = self.tail
            self.head = None
            self.tail = None
            return tail.get_value()
        #either way, set a variable the represents the vale of the tail    
        value = self.tail.value
        # set the tail to the prev node
        self.tail = self.tail.prev
        # return the value of the tail removed
        return value
        
                    
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # if the node is the head, cant move it anymore
        if node is self.head:
            return
        # assign a variable for value of node
        value = node.value
        # if the node is the tail, use remove from tail method
        if node is self.tail:
            self.remove_from_tail()
        else: 
            self.delete(node)
            # lessen the length
            self.length -=1
        self.add_to_head(value)
    
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        pass

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # If there is no node at all, nothing to delete
        if not self.head and not self.tail:
            return 
        # if there is only one node, after deleting, nothing is left
        if self.head is self.tail:
            self.head = None
            self.tail = None
        # if there is at least one other node, after deleting, the next node becomes the new head
        elif self.head is node:
            self.head = node.next
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
        elif self.tail is node:
            self.tail = node.prev
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
        else:
            if node.prev:
                node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev
        self.length -=1



    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        pass

    def print_list(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


A= DoublyLinkedList()
A.add_to_tail(33)
A.add_to_head(1)
A.add_to_tail(2)
#A.add_to_tail(3)
#A.add_to_tail(4)
#A.add_to_tail(6)
#A.add_to_head(10)
print(A.remove_from_head())
#print(len(A))
#A.print_list()