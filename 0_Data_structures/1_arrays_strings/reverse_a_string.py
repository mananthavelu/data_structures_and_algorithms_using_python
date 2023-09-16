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
print(reverse_a_string(input_string))