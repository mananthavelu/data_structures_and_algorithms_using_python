# Stack is a data structure which has a property which is; we can manipulate or operate on the last element which was added
# In Stack, the element which we added last, is the element which can be removed at first. This is called Last In, First Out principle
# We can not remove any other element without removing the element which was added after to it
# In Python, Stack can be implemented either using a list or Linked list

# Concepts
# Create a Stack class with some constant length and same values: This helps us to have a stack with certain size and contents (with no specific meaning to the problem in hand)
# Add the attributes which will help is to keep track of the total number of elements which are added to the Stack, the index on which the next element is to be added when adding a new element
# Wheneve we push a new element or remove an element (which was last pushed), update the instance attributes
# Whenever we wush the new element to the next available index, insert the new element into the next_index and update the next_index with increment of 1
# Remove the element from the last index

class Stack:
    def __init__(self, initial_size = 5):
        self.array = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.number_of_elements = 0
    
    #Check if a stack is empty
    def is_empty(self):
        if next_index == 0:
            return True
        return False
    
    #Add a new element to a Stack
    def push(self, data):
        if self.next_index == len(self.array):
            self.handle_stack_capacity()
        self.array[self.next_index] = data
        self.next_index += 1
        self.number_of_elements += 1
    
    # Handle the capacity of the Stack
    def handle_stack_capacity(self):
        old_array = self.array
        new_array = [None for _ in range(2* len(self.array))]
        for index, value in enumerate(old_array):
            new_array[index] = value
        self.array = new_array

    # Size of the stack
    def size_of_stack(self):
        return len(self.array)
    
    # Return an element
    def pop(self):
        if self.is_empty():
            return None
        self.next_index -= 1
        self.number_of_elements -= 1
        return self.array[next_index]
    
    # Print the Stack
    def __repr__(self):
        print(self.array)
        result = ''
        for element in self.array[:self.next_index]:
            element = str(element) + '->'
            result += element
        return result[:-2]

    def reverse(self):
        reversed_stack = []
        current_stack = self.array[:self.next_index]
        reversed_stack = current_stack[::-1] + self.array[self.next_index:]
        self.array = reversed_stack[:self.next_index]
        return

# Test the code 
# Create a stack 12,56,58,48 in which the 12 is added to the Stack first, 48 as last
stack_one = Stack()
stack_one.push(12)
stack_one.push(56)
stack_one.push(58)
stack_one.push(48)
stack_one.push(19)
stack_one.push(87)
stack_one.push(60)
stack_one.push(1)
print(stack_one)
stack_one.reverse()
print("I")
print(stack_one)
