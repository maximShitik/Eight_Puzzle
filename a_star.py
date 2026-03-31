import heapq
from puzzle import Node
from heuristics import liniar_conflict, manhattan_distance
from helper import reconstruct_path



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
        
        moves = puzzle.get_moves(node.state)
        curr_blank = puzzle.find_blank_pos(node.state)
        blank_row = curr_blank[0]
        blank_col = curr_blank[1]

        for move in moves:
            new_state = puzzle.apply_move(node.state, move)
            if new_state.tobytes() not in visited:
                tile_moved = node.state[blank_row + move[0], blank_col + move[1]]
                new_node = Node(new_state, node, tile_moved, heuristics=liniar_conflict(new_state))
                heapq.heappush(queue, (new_node.f, counter, new_node))
                counter += 1
        
