# Calculate the hamming distance between two strings
# Hamming distance is the number of positions the corresponding symbols are different between two given strings

def calculate_hamming_distance(string_one, string_two):
    if len(string_one) != len(string_two):
        return None

    if string_one == string_two:
        return None
    result = 0
    for index in range(len(string_one)):
        if string_one[index] != string_two[index]:
            result += 1
    return result

print ("Pass" if (10 == calculate_hamming_distance('ACTTGACCGGG','GATCCGGTACA')) else "Fail")
print ("Pass" if  (1 == calculate_hamming_distance('shove','stove')) else "Fail")
print ("Pass" if  (None == calculate_hamming_distance('Slot machines', 'Cash lost in me')) else "Fail")
print ("Pass" if  (9 == calculate_hamming_distance('A gentleman','Elegant men')) else "Fail")
print ("Pass" if  (2 == calculate_hamming_distance('0101010100011101','0101010100010001')) else "Fail")