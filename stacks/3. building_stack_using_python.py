# Stack consists of two main operations: push and pop
# This implementation is directly using list - which acts similar to dynamic array



class Stack:
    def __init__(self):
        self.items = []
        
    def size(self):
        return len(self.items)
    
    def push(self, new_data):
        self.items.append(new_data)
        return

    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop()