""" 
You have been given an array containg numbers. Find and return the largest sum in a contiguous subarray within the input array.
"""

def max_sum_sub_array(input_array):
    current_sum = input_array[0]
    max_sum = [0]
    
    for element in input_array[1:]:
        current_sum = max(current_sum + element, element)
        max_sum = max(current_sum, max_sum)
    return max_sum