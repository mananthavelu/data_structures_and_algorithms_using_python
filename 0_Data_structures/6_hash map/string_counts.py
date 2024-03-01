def count_the_strings(input_string):
	"""
	This function takes a string as input and returns a dictionary with the count of each string in the input.
	"""
	string_counts = {}
	for string in input_string.split():
		if string in string_counts:
			string_counts[string] += 1
		else:
			string_counts[string] = 1
	return string_counts

# Efficiently calculate the count of each string in the input string
input_string = "I am learning Python and Python is easy"
def count_the_strings(input_string):
	string_counts = {}
	for string in input_string.split():
		string_counts[string] = string_counts.get(string, 0) + 1
	return string_counts
print(count_the_strings(input_string))
# Path: 0_Data_structures/6_hash%20map/word_count.py

def count_the_characters_in_string(input_string):
	"""
	This function takes a string as input and returns a dictionary with the count of each character in the input.
	"""
	character_counts = {}
	for character in input_string:
		if character in character_counts:
			character_counts[character] += 1
		else:
			character_counts[character] = 1
	return character_counts

# Efficiently calculate the count of each character in the input string
def count_the_characters_in_string(input_string):
	character_counts = {}
	for character in input_string:
		character_counts[character] = character_counts.get(character, 0) + 1
	return character_counts

print(count_the_characters_in_string("Hello"))