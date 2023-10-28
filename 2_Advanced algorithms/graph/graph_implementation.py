# Implement a graph

class GraphNode():
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, new_node):
        self.children.append(new_node)

    def remove_child(self, del_child):
        if del_child in self.children:
            self.children.remove(del_child)

class Graph():
    def __init__(self, node_list):
        self.nodes = node_list

    def add_edge(self, node_one, node_two):
        if (node_one in self.nodes and node_two in self.nodes):
            node_one.add_child(node_two)
            node_two.add_child(node_one)
        
    def remove_edge(self, node_one, node_two):
        if (node_one in self.nodes and node_two in self.nodes):
            node_one.remove_child(node_two)
            node_two.remove_child(node_one)


# Create Nodes objects for a Graph

nodeG = GraphNode('G')
nodeR = GraphNode('R')
nodeA = GraphNode('A')
nodeP = GraphNode('P')
nodeH = GraphNode('H')
nodeS = GraphNode('S')

# Create a Graph object

graph1 = Graph([nodeS,nodeH,nodeG,nodeP,nodeR,nodeA] ) 
graph1.add_edge(nodeG,nodeR)
graph1.add_edge(nodeA,nodeR)
graph1.add_edge(nodeA,nodeG)
graph1.add_edge(nodeR,nodeP)
graph1.add_edge(nodeH,nodeG)
graph1.add_edge(nodeH,nodeP)
graph1.add_edge(nodeS,nodeR)

# Implementation of Depth First Search in Graphs

def dfs_search(start_node, search_value):
    stack = [start_node]
    
    while len(stack) > 0:
        node = stack.pop()
        
        if node.value == search_value:
            return start_node
        
        for child in node.children:
             if (child not in visited) and (child not in stack):
                stack.append(child)