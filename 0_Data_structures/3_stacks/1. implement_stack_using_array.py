# Stack is a data structure which is helpful to manipulate or operate on the last element which was added
# In Python, Stack is implemented with the help of list
# In Stack, Last element which was added; is the first element which can be removed.

# Concepts

# Create a Stack class with some constant length and same values
# Keep the total number of elements , last_index used in the Stack
# Push the new element to the next available index
# Remove the element from the last index

class Stack:
    def __init__(self, initial_size = 10):
        self.array = [0 for _ in range(initial_size)]
        self.next_index = 0
        self.number_of_elements = 0
    
    #Checking if a list
    def is_empty(self):
        if len(self.array) == 0:
            return True
        return False
    
    #Adding a new element
    def push(self, data):
        if self.next_index == len(self.array):
            self.handle_stack_capacity()
        
        self.array[self.next_index] = data
        self.next_index += 1
        self.number_of_elements += 1
    
    # Handle the capacity of the Stack
    def handle_stack_capacity(self):
        old_array = self.array
        
        self.array = [0 for _ in range(2 * len(self.array))]
        for index, element in enumerate(old_array):
            self.array[index] = element
    
    # Size of the stack
    def size_of_stack(self):
        return len(self.array)
    
    # Return an element
    def remove_an_element(self):
        if self.is_empty():
            return None
        self.next_index -= 1
        self.number_of_elements -= 1
        return self.array[next_index]