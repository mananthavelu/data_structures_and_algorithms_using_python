# Goal: Find if a linked list has a loop i.e an element in the linked list pointing to 
# any of it's previously visited 


# Concept: Use two pointers starting from its head
# One pointer - will move in each iteration by one element to its next
# Second pointer - will move in each iteration by two elements to its next
# As these two pointers in different pace, at one point they will both meet, if a loop is present

class SinglyLinkedListNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = Node(head)
        
    def add_node(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            print("Linked List was empty. New node was added as its head")
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(new_data)
        return


def isCircular(linked_list):
    if linked_list.head is None:
        return False
    
    # Initializing two pointers
    
    slow_mover = linked_list.head
    fast_mover = linked_list.head
    
    while fast_mover and fast_mover.next:
        slow_mover = slow_mover.next
        fast_mover = fast_mover.next.next
        if slow_mover == fast_mover:
            return True
    return False