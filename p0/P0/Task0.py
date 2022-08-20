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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
print(f"First record of texts, {texts[0][0]}  texts {texts[0][1]} at time {texts[0][2]}")
print(f"Last record of calls, {calls[-1][0]} calls {calls[-1][1]} at time {calls[-1][2]}, lasting {calls[-1][3]} seconds")

"""
# Time complexity :O(1)

Index based retrivals in an array is a constant time operation. These 7 different retrivals are simplified as O(1)

# Space complexity :O(1)

This is because of the space allocated for storing the retrived results. 
In total; we retrive 7 different values using index of a 2-dimensional array. However given the (in)significance 
of the individual retrival to the size of the array; O(1) is considered.
""" 