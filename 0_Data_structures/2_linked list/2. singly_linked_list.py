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
    def add_node(self, node_data):
        if self.head is None:
            self.head = Node(node_data)
            print("Head is added")
            #return
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = Node(node_data)
            print("New node added")
            #return
    
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

# Test
node_1 = 1
node_2 = 2
node_3 = 3
node_4 = 4
ll1 = SinglyLinkedList(node_1)
ll1.add_node(node_2)
ll1.add_node(node_3)
ll1.add_node(node_4)
ll1.print_linked_list()
print(ll1.to_list())
print(ll1)
print("pass" if (ll1.head.data == 1) else "fail")