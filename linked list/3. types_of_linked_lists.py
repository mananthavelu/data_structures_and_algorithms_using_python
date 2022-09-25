# Doubly Linked lists

    """
    These linked lists have the elements where for each element the 'next' and 
    'previous' elements are stored.
    """
    
class DoublyNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.previous = None
        
class DoublyLinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        
    def add_node(new_data):
        if self.head is None:
            self.head = DoublyNode(new_data)
            self.tail = self.Head
        
        self.tail.next = DoublyNode(new_data)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return