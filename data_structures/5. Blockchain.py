import hashlib
import datetime


class Block():
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None
    
    def get_data(self):
        return self.data
    
    def calc_hash(self):
        sha = hashlib.sha256()
        hash_input = self.data + str(self.timestamp)
        hash_str = hash_input.encode('utf-8')
        sha.update(hash_str)
        return sha.hexdigest()
    
    def get_hash():
        return self.hash()
    
    def __repr__(self):
        return f"data({self.get_data()})"
    
class BlockChain():
    def __init__(self, head = None):
        self.head = head
                    
    def add_a_block(self, timestamp, data):

        if self.head is None:
            self.head = Block(timestamp, data, previous_hash=0)
            return
        
        current_node = self.head
        # We move until the last block
        while current_node.next:
            current_node = current_node.next
        
        hash_of_prev_block = self.head.hash
        new_block = Block(timestamp, data, hash_of_prev_block)
        current_node.next = new_block
        return
    
    def traverse(self):
        current_block = self.head
        while current_block is not None:
            print(f"at {datetime(current_block.timestamp)}, block{current_block.data} is added")
            current_block = current_block.next
        return
    
    def __iter__(self):
        node = self.head
        while node:
            yield node.data
            node = node.next
            
    def __repr__(self):
        return str([block_data for block_data in self])

        
# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values
import time
block_chain = BlockChain()
time_stamp_one = time.time()
data_one = "HelloBlock1"
previous_hash_one = 0
block_chain.add_a_block(time_stamp_one, data_one)
print(f"1 {block_chain}")
# Test Case 1

#block_one = Block(time_stamp_one, data_one, previous_hash_one)
#block_chain = BlockChain(block_one)

# Test Case 2
time_stamp_two = time.time()
data_two = "HelloBlock2"
previous_hash_two = 0
block_chain.add_a_block(time_stamp_two, data_two)
print(f"2 {block_chain}")
# Test Case 3
time_stamp_three = time.time()
data_three = "HelloBlock3"
previous_hash_three = 0
block_chain.add_a_block(time_stamp_three, data_three)

print(f"3 {block_chain}")

block_chain.traverse()
# Reference: https://knowledge.udacity.com/questions/363520