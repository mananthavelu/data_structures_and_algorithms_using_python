
from helpers import Map, load_map, show_map
from student_code import shortest_path


def cum_distance(Map, node1, node2):
    """
    Calculates the distance between to given nodes in the map
    """
    import math
    
    x1 = Map.intersections[node1][0]
    y1 = Map.intersections[node1][1]
    x2 = Map.intersections[node2][0]
    y2 = Map.intersections[node2][1]
    
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)
def shortest_path(Map, start, goal):
    """
    
    Finds the shortest possible path using A* algorithm
    """
    import heapq
    
    explored_nodes = set()# Keep track of the nodes explored in a map
    shortest_path = [] # 
    list_of_paths = []
    initial_path = [start]
    start_path_cost = 0
    start_path_cum_distance = cum_distance(Map, start, goal)
    start_total_cost = start_path_cost + start_path_cum_distance
    
    start_record = [start_total_cost, start_path_cost, start_path_cum_distance, initial_path]
    
    heapq.heappush(list_of_paths, start_record)
    
    while len(list_of_paths) > 0:
        
        current_record = heapq.heappop(list_of_paths)
        current_path = current_record[3]
        current_path_cost = current_record[1]
        current_node = current_record[3][-1]
        explored_nodes.add(current_node)
        
        
        # Check if a node is final goal node
        if current_node == goal:
            path = current_path
            break
            
        # Extend the path from the current node
        for new_node in Map.roads[current_node]:
            if new_node not in explored_nodes:
                new_path = current_path + [new_node]
                new_path_cost = current_path_cost + cum_distance(Map, current_node, new_node)
                new_distance = cum_distance(Map, new_node, goal)
                new_total_cost = new_path_cost + new_distance
                new_record = [new_total_cost, new_path_cost, new_distance, new_path]
                heapq.heappush(list_of_paths, new_record)
                
    return path

path = shortest_path(map_40, 5, 34)
if path == [5, 16, 37, 12, 34]:
    print("great! Your code works for these inputs!")
else:
    print("something is off, your code produced the following:")
    print(path)