""" 
You have been given an array of length = n. The array contains integers from 0 to n - 2. 
Each number in the array is present exactly once except for one number which is present twice.
Find and return this duplicate number present in the array
"""

def remove_duplicate(input_array):
    current_sum = 0 
    expected_sum = 0
    
    for element in input_array:
        current_sum += element
        
    for element in range(len(input_array) - 1):
        expected_sum += element
    
    return current_sum - expected_sum

print(remove_duplicate([0,1,2,3,4,4]))
