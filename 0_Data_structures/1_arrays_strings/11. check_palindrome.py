# Given a string, check if it is a palindrome
def check_palindrome(input_string):
    if len(input_string) == 0:
        return True
    left_pointer = 0
    right_pointer = len(input_string) - 1
    while left_pointer < right_pointer:
        if input_string[left_pointer] == input_string[right_pointer]:
            left_pointer += 1
            right_pointer -= 1
        else:
            return False
    return True

print("Success" if check_palindrome('mari') == False else "Failure")
print("Success" if check_palindrome('level') == True else "Failure")
print("Success" if check_palindrome('') == True else "Failure")
print("Success" if check_palindrome('A B C') == False else "Failure")
print("Success" if check_palindrome('AB BA') == True else "Failure")
print("Success" if check_palindrome('AB bA') == False else "Failure")

# Time complexity: O(n)
# Space complexity: O(1)