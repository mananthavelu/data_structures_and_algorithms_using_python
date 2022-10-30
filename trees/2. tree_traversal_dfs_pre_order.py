# DFS

# Traversing: 'Visiting' all the nodes once
# is used for searching a value, inserting a value and deleting the node

# DFS:  Priority to the nodes with childrens first
# Pre-Order Traversal: root, left, right
# In- Order Traversal: left, root, right
# Post - Order Traversal: left, right, root


"""
Pre-Order

-We visit Root
-We check if there is left child: is Yes-> visit (and so on)-> And check if it has left child-> visit
-We check if there is a right child: visit


Detailed Steps: 
1. Initialize Stack
2. Add root node to Stack, add to visited nodes
3. Add left node to Stack, add to visited nodes


DFS uses Stack
"""

# Stack consists of two main operations: push and pop
# This implementation is directly using list - which acts similar to dynamic array

class Stack:
    def __init__(self):
        self.items = []
        
    def size(self):
        return len(self.items)
    
    def push(self, new_data):
        self.items.append(new_data)
        return

    def pop(self):
        if self.size() == 0:
            return None
        return self.items.pop()
    
    def top(self):
        if len(self.items) > 0:
            return self.items[-1]
        else:
            return None
    def is_empty(self):
        return len(self.items) == 0
    
    
    def __repr__(self):
        if len(self.items) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.items[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"
# Tree contains Node class

class TreeNode:
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None
        
    # Set the value of the tree node
    def set_value(self, new_data):
        self.data = new_data
        
    # Get the value of the tree node
    def get_value(self):
        return self.data
    
    # Set the value of the left child
    def set_left_child(self, left_child_value):
        self.left = left_child_value
    
    # Set the value of the right child
    def set_right_child(self, right_child_value):
        self.right = right_child_value
        
    # Get the value of the left child
    def get_left_child(self):
        return self.left
    
    # Get the value of the left child
    def get_right_child(self):
        return self.right
    
    # Check if the left child exists
    def has_left_child(self):
        return self.left is not None
    
    # Check if the right child exists
    def has_right_child(self):
        return self.right != None
    
    def __repr__(self):
        return f"Node({self.get_value()})"
    
    def __str__(self):
        return f"Node({self.get_value()})"
    
class Tree:
    def __init__(self, root = None):
        self.root = TreeNode(root)
        
    # Get the root node
    def get_root(self):
        return self.root

class State:
    def __init__(self, node):
        self.node = node
        self.left_visited = False
        self.right_visited = False
        
    def set_left_visited(self):
        self.left_visited = True
    
    def set_right_visited(self):
        self.right_visited = True

    def get_left_visited(self):
        return self.left_visited
    
    def get_right_visited(self):
        return self.right_visited
    
    def get_node(self):
        return self.node

    def __repr__(self):
        s = f"""{self.node} visited_left: {self.left_visited} visited_right: {self.right_visited}"""
        return s

# In the pre-order traversal
def pre_order_traversal(input_tree, debug_mode = False):
    stack = Stack()
    visiting_order = []
    node = input_tree.get_root()
    state = State(node)
    stack.push(state)
    visiting_order.append(node.get_value())
    count = 0
    while node:
        count += 1
        if debug_mode:
            print(f"""current node:{node}, stack: {stack}""")
        if node.has_left_child() and not state.get_left_visited():
            state.set_left_visited()
            node = node.get_left_child()
            visiting_order.append(node.get_value())
            state = State(node)
            stack.push(state)
        elif node.has_right_child() and not state.get_right_visited():
            state.set_right_visited()
            node = node.get_right_child()
            visiting_order.append(node.get_value())
            state = State(node)
            #stack.push(state)
        else:
            stack.pop()
            if not stack.is_empty():
                state = stack.top()
                node = state.get_node()
            else:
                node = None
    if debug_mode:
        print(f"""current node:{node}, stack: {stack}""")
    return visiting_order


            
# create a tree and add some nodes
tree = Tree("apple")  # root node

# set first level's left child
tree.get_root().set_left_child(TreeNode("banana"))  

# set first level's right child
tree.get_root().set_right_child(TreeNode("cherry"))  

# set second level's left child 
# by getting the first level's left child first
tree.get_root().get_left_child().set_left_child(TreeNode("dates"))

# check pre-order traversal

print(pre_order_traversal(tree, debug_mode= True))
    
# Troubleshoot why 3 times the dates are appearing