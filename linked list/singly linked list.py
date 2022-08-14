# Implementation of a Singly Linked List

# Linkedlist has a node
# Node stores the data we want to store
# Each node has its link to its 'next' node
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
# Linked list has head and tail initialized to 'None'
class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = Node(head)
        
    def add_node(self, node_data):
        if self.head is None:
            self.head = Node(node_data)
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            
        current_node.next = Node(node_data)
        print("New node added")
        return
        
    def print_linked_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        return
            
node_1 = 1 
node_2 = 2
linked_list_example = SinglyLinkedList(node_1)
linked_list_example.add_node(node_2)
print("Here")
linked_list_example.print_linked_list()

#mari.ananth22