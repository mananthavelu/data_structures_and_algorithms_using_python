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
    return f"{self.get_value()}" 