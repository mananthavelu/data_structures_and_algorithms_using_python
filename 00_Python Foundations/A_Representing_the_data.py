# Representing the data

# 1.Basic Elements

# 1.1 None

# None is a special constant which represents the absence of the value

# 1.2 Boolean

# True - A presence of something
# False - An absence of something

start_value = 0
value_until_to_print = 10
while True:
    if start_value <= value_until_to_print:
        print(start_value)
    else:
        break
    start_value += 1


# 1.3 Integer

x = 100
y = x.__str__()
print(x)
print(y)
print(type(x))
print(type(y))
print(y + ' Hey')
#help(x)


# 1.4 String/Text
# String a sequence of character(s)
# It is a collection
# It is an iterable
# It is sized
# Collections