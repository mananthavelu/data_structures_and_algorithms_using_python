"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open(r'C:\Users\32470\Desktop\coding_practice\dsa_python\p0\calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore. In other words, the calls were initiated by "(080)" area code
to the following area codes and mobile prefixes:
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
# Part A

results = []
for element in calls:
  if element[0][0:5] == '(080)':
    results.append(element[1])
    
final_result = []

for element in results:
  if element[0] == '(':
    index_needed = element.index(')')
    final_result.append(element[0:index_needed + 1])
  elif element[0] in ['7', '8' ,'9']:
    final_result.append(element[0:4])
  else:
    final_result.append(element[0:3])

final_result_unique = sorted(list(set(final_result)))

#print("The numbers called by people in Bangalore have codes:")
print(*final_result_unique, sep = "\n")

# Part B

#print(final_result)
print(f"{round((final_result.count('(080)') / len(final_result) * 100), 2)} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.")



"""
Part - A:

# Time complexity :O(nlogn)- Worst case

whereas;
n - total number of calls

The different number of operations we perform include;

a. Finding ' results' require O(n)
b. Once the 'results' is constrcuted, then it needs one more complete traverse to collect the i)fixed lines ii)mobile numbers and iii)Tele marketers.
This needs O(n)
c. Sorting needs O(nlogn)

So overall:

O(n + n + nlogn + constant operations)

Final and predominant time complexity: O(nlogn)

# Space complexity :O(n)- Worst case

We store results in 'results' and 'final_result' which each count for O(n) making the space complexity: O(n + n) i.e O(2n)

Simplifying the above by neglecting the constant time operations yield O(n)

""" 