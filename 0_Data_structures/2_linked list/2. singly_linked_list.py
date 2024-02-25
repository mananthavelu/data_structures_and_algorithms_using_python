# Implementation of a Singly Linked List

# Linkedlist has a node
# Node stores the data we want to store
# Each node has its link to its 'next' node, thus creating a sequence with links ('link'ed 'list')
class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self, head = None):
        self.head = head

    def is_empty(self):
        return self.head is None

    def append(self, data):
        # Add as a head if it does not exist
        if self.head is None:
            self.head = Node(data)
            return            
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = Node(data)                                                                                                                                                                                                                                                                                                                      
        return
    
    def size(self):
        if self.is_empty():
            return 0
        current_node = self.head
        current_size = 0
        while current_node:
            current_size += 1
            current_node = current_node.next
        return current_size
    
    def convert_list_to_ll(self, input_list):
        if self.head is None:
            self.head = Node(input_list[0])
            current_node = self.head
            for element in input_list[1:]:
                current_node.next = Node(element)
                current_node = current_node.next
        else:
            current_node = self.return_end_node()
            for element in input_list:
                current_node.next = Node(element)
                current_node = current_node.next
        return

    def return_end_node(self):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        return current_node

    def prepend(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        #current_node = self.head
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"prepended {new_node.data} and the head is {self.head.data}")
        return

    def reverse_linked_list(self):
        current_node = self.head
        print(current_node.data)
        reversed_linked_list = SinglyLinkedList()
        reversed_linked_list.append(current_node.data)
        print(f"Here I am {reversed_linked_list}")
        while current_node.next:
            node_to_prepend = current_node.next
            reversed_linked_list.prepend(node_to_prepend.data)
            current_node = current_node.next
        return reversed_linked_list

    def add_node_at_position(self, data, position):
        if position == 1:
            self.prepend(data)
            return
        current_position = 1
        current_node = self.head
        new_node = Node(data)
        while current_node:
            if (current_position + 1) == position:
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_position += 1
            current_node = current_node.next
        return
    
    def remove_head(self):
        if self.head is None:
            return
        head_to_be_node = self.head.next
        self.head = head_to_be_node
        return

    def remove_a_node_with_value(self, data):
        if self.head.data == data:
            self.remove_head()
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def __repr__(self):
        result_string = ''
        current_node = self.head
        while current_node:
            result_string += current_node.data
            result_string += '->'
            current_node = current_node.next
        return result_string[:-2]

example_ll = SinglyLinkedList()
example_ll.convert_list_to_ll(['Germany',"Austria","Belgium","Netherlands"])
print(example_ll)
example_ll.add_node_at_position('Switzerland', 1)
print(example_ll)
example_ll.remove_a_node_with_value('Netherlands')
print(example_ll)
#print("Here")
#example_ll.reverse_linked_list()
#print(f"Reversed list is {reversed_list}")

class NodeHeadTail:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class SinglyLinkedListHeadTail:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail

    def __repr__(self):
        result = ""
        current_node = self.head
        while current_node.next:
            result += current_node.data
            result += "->"
            current_node = current_node.next
        return result[:-2]

    def append(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head

        new_node = Node(data)
        self.tail.next = new_node
        self.tail = self.tail.next
        
new_ss_list = SinglyLinkedListHeadTail()
new_ss_list.append("C1")
new_ss_list.append("C2")
new_ss_list.append("C3")
new_ss_list.append("C4")
print(f"The new ss list is: {new_ss_list}")

"""
new_node = Node('Switezerland')
new_linked_list = SinglyLinkedList(new_node)
print(new_linked_list.size())
new_linked_list.append('Zurich')    
print(new_linked_list.size())
print(new_linked_list.is_empty())
print(new_linked_list)
new_linked_list.convert_list_to_ll(['Germany',"Austria"])
print(new_linked_list)       


class Node:
    def __init__(self, data = None):
        #Constructor for the class

        #Args:
        #    data (_type_, optional): Content of the Node. Defaults to None.
        
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
print(linked_list_one.head.data)
print(linked_list_one.to_list())
"""