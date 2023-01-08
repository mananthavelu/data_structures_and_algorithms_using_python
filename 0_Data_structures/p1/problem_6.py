class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def search_v(self, value):
        if value == self.head.value:
            return True

        node = self.head
        while node:
            if value == node.value:
                return True
            node = node.next
        return False

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    results = set()
    head_llist_1 = llist_1.head
    head_llist_2 = llist_2.head
    while head_llist_1:
        value_to_add = head_llist_1.value
        if value_to_add not in results:
            results.add(value_to_add)
        head_llist_1 = head_llist_1.next

    while head_llist_2:
        value_to_add = head_llist_2.value
        if value_to_add not in results:
            results.add(value_to_add)
        head_llist_2 = head_llist_2.next

    return list(results)

def intersection(llist_1, llist_2):
    results = set()
    head_llist_1 = llist_1.head
    head_llist_2 = llist_2.head

    while head_llist_1:
        if llist_1.search_v(head_llist_1.value) and llist_2.search_v(head_llist_1.value):
            results.add(head_llist_1.value)
        head_llist_1 = head_llist_1.next

    return list(results)
    

# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))#returns [3, 2, 4, 35, 6, 65, 21, 32, 9, 1, 11]
print (intersection(linked_list_1,linked_list_2))#[4, 21, 6]

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))#returns [3, 2, 4, 35, 6, 65, 23, 1, 7, 8, 9, 11, 21]
print (intersection(linked_list_3,linked_list_4))#returns []

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 3

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2]
element_2 = [6,3]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))#returns [3, 2, 6]
print (intersection(linked_list_1,linked_list_2))# returns [3]

# Test Case 4
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = [11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))#returns [11, 21, 1]
print (intersection(linked_list_1,linked_list_2))#returns []

# Test Case 5
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))#returns []
print (intersection(linked_list_1,linked_list_2))#returns []