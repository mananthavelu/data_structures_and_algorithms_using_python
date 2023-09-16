# 1. Basic Function
def check_for_membership(item, input_array):
    """
    This function receives an input array and an item for which the membership property is checked against

    Args:
    item (integer): an item which needs to be checked for its presence in an input_array.
    input_array (list): an input list which contains collection of elements.

    Returns:
    Boolean: True or False if an item foundin the input_array or not.
    """
    for element in input_array:
        if item == element:
            return True
    else:
        return False

if __name__ == "__main__":
    print("pass" if check_for_membership(1, [2,3,4]) == False else "Fail")
    print("pass" if check_for_membership(3, [2,3,4]) == True else "Fail")

# 2. Functions with several types of parameters