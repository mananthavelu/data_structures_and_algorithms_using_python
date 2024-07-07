# Add Compression function
# Why: These hash codes are huge/large numbers and we need to reduce them
# One way to do is; by Mod total number of elements on the results

class LinkedListNode():
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        
class HashMap():
    def __init__(self, initial_size = 10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0
        
    def put(self, key, value):
        # Key is string
        pass
    
    def get(self, key, value):
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
    
    
    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)
        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]
        
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next
            
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1
    
    def get(self, key):
        bucket_index = self.get_bucket_index(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None
    
    def size(self):
        return self.num_entries
    
        # Helper function to see the hashmap
    def __repr__(self):
        output = "\nLet's view the hash map:"

        node = self.bucket_array
        for bucket_index, node in enumerate(self.bucket_array):
            if node is None:
                output += '\n[{}] '.format(bucket_index)
            else:
                output += '\n[{}]'.format(bucket_index)
                while node is not None:
                    output += ' ({} , {}) '.format(node.key, node.value)
                    if node.next is not None:
                        output += ' --> '
                    node = node.next
                    
        return output
# Test the collision resolution technique
hash_map = HashMap()

hash_map.put("one", 1)
hash_map.put("two", 2)
hash_map.put("three", 3)          # Collision: The key "three" will generate the same bucket_index as that of the key "two"
hash_map.put("neo", 11)           # Collision: The key "neo" will generate the same bucket_index as that of the key "one"

print("size: {}".format(hash_map.size()))

print("one: {}".format(hash_map.get("one")))
print("neo: {}".format(hash_map.get("neo")))
print("three: {}".format(hash_map.get("three")))

print(hash_map)                          # call to the helper function to see the hashmap