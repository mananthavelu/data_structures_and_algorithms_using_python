# Goal: The number 123 would be provided as arr = [1, 2, 3]. Add one to the number and return the output in the form of a new list.

# Examples:[1,2,3] will return [1,2,4]
# Examples:[1,9,9] will return [2,0,0]



def add_one(input_array):
    borrow = 1
    for i in range(len(input_array), 0, -1):
        digit = borrow + input_array[i-1]
        borrow = digit // 10
        if borrow == 0:
            input_array[i-1] = digit
            break
        else:
            input_array[i-1] = digit % 10
            
    input_array = [borrow] + input_array
    position = 0
    while input_array[position] == 0:
        position += 1
    return input_array[position:]

            
print(add_one([1,2,3]))
print(add_one([1,2,9]))
print(add_one([9,9]))