def front_back(str):
  first_element = str[0]
  last_element = str[-1]
  string_to_list = [*str]
  string_to_list[0] = last_element
  string_to_list[-1] = first_element
  return ''.join(string_to_list)

print("Pass" if front_back('mari') == 'iarm' else "Fail")