# Problem Statement: https://leetcode.com/problems/two-sum/

"""
Examples:
nums = [1, 2, 4, 5, -4, 2]
target = 9
Output = [4, 5]
"""

def two_sum(input_numbers, target_sum):
    # Return True if there are two numbers in the sorted array: input_numbers that add up to the target_sum

    if len(input_numbers) == 0:
        return False

    left_index = 0
    right_index = len(input_numbers) - 1

    while left_index < right_index:
        calculated_sum = input_numbers[left_index] + input_numbers[right_index]
        if calculated_sum == target_sum:
            return True
        elif current_sum < target_sum:

    

