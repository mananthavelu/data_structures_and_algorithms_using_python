"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open(r"C:\Users\32470\Desktop\coding_practice\data_structures_and_algorithms_using_python\p0\texts.csv", 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open(R'C:\Users\32470\Desktop\coding_practice\data_structures_and_algorithms_using_python\p0\calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
from operator import itemgetter

def get_all_telephone_numbers(nested_list, position):
    return list(map(itemgetter(position), nested_list))

total_records_in_both_files = get_all_telephone_numbers(texts, 0) + get_all_telephone_numbers(texts, 1) + get_all_telephone_numbers(calls, 0)  + get_all_telephone_numbers(calls, 1)
print(f"There are {len(set(total_records_in_both_files))} different telephone numbers in the records.")
