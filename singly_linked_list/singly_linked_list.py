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


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_tail(self, value):
        new_node = Node(value, None)
        #check if there is no head
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node

    def remove_head(self):
        # Is there a head?
        if not self.head:
            return None

        # if head has no next, there is a single elemnet in the linked list
        if not self.head.get_next():
            head = self.head
            self.head= None
            self.tail = None

            return head.get_value()
        
        value = self.head.get_value()
        # set the head reference to the current head's next node in the list
        self.head = self.head.get_next()
        return value

    def contains(self, value):
        if not self.head:
            return False
        
        # get a reference to the node we're currrentlt at ; update this as we traverse the link
        current = self.head
        #check to see if we are at a valid node
        while current:
            # return True if the current value we are looking at matches our targe value
            if current.get_value() ==value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

A = LinkedList()

