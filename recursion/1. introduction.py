# Definition: Recursion is a TECHNIQUE for solution for the problem depends upon the 
# solution for the smaller instance of the same problem

# Eg. Calculate 2**5 is the main problem
# The solution to the above problem depends the smaller instance of the same problem 2 * (2**5-1 = 2**4)
# If we know the value of 2**4 , then we can easily calculate the value for 2**5

# Eg. Calculate power of 2
"""
2**5 means

2*2*2*2*2

The multiplication of 2 is repetetive.

2**5 = 2* (2**4)
2**4 = 2* (2**3)
2**3 = 2* (2**2)
2**2 = 2* (2**1)
2**1 = 2 * (2**0) # is the base case

""" 
def power_of_two(input_value):
    # Base case: when to stop the recursion and what to return in each recursive function
    if input_value == 0:
        return 1
    return 2 * power_of_two(input_value - 1)

print(power_of_two(5))