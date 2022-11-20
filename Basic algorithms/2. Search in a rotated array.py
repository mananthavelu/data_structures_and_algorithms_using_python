def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    # Find the index of a random pivot
    left = 0
    right = len(input_list) - 1
    def find_pivot(input_list, left, right):
        if left == right:
            return left
        if (right - left) == 1:
            return right
        if (left - right) == 1:
            return left
        middle = (left + right) // 2
        if input_list[middle] > input_list[right]:
            return find_pivot(input_list, middle, right)
        elif input_list[middle] < input_list[right]:
            return find_pivot(input_list, left, middle)
        else:
            return middle
    pivot = find_pivot(input_list, left, right)

    def binary_search(input_list, number, left, right, pivot):
        if number == input_list[pivot]:
            return pivot
        elif input_list[pivot] <= number and number < input_list[right]:
            return binary_search(input_list, number, ((right - input_list[pivot])//2) + pivot, pivot, right)
        elif input_list[0] <= number and number <= input_list[pivot - 1]:
            return binary_search(input_list, number, ((pivot - left)//2), 0, pivot-1)
        else:
            return -1
    return binary_search(input_list, number, 0, right, pivot)

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4] , 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])