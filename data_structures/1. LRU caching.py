# LRU is a criteria used for evicting an element when a cache is full
# 
class DoublyNode:
    def __init__(self, key = None, value = None):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None
        
class DoublyLinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail
        
    def add_node(self, DoublyLLNode):
        # If the Doubly Linked List is empty, add a new node as head
        if self.head is None:
            self.head = DoublyLLNode
            self.tail = self.Head

        # We add in front of the DoublyLinkedList
        DoublyLLNode.next = self.head
        self.head.previous = DoublyLLNode
        self.head = DoublyLLNode
        return

    def remove_node(self, DoublyLLNode):
        # If the node to remove is head; set it to None for both head and tail of linked list
        if self.head == DoublyLLNode:
            self.head = None
            self.tail = None
    
        # If the node to remove is tail; set it to tail
        elif self.tail == DoublyLLNode:
            self.tail.prev.next = None
            self.tail = DoublyLLNode.previous

        # If the node to remove is not head or tail
        else:
            DoublyLLNode.prev.next = DoublyLLNode.next
            DoublyLLNode.next.previous = DoublyLLNode.previous
        return

    def print_linked_list(self):
        node = self.head
        while node:
            print(f"key is {node.key}, value is {node.value}")
            node = node.next
        return

doubly_linked_list_ex = DoublyLinkedList(1, "One")
print(doubly_linked_list_ex.print_linked_list())
doubly_linked_list_ex.add_node(2, "Two")


print(type(DoublyNode_one))
print(type(DoublyNode_two))
print(type(doubly_linked_list_ex))
print(doubly_linked_list_ex.print_linked_list())


class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.hash_map = {}
        self.doubly_linked_list = DoublyLinkedList()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        pass

    def set(self, key, value):
        if self.capacity > 0 and len(self.hash_map) < self.capacity:
            self.hash_map[key] = DoublyNode(key, value)
            self.doubly_linked_list.add_node(DoublyNode(key, value))
        else:
            least_used_node = self.doubly_linked_list.tail
            # Remove this node in doubly linked list and from hash
            self.hash_map.pop(least_used_node.key)
            
            key_least_used_node = least_used_node.key
            
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        pass
    
    def get_bucket_index(self, key):
        return self.get_hash_code(key)
    
    def get_hash_code(self, key):
        key = str(key)
        current_co_efficient = 1
        hash_code = 0
        num_buckets = len(self.bucket_array)
        for character in key:
            hash_code += ord(character) * current_co_efficient
            hash_code = hash_code % num_buckets
            current_co_efficient  *= self.p
            current_co_efficient = current_co_efficient % num_buckets
        return hash_code % num_buckets
    

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1

# Test Case 2

# Test Case 3
