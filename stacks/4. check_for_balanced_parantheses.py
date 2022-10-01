# The goal is to check if all the parantheses pairs are balanced

# First - Implementation of Stack
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
    
    
# Concept: Add each '('  to the stack
# For each ')', pop an open paranthesis
# Return False; when poped element is None (means, there are more '(' and less ')' 


def balanced_parantheses(input_string):
    if input_string == '':
        return False
    stack = Stack()
    for char in input_string:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if stack.pop() is None:
                return False
    if stack.size() == 0:
        return True
    else:
        return False
            
    