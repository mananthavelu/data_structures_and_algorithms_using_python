# What we need: a Hash function which converts the given input to a certain value (hash code) which will act as an array index
# Simple hash map implementation


class HashMap():
    def __init__(self, initial_size = 10):
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
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 37
        self.num_entries = 0
        
    def put(self, key, value):
        # Key is string
        pass
    
    def get(self, key, value):
        pass
    
    def get_bucket_index(self, key):
        return self.get_has_code(key)
    
    def get_hash_code(self, key):