"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
#Import the required library
from operator import itemgetter

def get_all_telephone_numbers(nested_list, position):
    """_summary_

    Args:
        nested_list (list): list of lists
        position (integer): index in the list

    Returns:
        list: list of integers
    """
    # Collect the list of phone numbers using index position
    return list(map(itemgetter(position), nested_list))

total_records_in_both_files = len(set(get_all_telephone_numbers(texts, 0) + get_all_telephone_numbers(texts, 1) + get_all_telephone_numbers(calls, 0)  + get_all_telephone_numbers(calls, 1)))
print(f"There are {total_records_in_both_files} different telephone numbers in the records.")


"""
# Time complexity :O(m**2)- Worst case

whereas;
n - total number of calls
m - total number of texts messages

Index based retrivals in an array is a constant time operation. However as we do this for all elements twice, in normal and worst case,
O(n*n) / O(m*m) will be needed.

if we consider the total number of texts > total number of calls; then the simplified version of time complexity is: O(m**2)

# Space complexity :O(1)- Worst case

The final results are calculated directly and stored in a variable 'total_records_in_both_files'.

""" 

