
class RouteTrie:

    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root_node = '/'
        self.children = {}
        self.handler = None
