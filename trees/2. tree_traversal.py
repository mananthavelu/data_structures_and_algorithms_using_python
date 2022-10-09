# DFS

# Traversing: 'Visiting' all the nodes once

# DFS:  Priority to the nodes with childrens first
# Pre-Order Traversal: root, left, right
# In- Order Traversal: left, root, right
# Post - Order Traversal: left, right, root


"""
Pre-Order

We visit Root
We check if there is left child: is Yes-> visit (and so on)-> And check if it has left child-> visit
We check if there is a right child: visit


Detailed Steps: 
1. Initialize Stack
2. Add root node to Stack, add to visited nodes
3. Add left node to Stack, add to visited nodes


DFS uses Stack
"""
# Tree contains Node class

class TreeNode:
    def __init__(self, data = None):
        self.data = data
        self.left = left
        self.right = right
        
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
    def check_left_child(self):
        return self.left is not None
    
    # Check if the right child exists
    def check_left_child(self):
        return self.right != None
    
    
class Tree:
    def __init__(self, root = None):
        self.root = TreeNode(root)
        
    # Get the root node
    def get_root(self):
        return self.root
    
    
class PreOrderTree_Traversal:
    