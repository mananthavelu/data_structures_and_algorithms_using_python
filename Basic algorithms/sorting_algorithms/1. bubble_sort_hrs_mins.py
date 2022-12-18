# Input format: Tuple containing an hour and minutes
sleep_times = [(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]

# THought process

# We can apply bubble sort; however with a condition on the hour and minutes

def sort_hour_minutes(input_array):
    for count in range(len(input_array)):
        for index in range(len(input_array) - 1):
            current_hour, current_min = input_array[index]
            next_hour, next_min = input_array[index + 1]
            if current_hour < next_hour or (current_hour == next_hour and current_min < next_min):
                continue
            input_array[index] = next_hour, next_min
            input_array[index + 1] = current_hour, current_min
    return input_array


print(sort_hour_minutes([(24,13), (21,55), (23,20), (22,5), (24,23), (21,58), (24,3)]))