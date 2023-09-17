def reverse_a_string(input_string):
    """
    returns a reversed input string

    Argument (string) : input string
    Output (string): Reversed input string
    """

    # This method uses the indexing in which the we traverse from the end to start
    # The negative sign in the 'step' indicates the reverse direction of traversal
    return input_string[::-1]


# Tests
input_string = "Zurich"
# print(reverse_a_string(input_string))
# print("Pass" if reverse_a_string("Zurich") == "hciruZ" else "Fail")
# print("Pass" if reverse_a_string("Dubendorf") == "frodnebuD" else "Fail")
# print("Pass" if reverse_a_string("") == "" else "Fail")

# Alternative method

def reverse_a_string_two(input_string):
    reversed_string = ""
    for character_index in range(len(input_string)-1, -1, -1):
        reversed_string += input_string[character_index]
    return reversed_string


# Tests
print("Pass" if reverse_a_string_two("Zurich") == "hciruZ" else "Fail")
print("Pass" if reverse_a_string_two("Dubendorf") == "frodnebuD" else "Fail")
print("Pass" if reverse_a_string_two("") == "" else "Fail")
