# Given two sorted arrays, combine and return them in a single sorted array
def combine_and_sort_arrays(array_one_sorted, array_two_sorted):
    index_first_array = index_second_array = 0
    result_array = []
    while index_first_array < len(array_one_sorted) and index_second_array < len(array_two_sorted):
        if array_one_sorted[index_first_array] < array_two_sorted[index_second_array]:
            result_array.append(array_one_sorted[index_first_array])
            index_first_array += 1
        elif array_one_sorted[index_first_array] > array_two_sorted[index_second_array]:
            result_array.append(array_two_sorted[index_second_array])
            index_second_array += 1
        else:
            result_array.append(array_one_sorted[index_first_array])
            result_array.append(array_two_sorted[index_second_array])
            index_first_array += 1
            index_second_array += 1
    if index_first_array < len(array_one_sorted):
        result_array += array_one_sorted[index_first_array:]
    if index_second_array < len(array_two_sorted):
        result_array += array_two_sorted[index_second_array:]
    return result_array


print("Success" if combine_and_sort_arrays([1, 2], [3,5,8]) == [1, 2, 3, 5,8] else "Failure")


# Time complexity: O(n+m) where n - size of the first array, m - size of the second array
# Space complexity: O(n+m) where n - size of the first array, m - size of the second array