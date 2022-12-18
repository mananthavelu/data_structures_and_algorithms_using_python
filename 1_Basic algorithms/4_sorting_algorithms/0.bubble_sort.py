# Concept: Compare the pair of neighbouring elements in each iteration, move the largest element to the right end
# In each iteration; the largest element in the array will bubble on top
# Naive approach
""" 
Start at the beginning of the array
Check if the first > second element; if yes - swap, if not; dont do anything
Repeat this step as many number of times of the length of the array / until the input array is sorted

""" 
def bubble_sort(input_array):
    for iteration in range(len(input_array)):
        for index in range(len(input_array) - 1):
            if input_array[index] > input_array[index + 1]:
                input_array[index], input_array[index + 1] = input_array[index +1 ] , input_array[index]
    return input_array

print(bubble_sort([3,2,1,5,6,17,5]))


# Efficiency of the algorithm
# Run time (worst/ average): n2 (i.e (n-1) iterations with (n-1) comparisons), Best: O(n) i.e the array is already sorted
# We can save sometime ; still not good
# Space complexity: O(n) because it is an in-place sorting