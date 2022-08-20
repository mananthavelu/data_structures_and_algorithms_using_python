"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open(r"C:\Users\32470\Desktop\coding_practice\data_structures_and_algorithms_using_python\p0\texts.csv", 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open(R'C:\Users\32470\Desktop\coding_practice\data_structures_and_algorithms_using_python\p0\p0\calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

total_calls = len(calls) - 1
# Create a dictionary which keeps adding the 'duration of telephone call in seconds (string)' for each phone number
call_dur_res = {}
# Specify the indexes in the calls (nested lists where the phone numbers are stored)
list_of_index = [0,1]
#Travers all the phone numbers and update the call duration each time
for index_position in list_of_index:
    count = 0
    while count <= total_calls:
        phone_number = calls[count][index_position]
        call_duration = calls[count][3] 
        if phone_number in call_dur_res.keys():
            call_dur_res[phone_number]  += int(call_duration)
        else:
            call_dur_res[phone_number] = int(call_duration)
        count += 1

# Finding the key / Phone number in the results which has the maxi.value
max_dur = max(call_dur_res, key=call_dur_res.get)

#Printing the results
print(f"{max_dur} spent the longest time, {call_dur_res[max_dur]} seconds, on the phone during September 2016.")
