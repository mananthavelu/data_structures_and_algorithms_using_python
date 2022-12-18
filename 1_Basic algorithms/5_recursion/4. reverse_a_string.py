# Goal: Given a string, reverse


# Concept: Take the first letter in the string
# Reverse the remaining sub-string and attach the first letter in the last


def reverse_a_string(input_string):
    if len(input_string) == 0:
        return ""

    first_letter = input_string[0]
    sub_string = input_string[1: len(input_string)]
    return reverse_a_string(sub_string) + first_letter

print(reverse_a_string("marimuthu"))
    