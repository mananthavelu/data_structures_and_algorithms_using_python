# Given the equation in Polish notation as list of elements, express in normal mathematical way and return the results
# eg 3 1 + 4 * -> (3 + 1) * 4 returning 16

def reverse_polish(input_list):
    stack = Stack()
    for char in input_list:
        # For operators, simply pop the two last elements and perform the operation
        if char == '*':
            second_item = stack.pop()
            first_item = stack.pop()
            result = second_item * first_item
            stack.push(result)
        elif char == '/':
            second_item = stack.pop()
            first_item = stack.pop()
            result = second_item / first_item
            stack.push(result)
        elif char == '+':
            second_item = stack.pop()
            first_item = stack.pop()
            result = second_item + first_item
            stack.push(result)
        elif char == '-':
            second_item = stack.pop()
            first_item = stack.pop()
            result = second_item - first_item
            stack.push(result)
        else:
            #For all operands, simply add to stack
            stack.push(char)
    return stack.pop()