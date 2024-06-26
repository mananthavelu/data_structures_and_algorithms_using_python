# Write a code to traverse a tree in in-order fashion   
def in_order_traversal(tree):
    stack = Stack()
    current_node = tree.get_root() # We alwayss tart with root
    visited_nodes = []
    while current_node or not stack.is_empty():
        while current_node:
            stack.push(current_node)
            current_node =current_node.get_left_child()

        current_node = stack.pop()
        visited_nodes.append(current_node.get_value())
        current_node = current_node.get_right_child()
    return visited_nodes                                                                                                                          
