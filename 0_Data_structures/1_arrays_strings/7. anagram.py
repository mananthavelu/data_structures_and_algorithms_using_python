# Check if given two strings are anagram or not

def check_anagram(string_one, string_two):
    if len(string_one) != len(string_two):
        return False
    
    def count_letters(input_string):
        frequency_of_letters = {}
        for character in input_string:
            if character in frequency_of_letters:
                frequency_of_letters[character] += 1
            else:
                frequency_of_letters[character] = 0
        
    string_one_frequency_of_letters = count_letters(string_one)
    string_two_frequency_of_letters = count_letters(string_two)
    if string_one_frequency_of_letters == string_two_frequency_of_letters:
        return True
    return False

#print("Pass" if check_anagram("mari", "riam") == True else "Fail")


# Alternative method

def check_anagram_two(string_one, string_two):
    string_one = string_one.replace(" ", "").lower()
    string_two = string_two.replace(" ", "").lower()
    if len(string_one) != len(string_two):
        return False
    return sorted(string_one) == sorted(string_two)

print("Pass" if check_anagram_two("mari", "riam") == True else "Fail")
print ("Pass" if not (check_anagram_two('water','waiter')) else "Fail")
print ("Pass" if check_anagram_two('Dormitory','Dirty room') else "Fail")
print ("Pass" if check_anagram_two('Slot machines', 'Cash lost in me') else "Fail")
print ("Pass" if not (check_anagram_two('A gentleman','Elegant men')) else "Fail")
print ("Pass" if check_anagram_two('Time and tide wait for no man','Notified madman into water') else "Fail")
