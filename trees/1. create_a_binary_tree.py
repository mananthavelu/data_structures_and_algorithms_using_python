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