
class RouteTrie:

    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root_node = '/'
        self.children = {}
        self.handler = None
    
    
    def insert(self, paths, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_path = self.children
        _paths = paths.split('/')
        print(_paths)
        # Moving to leaf node
        for path in _paths:
            current_path.insert(RouteTrieNode(path))
            current_path = current_path.children[path]
        current_path.handler = handler


    def find(self, paths):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        if paths == '/':
            return self.handler
        paths_parts = paths.split('/')

        for path in paths_parts:
            _current = self
            for sub_path in path:
                _current = _current.children
                _current = _current[sub_path]
            handler = _current.handler

    def __repr__(self):
        return f"{self.handler} {self.root_node}"

"""
Trie_example = RouteTrie()
print(RouteTrie())
"""


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, value=""):
        # Initialize the node with children as before, plus a handler
        self.value = value
        self.children = {}
        self.handler = None

    def insert(self, next_path, handler=None):
        # Insert the node as before
        self.children[next_path] = self.children.get(next_path, RouteTrieNode(next_path))
        self.children[next_path].handler = handler


#Test cases


# Here are some test cases and expected outputs you can use to test your implementation

# create the router and add a route
router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
router.add_handler("/home/about", "about handler")  # add a route
router.add_handler("/home/about/team", "about team")  # add a route


# some lookups with the expected output
print(router.lookup("/"))  # should print 'root handler'
print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about"))  # should print 'about handler'
print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one
print(router.lookup("/home/about/team"))
