import heapq
from puzzle import Node
from heuristics import liniar_conflict, manhattan_distance
from helper import reconstruct_path , expand



def aStar(puzzle,initial_state):
    queue = []
    visited = set()
    counter = 0
    expanded_counter = 0

    node = Node(initial_state,parent=None,moved=None,heuristics=liniar_conflict(initial_state))
    heapq.heappush(queue, (node.f, counter, node))
    counter += 1
    
    while queue:
        _, _, node = heapq.heappop(queue)

        if node.state.tobytes() in visited:
            continue

        visited.add(node.state.tobytes())

        if puzzle.is_goal(node.state):  
            path = reconstruct_path(node)
            return path, node.depth, expanded_counter
        
        expanded_counter += 1
        children = expand(node,puzzle,heuristic=liniar_conflict)
        for child in children:
            if child.state.tobytes() not in visited:
                heapq.heappush(queue, (child.f, counter, child))
                counter += 1
        
