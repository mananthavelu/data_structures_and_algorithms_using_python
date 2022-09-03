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

"""
# Time complexity :O(nlogn)

whereas;
n - total number of calls

a. Finding 'final_result' requires O(n)

b. Once the 'final_result' is constrcuted, then it needs one more complete traverse to collect the i)fixed lines ii)mobile numbers and iii)Tele marketers.
This needs O(n)

c. Sorting needs O(nlogn)

So overall:

O(n + n + nlogn + constant operations)

Final and predominant time complexity: O(nlogn)
Index based retrivals in an array is a constant time operation. However as we do this for all elements twice, in normal and worst case,
O(n*n) will be needed.

# Space complexity :O(n)

We store results in 'results' and 'final_result' which each count for O(n) making the space complexity: O(n + n) i.e O(2n)

Simplifying the above space yields O(n)

""" 