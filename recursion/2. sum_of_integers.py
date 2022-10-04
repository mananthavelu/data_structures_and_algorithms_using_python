def sum_of_integers(input_value):
    if input_value == 1:
        return 1
    
    return input_value + sum_of_integers(input_value - 1)

print(sum_of_integers(5))