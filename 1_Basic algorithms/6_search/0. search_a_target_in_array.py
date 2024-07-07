# Interative solution

def binary_search(input_array, target):
    start_index = 0
    end_index = len(input_array) - 1
    while start_index <= end_index:
        middle_index = start_index + (end_index - start_index) // 2
        if input_array[middle_index] > target:
            end_index = middle_index - 1
        elif input_array[middle_index] < target:
            start_index = middle_index + 1
        else:
            return True
    return False
print(binary_search([1,2,3,4,5], 4))