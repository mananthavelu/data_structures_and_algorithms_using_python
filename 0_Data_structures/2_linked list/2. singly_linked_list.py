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

    # Remove a head node
    def remove_head(self):
        current_node = self.head
        self.head = current_node.next
        return

    # Remove a node from a particular position
    def remove_node_at_position(self, position):
        if position == 1:
            return self.remove_head
        current_node = self.head
        current_position = 2
        while current_node is not None:
            if current_position == position:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
            current_position += 1
        

    # print linked list
    def print_linked_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next
        return

    # Search for a node data
    def search(self, input):
        if self.head.data == input:
            return True
        current_node = self.head
        while current_node is not None:
            if current_node.data == input:
                return True
            current_node = current_node.next
        return False
    # Reverse a linked list
    def reverse_linked_list(self):
        # Keep the None as the self.heads next
        # 
        node_to_point_to = None
        current_node = self.head
        while True:
            current_node.next = node_to_point_to
            node_to_point_to = current_node
            current_node = current_node.next
        self.head = node_to_point_to
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
linked_list_one.prepend(node_5)
linked_list_one.add_node_at_position(17, 1)
linked_list_one.remove_head()
print(linked_list_one)# Head node is given an entry point
linked_list_one.remove_node_at_position(2)
print(linked_list_one)# Head node is given an entry point
print(linked_list_one.search(2))
linked_list_one.reverse_linked_list()
print(linked_list_one)
# TODO Search for a value,pop a value, Size of a linked list