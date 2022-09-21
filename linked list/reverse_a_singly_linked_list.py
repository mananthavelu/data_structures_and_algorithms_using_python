class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
        
class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = Node(head)
        
    def add_node(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(new_data)
        return
    def print_linked_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        return
# Example
singly_linked_list_eg = SinglyLinkedList(1)
singly_linked_list_eg.add_node(2)
singly_linked_list_eg.add_node(3)
singly_linked_list_eg.print_linked_list()

def reverse(linkedlist):
    new_list = SinglyLinkedList()
    current_end = None
    for value in linkedlist:
        new_node = Node(value)
        new_node.next = current_end
        current_end = new_node
    new_list.head = current_end
    return new_list

# Eg
new_list = reverse([1,2,3,4])
new_list.print_linked_list()