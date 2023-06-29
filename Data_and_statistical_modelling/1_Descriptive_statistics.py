# Meansure of central value

# Mean

# Method -1
def calculate_mean_method_one(list_of_values):
    """
    Used to calculate the mean for the input values/list of values

    Parameters:
        list_of_values (list or tuple): list of input values

    returns:
        mean
    """
    number_of_elements = len(list_of_values)
    sum_of_values = 0
    
    for value in list_of_values:
        sum_of_values += value
    
    return f"The mean is {sum_of_values/number_of_elements}"

print(calculate_mean_method_one([10,12,14]))

# Method -2
def calculate_mean_method_two(list_of_values):
    """
    Used to calculate the mean for the input values/list of values

    Parameters:
        list_of_values (list or tuple): list of input values

    returns:
        mean
    """    
    return f"The mean is {sum(list_of_values)/len(list_of_values)}"

print(calculate_mean_method_two([10,12,14]))