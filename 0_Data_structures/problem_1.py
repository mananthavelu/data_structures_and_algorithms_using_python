# LRU is a criteria used for evicting an element when a cache is full

# Set up a DoublyLinkedList Node
class DNode:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None
        
# Set up a DoublyLinkedList
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Insert a node at the beginning of a linked list
    def add_node(self, DoublyLLNode):
        # If the Doubly Linked List is empty, add a new node as head
        if self.head is None:
            self.head = DoublyLLNode
            self.tail = self.head
        else:
        # We add in front of the DoublyLinkedList
            DoublyLLNode.next = self.head
            self.head.previous = DoublyLLNode
            self.head = DoublyLLNode
    
    # Remove a node (in any place; it takes constant time)
    # Appropriately assigning the 'next' and ' previous' pointers helps to make the 'removal'  in constant time.
    def remove_node(self, DoublyLLNode):
        if DoublyLLNode.previous is None and DoublyLLNode.next is None:
            self.head = None
            self.tail = None
        # If the node to remove is head; set it to None for both head and tail of linked list
        elif self.head  == DoublyLLNode:
            DoublyLLNode.next = None
            self.head = DoublyLLNode.next
        # If the node to remove is tail; set it to tail
        elif self.tail == DoublyLLNode:
            self.tail.previous.next = None
            self.tail = DoublyLLNode.previous
        # If the node to remove is not head or tail
        else:
            DoublyLLNode.previous.next = DoublyLLNode.next
            DoublyLLNode.next.previous = DoublyLLNode.previous
        return

# Update the LRU Cache
class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.hash_map = {}
        self.doubly_linked_list = DoublyLinkedList()

    def get(self, key):
        if key in self.hash_map.keys():
            node = self.hash_map[key]
            self.doubly_linked_list.remove_node(node)
            self.doubly_linked_list.add_node(node)
            return node.value
        else:
            return -1

    def set(self, key, value):
        if self.capacity > 0:
            if len(self.hash_map) < self.capacity:
                self.hash_map[key] = DNode(key, value)
                self.doubly_linked_list.add_node(self.hash_map[key])
            else:
                # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
                # Remove the node which is least recently used
                least_used_node = self.doubly_linked_list.tail
                # Remove this node key in doubly linked list and from hash
                self.hash_map.pop(least_used_node.key)
                # Remove this node from the Doubly linked list
                self.doubly_linked_list.remove_node(least_used_node)
                
                self.hash_map[key] = DNode(key, value)
                self.doubly_linked_list.add_node(self.hash_map[key])

our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)

print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2

print(our_cache.get(9))      # returns -1 because 9 is not present in the cache
our_cache.set(5, 5) 
our_cache.set(6, 6)
our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
print(our_cache.get(11) == -1)#returns True
# Test Case 2
print(our_cache.get(4) == 4)#returns True
# Test Case 3
print(our_cache.get(5) == 5)#returns True