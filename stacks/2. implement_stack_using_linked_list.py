# Stack is a data structure which is helpful to manipulate or operate on the last element which was added
# In Python, Stack is implemented with the help of list. Here, we implement with the help of linked list
# In Stack, Last element which was added; is the first element which can be removed.

# Concepts

# Create a Stack class with some constant length and same values
# Keep the total number of elements , last_index used in the Stack
# Push the new element to the next available index
# Remove the element from the last index

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class StackLinkedList:
    def __init__(self, head = None):
        self.head = head
        self.number_of_elements = 0
        
    def push(self, data):
        #The element which we push last will be the first we will remove
        # Head is here considered as the top of the stack
        # In this case, we dont need to traverse till tail for pusing a new element/value
        if self.head is None:
            self.head = Node(data)
            return
        current_node = self.head
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        number_of_elements += 1
        return
    def size(self):
        return self.number_of_elements

    def is_empty(self):
        return self.number_of_elements == 0
    
    def pop(self):
        if self.is_empty():
            return None
        
        node_to_pop = self.head
        self.head = self.head.next
        self.number_of_elements -= 1
        return node_to_pop
        