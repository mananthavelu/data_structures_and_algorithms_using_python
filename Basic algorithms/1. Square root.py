def sqrt(number):
   
   """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
   """
   #candidate_value = number % 2

   # THe approach is similar to 'searching in Binary search tree'
   # Search criteria: The squared value of an iterm is equal to the given number
   return search_square_root(0, number, number)

def search_square_root(left, right, number):
   if left <= right:
      middle_value = (left +right) % 2
      if (middle_value*middle_value <= number) and ((middle_value + 1) * (middle_value + 1) > number):
         return middle_value
      elif (middle_value *middle_value) < number:
         search_square_root(middle_value + 1, right, number)
      else:
         search_square_root(left, middle_value - 1, number)
   return left

print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")