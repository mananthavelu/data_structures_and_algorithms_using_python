"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open(r"C:\Users\32470\Desktop\coding_practice\dsa_python\p0\texts.csv", 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open(r'C:\Users\32470\Desktop\coding_practice\dsa_python\p0\calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

calling_numbers = []
for element in calls:
    if element[0][0:3] == '140':
        calling_numbers.append(element[0])

        

call_nos = set(calling_numbers)

receiving_nos = set(map(lambda x: x[1], calls))
sending_test = set(map(lambda x: x[0], texts))
receiving_test = set(map(lambda x: x[1], texts))

result1 = call_nos.difference(receiving_nos)
result2 = result1.difference(sending_test)
result3 = result2.difference(receiving_test)

print(f"These numbers could be telemarketers: ")

print(*sorted(list(result3)), sep = "\n")

