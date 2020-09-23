'''Each node holds a reference to its previous and its next'''
class ListNode:
    def __init__(self, value = None, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

    ''' Wrap the given value in a listnode and insert it after this node. 
    Note that this Node could already have a next nodeit is pointing to.'''
    def insert_after(self,value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next
    
    '''Wrap the given value in a ListNode and insert it before this node.
    Note that this Node could already have a previous node it is pointing to '''
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, self, current_prev)
        if current_prev:
            current_prev.next = self.prev
    
    '''Rearranges this ListNode's previous and next pointers accordingly,
     effectively deleting this ListNode'''
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
    
'''Our DoublyLisnkedList class. It holds references to 
the List's head and tail nodes'''
class DoublyLinkedList:
    def __init__(self, node = None):
        self.head = None
        self.tail = None
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    '''Wraps the given value in a ListNode and inserts it as the new 
    head of the list. Dont forget to handle the old head node's 
    previous pointer accordingly.'''
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length +=1
        if not self.head and not self.tail:
            self.head =new_node
            self.tail = new_node
        else: 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    '''Removes the List's current head node, making the current 
    head's next node the new head of the list. Returns the value 
    of the removed Node. '''
    def remove_fom_head(self):
        value = self.head.value
        self.delete(self.head)
        return value

    '''Wraps the given value ina ListNode and inserts it as 
    a new tail of the list. Dont forget to handle the old tail
    node's next pointer accordingly.'''
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length +=1
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    '''Removes the List's curret tail node, making the current tail node's
    previous node the new tail pf the List. Returns the value of the 
    removed Node.'''
    def remove_from_tail(self):
        value = self.tail.value
        self.delete(self.tail)
        return value
    
    '''Removes the input node from its current spot in the List and 
    inserts it as the new head node of the List.'''
    def move_to_front(self, node):
        if node is self.head:
            return
        value = node.value
        if node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -=1
        self.add_to_head(value)

    '''Removes the input node from its current spot in the List
    and inserts it a the new tail node of the List.'''
    def move_to_end(self, node):
        if node is self.tail:
            return
        value = node.value
        if node is self.head:
            self.remove_fom_head()
            self.add_to_head(value)
        else: 
            node.delete()
            self.length -=1
            self.add_to_tail(value)

    '''Returns the max value in the List. '''
    def get_max(self):
        if not self.head:
            return None
        max_val = self.head.value
        current = self.head
        while current:
            if current.value >max_val:
                max_val = current.value
            current = current.next
        return max_val

    def delete(self, node):
        #self.length -=1
        if not self.head and not self.tail:
            return

        self.length -= 1
        if self.head ==self.tail:
            self.head = None
            self.tail = None
        elif self.head ==node:
            self.head = node.next
            node.delete()
        elif self.tail == node:
            self.tail = node.prev
            node.delete()
        else:
            node.delete()

    
        