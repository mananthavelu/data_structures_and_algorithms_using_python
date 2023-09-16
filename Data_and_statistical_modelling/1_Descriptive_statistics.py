sample = np.random.choice(pop_data, size = 3)
mean = np.mean(sample)
var_sample = np.var(sample)
std_sample= np.std(sample)
print(mean, var_sample, std_sample)
mean_population = np.mean(pop_data)
var_population = np.var(pop_data)
std_population = np.std(pop_data)
print(mean_population, var_population, std_population)
mean_size_3 = []
for _ in range(10000):
    sample_draw = np.random.choice(pop_data, size = 3)
    mean_size_3.append(np.mean(sample_draw))

var_3 = np.var(mean_size_3)
std_3 = np.std(mean_size_3)
mean_3 = np.mean(mean_size_3)
print(mean_3, var_3, std_3)

import matplotlib.pyplot as plt
plt.hist(mean_size_3, alpha = 0.6, label = 'Sample size 3')
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

#print(calculate_mean_method_one([10,12,14]))

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

#print(calculate_mean_method_two([10,12,14]))


# Median

# Method - 1

def calculate_median_method_one(list_of_values):
    sorted_list_of_values = sorted(list_of_values)
    length_of_input = len(list_of_values)
    if length_of_input % 2 == 0:
        median = (sorted_list_of_values[(length_of_input//2)-1] + sorted_list_of_values[(length_of_input//2)]) // 2
        print(median)
    elif length_of_input % 2 == 1:
        median = sorted_list_of_values[length_of_input//2]
    return median

print("Successful" if calculate_median_method_one([1,2,3,4,5,6,7]) == 4 else "Error")
print("Successful" if calculate_median_method_one([10,28,38,4,95,6,57]) == 28 else "Error")


# Mode

# Method - 1

def calculate_median_method_one(list_of_values):
    frequency_of_values = {}
    for value in list_of_values:
        if value in frequency_of_values.keys():
            frequency_of_values[value] += 1
        else:
            frequency_of_values[value] = 1

    mode = {key:value for key, value in sorted(frequency_of_values.items(), key  = lambda item:item[1], reverse=True)}
    return list(mode.keys())[0]

print("Successful" if calculate_median_method_one([1,2,3,3,5,6,7]) == 3 else "Error")
print("Successful" if calculate_median_method_one([1,2,3,3,5,5,5,6,7]) == 5 else "Error")


# Percentiles / Quantiles