# Given the random integers one followed by another and so on, create a sorted linked list

# Create a Singly Linked List Node
class SinglyLinkedListNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = head
        
    def create_sorted_linked_list(self, integer_element):
        if self.head is None:
            self.head = Node(integer_element)
            return
        
        if integer_element < self.head.data:
            new_node = Node(integer_element)
            new_node.next = self.head
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next is not None and integer_element <= current_node.next.value:
            current_node = current_node.next
        
        new_node = Node(integer_element)
        new_node.next = current_node.next
        current_node.next = new_node
        return
        