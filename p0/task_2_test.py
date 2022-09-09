calls = [[1,2,3,4], [1,2,3,4], [1,2,3,4], [1,2,3,4],[5,2,5,300]]
print(len(calls))
total_calls = len(calls) - 1
#total_calls = 5
sum_of_call_duration = {}
list_of_index = [0,1]
for index_position in list_of_index:
    count = 0
    while count <= total_calls:
        phone_number = calls[count][index_position]
        call_duration = calls[count][3] 
        if phone_number in sum_of_call_duration.keys():
            sum_of_call_duration[phone_number]  += call_duration
        else:
            sum_of_call_duration[phone_number] = call_duration
        count += 1
        

print(max(sum_of_call_duration.values()))
print(sum_of_call_duration.values())
print(sum_of_call_duration)