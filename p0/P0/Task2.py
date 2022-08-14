"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open(r"C:\Users\32470\Desktop\coding_practice\data_structures_and_algorithms_using_python\p0\texts.csv", 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open(R'C:\Users\32470\Desktop\coding_practice\data_structures_and_algorithms_using_python\p0\calls.csv', 'r') as f:
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
high_time = 0
high_time_spent = {highest_caller : high_time}
