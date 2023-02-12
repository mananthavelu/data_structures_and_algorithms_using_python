"""Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is maximum. Return these two numbers. 
You can assume that all array elements are in the range [0, 9]. 
The number of digits in both the numbers cannot differ by more than 1. 
You're not allowed to use any sorting function that Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In scenarios such as these when there are more than one possible answers, return any one.

Here is some boilerplate code and test cases to start with:"""


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """

    
    length_of_input_list = len(input_list)

    if length_of_input_list == 0:
        return []

    if length_of_input_list == 1:
        return input_list


    number_one = []
    number_two = []
    #
    for i in range(9, -1, -1):# Iterate from 9 to 0 in reverse order/Larger to smaller value
        for j, number in enumerate(input_list):# Iterate the input list
            if number == i:
                if len(number_one) <= len(number_two):
                    number_one.append(str(number))
                else:
                    number_two.append(str(number))

    number_one = int("".join(number_one))
    number_two = int("".join(number_two))
    return [number_one, number_two]


def test_function(test_case):
    """Test function for rearrange_digits

    Args:
        test_case (_type_): which contains the input list with expected outcome
    """
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# Test cases
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
