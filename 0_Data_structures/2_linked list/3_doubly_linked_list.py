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
        
    def append(self, data):
        if self.head is None:
            self.head = DoublyNode(data)
            self.tail = self.head
            return
        
        self.tail.next = DoublyNode(data)
        self.tail.next.previous = self.tail
        self.tail = self.tail.next
        return

    def append_at_position(self, data, position):
        if position == 1:
            self.head = DoublyNode(data)
            self.tail = self.head
            return
        current_position = 1
        current_node = self.head
        new_node = DoublyNode(data)
        while current_node:
            if (current_position + 1) == position:
                new_node.next = current_node.next
                current_node.next.previous = new_node
                current_node.next = new_node
                new_node.previous = current_node
            current_node = current_node.next
            current_position += 1
        return

    def delete_element_at_position(self, position):
        if position == 1:
            self.head = None
            self.tail = None
            return
        current_position = 1
        current_node = self.head
        while current_node:
            if (current_position + 1) == position:
                current_node.next.next.previous == current_node
                current_node.next =current_node.next.next
                return
            current_node = current_node.next
            current_position += 1

    def __repr__(self):
        result = ""
        current_node = self.head
        while current_node:
            result += current_node.data
            result += "->"
            current_node = current_node.next
        return result[:-2]

new_dd_list = DoublyLinkedList()
new_dd_list.append("C1")
new_dd_list.append("C2")
new_dd_list.append("C3")
new_dd_list.append("C4")
new_dd_list.append("C5")
new_dd_list.append_at_position("C3A", 2)
print(new_dd_list)
new_dd_list.delete_element_at_position(4)
print(new_dd_list)