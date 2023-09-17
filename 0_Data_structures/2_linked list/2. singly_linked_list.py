# Implementation of a Singly Linked List

# Linkedlist has a node
# Node stores the data we want to store
# Each node has its link to its 'next' node, thus creating a sequence with links ('link'ed 'list')

class Node:
    def __init__(self, data = None):
        """Constructor for the class

        Args:
            data (_type_, optional): Content of the Node. Defaults to None.
        """
        self.data = data
        self.next = None
        
# Linked list has head and tail initialized to 'None'
class SinglyLinkedList:
    # Initialization
    def __init__(self, head = None):
        self.head = Node(head)
        print("Head is initialized")
    
    # add new node
    def append(self, node_data):
        if self.head is None:
            self.head = Node(node_data)
            print("Head is added")
            return
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(node_data)
            print("New node added")
            return
    
    # Add a node in a particular position
    def add_node_at_position(self, node_data, position):
        new_node = Node(node_data)
        if self.head is None:
            self.head = new_node
            return
        if position == 1:
            self.prepend(node_data)
            return
        current_position = 2
        current_node = self.head
        while current_node is not None:
            if position == current_position:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_position += 1
            current_node = current_node.next

    # Prepend a node to the linked list
    def prepend(self, node_data):
        new_node = Node(node_data)
        if self.head is None:
            self.head = new_node
            print("Head is added")
            return
        new_node.next = self.head
        self.head = new_node
        

    # print linked list
    def print_linked_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        return

    # convert linked list to list
    def to_list(self):
        result = []
        current_node = self.head
        while current_node:
            result.append(current_node.data)
            current_node = current_node.next
        return result
    
    def is_empty(self):
        return self.head is None

    # print the linked list with values
    def __repr__(self):
        if self.is_empty():
            return "[]"
        res = "["
        p = self.head
        while p is not None:
            res += repr(p.data)
            if p.next is not None:
                res += " -> "
            p = p.next
        res += "-> None]"
        return res

# Test case
node_1 = 1
node_2 = 2
node_3 = 3
node_4 = 4
node_5 = 10
linked_list_one = SinglyLinkedList(node_1)
linked_list_one.append(node_2)
linked_list_one.append(node_3)
linked_list_one.append(node_4)
print("pass" if (linked_list_one.head.data == 1) else "fail")
linked_list_one.prepend(node_5)
linked_list_one.add_node_at_position(17, 1)
linked_list_one.print_linked_list()
print(linked_list_one.to_list())
print(linked_list_one)# Head node is given an entry point
print("pass" if (linked_list_one.head.data == 10) else "fail")

# TODO Add a method to remove an element from the linked list using position, using value