# Concept: Compare the pair of elements in each iteration, move the largest element to the right end
# In each iteration; the largest element in the array will bubble on top
# Naive approach
def bubble_sort(input_array):
    for iteration in range(len(input_array)):
        for index in range(len(input_array) - 1):
            if input_array[index] > input_array[index + 1]:
                input_array[index], input_array[index + 1] = input_array[index +1 ] , input_array[index]
    return input_array

print(bubble_sort([3,2,1,5,6,17,5]))