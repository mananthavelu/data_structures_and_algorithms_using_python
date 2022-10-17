"""
Trie is a type of tree data structure
Often used for storing the characters; each node can store a character
If we look at the path down to the root; that node is really representing a word or part of the node
Helpful to do quick look up
Validation of words; is one example of application
"""
basic_trie = {'a': {'d': {'d': {'word_end': True},'word_end': False},'word_end': True},
              'h': {'i': {'word_end': True}, 'word_end': False}}

# is implemented using dictionary

print(type(basic_trie))

# consists of the sequence of characters which can be constructed as a path in a tree
print(basic_trie['a'])
print(basic_trie['a']['word_end'])
#print(basic_trie['a']['d']['word_end'])
#print(basic_trie['a']['d']['d']['word_end'])
print("after")
def word_validation(word_input):
    current_node = basic_trie
    for char in word_input:
        print(current_node)
        if char not in current_node:
            return False
        current_node = current_node[char]
        print(current_node)
    return current_node['word_end']
        
        
print(word_validation('ad'))


# Implementation using dictionary and as Class

class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.children = {}

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        """
        Add `word` to trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]

        current_node.is_word = True#Assign that this word is valid

    def exists(self, word):
        """
        Check if word exists in trie
        """
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]

        return current_node.is_word#return True if a word exists or False if it does not
""" 

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

print(people[1]['name'])
print(people[1]['age'])
print(people[1]['sex'])

""" 