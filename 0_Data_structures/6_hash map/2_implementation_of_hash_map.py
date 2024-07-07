# What we need: a Hash function which converts the given input to a certain value (hash code) which will act as an array index
# Simple hash map implementation

class HashMap():
    def __init__(self, initial_size = 5):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 37
        self.num_entries = 0
        
# Explanations
"""
# The implementation of hash map is done using an array here
# We will initialize an array with a size
# self.p is the coefficient used in hash function - This is constant across all instances of hash function
# self.num_entries is initialized with each instance
"""
class HashMap():
    def __init__(self, initial_size = 10):
        self.bucket_array = [[] for _ in range(initial_size)]
        self.p = 31
        self.num_entries = 0
        
    def put(self, key, value):
        index_for_value = self.get_hash_code(key) % 10
        bucket = self.bucket_array[index_for_value]
        print(f"adding {key}, at index {index_for_value} with {value}")
        for i, (k,v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return
        bucket.append((key, value))
        self.num_entries += 1
    
    def get(self, key, value):
        bucket = self.bucket_array[self.get_hash_code(key)]
        for k, v in bucket:
            if k == key:
                return v

    def get_bucket_index(self, key):
        return self.get_hash_code(key)
    
    def get_hash_code(self, key):
        key = str(key)
        current_co_efficient = 1
        hash_code = 0
        for character in key:
            value = ord(character)
            hash_code += value * current_co_efficient
            current_co_efficient  *= self.p
        return hash_code

    def __repr__(self):
        return str(self.bucket_array)

grocery_costs = HashMap()
grocery_costs.put('tomatos', 4)
grocery_costs.put('Brocolli', 7)
grocery_costs.put('Carrots', 3)
grocery_costs.put('tomat', 4)
grocery_costs.put('Brocli', 7)
grocery_costs.put('Carts', 3)
print(grocery_costs)


