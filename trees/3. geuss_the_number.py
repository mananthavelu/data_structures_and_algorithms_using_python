# Interative solution
"""
def binary_search(input_array, target):
    start_index = 0
    end_index = len(input_array) - 1
    while start_index <= end_index:
        middle_index = (start_index + end_index) // 2
        if input_array[middle_index] > target:
            end_index = middle_index - 1
        elif input_array[middle_index] < target:
            start_index = middle_index + 1
        else:
            return middle_index
    return -1
    
print(binary_search([1,2,3,4,5], 4))
""" 
# Recursive solution

def binary_search_recursive(array, target):
    return binary_search_helper(array, target, 0, len(array) - 1)

def binary_search_helper(array, target, start_index, end_index):
    if start_index > end_index:
        return -1
    middle_index = (start_index + end_index) // 2
    
    if array[middle_index] == target:
        return middle_index
    elif array[middle_index] > target:
        binary_search_helper(array, target, start_index, middle_index - 1)
    else:
        binary_search_helper(array, target, middle_index + 1, end_index)

print(binary_search_recursive([1,2,3,4,5,5], 5))