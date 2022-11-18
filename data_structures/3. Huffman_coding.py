# Steps

# Set up a class for TreeNode and Binary Tree
import sys

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        
    @property
    def left(self):
        return self.left_child

    @left.setter
    def left(self, node):
        self.left_child = node

    @property
    def right(self):
        return self.right_child

    @right.setter
    def right(self, node):
        self.right_child = node

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, node):
        self._value = node

    def has_left_child(self):
        return self.left_child is not None

    def has_right_child(self):
        return self.right_child is not None


class BinaryTree:
    def __init__(self, value = None):
        self.root_node = TreeNode(value)
    
    @property
    def root_node(self):
        return self._root_node

    @root_node.setter
    def root_node(self, node):
        self._root_node = node
    


def huffman_encoding(data):
    # Frequency counter for each character in the given data
    if len(data) == 0:
        return None

    freq_of_char = {}
    for character in data:
        if character in freq_of_char.keys():
            freq_of_char[character] =+ 1
        else:
            freq_of_char[character] = 1
    # Sort using the frequency
    list_of_freq_count = [TreeNode((k,v)) for k, v in freq_of_char.items()]
    ordered_list_freq_count = sorted(list_of_freq_count, key = lambda x: -x.value[1])
    
    # Build a tree
    huffman_tree = BinaryTree()

    while len(ordered_list_freq_count) > 1:
        left_node = ordered_list_freq_count.pop()
        right_node = ordered_list_freq_count.pop()
        new_node_created = TreeNode((left_node.value[0]+right_node.value[0], left_node.value[1], right_node.value[1]))
        new_node_created.left = left_node
        new_node_created.right = right_node

        next_iteration = 0
        for index in range(0, len(ordered_list_freq_count)):
            if ordered_list_freq_count[index].value[1] == new_node_created.value[1]:
                ordered_list_freq_count.insert(index, new_node_created)
                next_iteration = 1
                break

        if next_iteration:
            continue
        else:
            ordered_list_freq_count.append(new_node_created)
    
    huffman_tree.root_node = ordered_list_freq_count[0]
    

    if not huffman_tree.root_node.has_left_child() and not huffman_tree.root_node.has_right_child():
        root_node_node = TreeNode(huffman_tree.root_node.value)
        root_node_node.left = huffman_tree.root_node
        root_node_node.right = huffman_tree.root_node
        huffman_tree.root_node = root_node_node
   
    # Convert a Tree to dictionary
    huffman_dictionary = {}

    def traverse_tree(root_node_node, huffman_dictionary, data):
        if not root_node_node.has_left_child() and not root_node_node.has_right_child():
            root_node_node.value = root_node_node.value[0]
            if data == "":
                data = "0"
            huffman_dictionary[root_node_node.value] = data
            return

        if root_node_node is not None:
            traverse_tree(root_node_node.left_child, huffman_dictionary, data + "0")
            traverse_tree(root_node_node.right_child, huffman_dictionary, data + "1")
    
    traverse_tree(huffman_tree.root_node, huffman_dictionary, "")
    print(huffman_dictionary)

    encoded_result = ""
    for character in data:
        encoded_result += huffman_dictionary[character]
    return encoded_result, huffman_tree

def huffman_decoding(data,tree):
    # Decode
    current_node = tree.root_node

    decoded_result = ""
    
    for character in data:
        if character == "0":
            current_node = current_node.left_child
        elif character == "1":
            current_node = current_node.right_child

        if not current_node.has_left_child() and not current_node.has_right_child():
            decoded_result += current_node.value
            current_node = tree.root_node
    return decoded_result

if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
a_great_sentence_one = "Hello positivity"

print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence_one)))
print ("The content of the data is: {}\n".format(a_great_sentence_one))

encoded_data, tree = huffman_encoding(a_great_sentence_one)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

# Test Case 2
a_great_sentence_two = "Winter is coming"
print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence_two)))
print ("The content of the data is: {}\n".format(a_great_sentence_two))

encoded_data, tree = huffman_encoding(a_great_sentence_two)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))

# Test Case 3
a_great_sentence_three = "Progress is exponential in learnig"
print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence_three)))
print ("The content of the data is: {}\n".format(a_great_sentence_three))

encoded_data, tree = huffman_encoding(a_great_sentence_three)

print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
print ("The content of the encoded data is: {}\n".format(encoded_data))

decoded_data = huffman_decoding(encoded_data, tree)

print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
print ("The content of the encoded data is: {}\n".format(decoded_data))