def sqrt(number):
   
   """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
   """
   if number is None or '':
      return None
   #candidate_value = number % 2

   # THe approach is similar to 'searching in Binary search tree'
   # Search criteria: The squared value of an iterm is equal to the given number
   return search_square_root(0, number, number)

def search_square_root(left, right, number):
   if left == right:
      return left
   if left <= right:
      middle_value = (left + ((right - left) // 2))
      middle_value_squared = int(middle_value **2)
      if middle_value_squared < number:
         return search_square_root(middle_value + 1, right, number)
      elif middle_value_squared > number:
         return search_square_root(left, middle_value - 1, number)
      else:
         return middle_value
   return None

print ("Pass" if  (3 == sqrt(9)) else "Fail")#returns Pass
print ("Pass" if  (0 == sqrt(0)) else "Fail")#returns Pass
print ("Pass" if  (4 == sqrt(16)) else "Fail")#returns Pass
print ("Pass" if  (1 == sqrt(1)) else "Fail")#returns Pass
print ("Pass" if  (5 == sqrt(27)) else "Fail")#returns Pass
print ("Pass" if  (None == sqrt(None)) else "Fail")#returns Pass
