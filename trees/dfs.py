

class Tree():
    def __init__(self, value=None):
        self.root = Node(value)
        
    def get_root(self):
        return self.root

# Create a Node
class Node:
  def __init__(self, value = None):
    self.value = value
    self.left = None
    self.right = None
  
  def set_value(self, new_value):
    self.value = new_value

  def get_value(self):
    return self.value
  
  def set_left_child(self, node):
    self.left = node

  def set_right_child(self, node):
    self.right= node

  def get_left_child(self):
    return self.left
  
  def get_right_child(self):
    return self.right

  def has_left_child(self):
    return self.left != None

  def has_right_child(self):
    return self.right != None

  def __repr__(self):
    return f"Node({self.get_value()})" 


class Stack:
  def __init__(self):
    self.stack = list()
  
  def append(self, value):
    new_node = Node(value)
    self.stack.append(new_node)
  
  def pop(self):
    if self.stack is self.is_empty():
      raise  Exception('The stack is empty')
    else:
      return self.stack.pop()
  
  def is_empty(self):
    return len(self.stack) != 0


class BinaryTree:
  def __init__(self, value = None):
    self.root = Node(value)

  def get_root(self):
    return self.root

  def __repr__(self):
    return f"{self.root.value}"

  def traverse_pre_order_recursive(self):
      if self.root is None:
        return []

      output = []
      return self.recursive_call(self.root, output)
    
  def recursive_call(self, node, output):
    if node is not None:
      output.append(node.value)
      self.recursive_call(node.get_left_child(), output)
      self.recursive_call(node.get_right_child(), output)
    return output

  def traverse_pre_order_stack(self):
    if self.root is None:
        return []
    visited_nodes = []
    stack_ds = []
    stack_ds.append(self.root)
    while stack_ds:
      root_node = stack_ds.pop()
      if root_node is not None:
        visited_nodes.append(root_node.value)
        if root_node.has_left_child():
          stack_ds.append(root_node.get_left_child())
        elif root_node.has_right_child():
          stack_ds.append(root_node.get_right_child())
    return visited_nodes


  def preorderTraversal(self):
"""
    :type root: TreeNode
    :rtype: List[int]
    """
    if self.root is None:
        return []
    
    stack, output = [self.root, ], []
    
    while stack:
        root = stack.pop()
        if root is not None:
            output.append(root.value)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)
    return output
  # create a tree and add some nodes
tree = BinaryTree("apple")
print(tree)
tree.get_root().set_left_child(Node("banana"))
print(tree.get_root().get_left_child())
tree.get_root().set_right_child(Node("cherry"))
print(tree.get_root().get_right_child())
tree.get_root().get_left_child().set_left_child(Node("dates"))


print(" traverse_pre_order_stack", tree.traverse_pre_order_stack())
print(" preorderTraversal", tree.preorderTraversal())
print(" traverse_pre_order_recursive", tree.traverse_pre_order_recursive())

