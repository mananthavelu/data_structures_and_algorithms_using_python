# Goal: Check if a given string is palindrome

# Concept:
def palindrome_check(string_input):
    if len(string_input) <=1:
        return True
    
    first_letter = string_input[0]
    last_letter = string_input[-1]
    sub_string = string_input[1:-1]
    return (first_letter == last_letter) and palindrome_check(sub_string)


print(palindrome_check("cat"))
print(palindrome_check("wow"))