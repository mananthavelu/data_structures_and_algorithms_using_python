"""
Input [1,2,3]
Output [1,2,4]

Input [1,2,9]
Output [1,3,0]

Input [9,9,9]
Output [1,0,0,0]
"""
def add_one_to_list(input_list):
    if input_list == [9]:
        return [1,0]
    if input_list[-1] < 9:
        input_list[-1] += 1
    else:
        input_list = add_one_to_list(input_list[:-1]) + [0]
    return input_list


inputs = [[1,2,3], [1,3,9], [9,9,9]]
expected_outputs = [[1,2,4], [1,4,0], [1,0,0,0]]
#inputs = [[1,2,3], [1,3,9]]
#expected_outputs = [[1,2,4], [1,4,0]]

def test_add_one_to_list():
    for input, expected_output in zip(inputs, expected_outputs):
        actual_output = add_one_to_list(input)
        print(actual_output)
        assert actual_output == expected_output, 'Test has failed'
        print("Tests are successful")
    return

test_add_one_to_list()