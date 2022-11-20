def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    left = 0
    right = len(input_list) - 1
    current_zero_position = 0
    # The goal is to move all 0s to the front and 2s to the end
    while left <= right:
        if input_list[left] == 0:
            input_list[left] == input_list[current_zero_position]
            current_zero_position += 1
            left += 1
        elif input_list[left] == 2:
            input_list[left] == input_list[right]
            input_list[right] = 2
            right -= 1
        else:
            left += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])