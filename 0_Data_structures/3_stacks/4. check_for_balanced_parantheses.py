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
# Idea: Equal number of times the '(' is pushed and '(' is popped.

# ((32+8)∗(5/2))/(2+6)
class Stack:
    def __init__(self):
        self.items = []
    
    def size(self):
        return len(self.items)
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.size()==0:
            return None
        else:
            return self.items.pop()

def balanced_parantheses(input_string):
    mapping = {')': '(', '}':'{'}
    if input_string == '':
        return False
    stack = Stack()
    for char in input_string:
        if char == '(':
            stack.push(char)
        elif char == ')':
            if mapping[char] != stack.pop():
                return False
                
    return stack.size() == 0

print(f"Successful" if balanced_parantheses('((32+8)∗(5/2))/(2+6)') == True else "Failed")
print(f"Successful" if balanced_parantheses('((32+8))∗(5/2))/(2+6)') == False else "Failed")