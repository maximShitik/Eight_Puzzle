from collections import deque
from puzzle import Node


def BFS(puzzle,initial_state):
    queue = deque()
    visited = set()
    node = Node(initial_state,parent=None,moved=None)
    queue.append(node)
    visited.add(node.state.tobytes())
    expanded_counter = 0

    while queue:
        
        node = queue.popleft()
        expanded_counter +=1

        moves = puzzle.get_moves(node.state)

        curr_blank = puzzle.find_blank_pos(node.state)
        blank_row = curr_blank[0]
        blank_col = curr_blank[1]

        for move in moves:
            new_state = puzzle.apply_move(node.state,move)
            if new_state.tobytes() not in visited:
                tile_moved = node.state[blank_row + move[0], blank_col + move[1]]
                new_node = Node(new_state,node,tile_moved)
                if puzzle.is_goal(new_state):
                    path = reconstruct_path(node)
                    return path, node.depth, expanded_counter
                queue.append(new_node)
                visited.add(new_state.tobytes())

def reconstruct_path(node):
    path_list = []

    while node.parent:
        path_list.append(node.moved)
        node = node.parent
    return path_list[::-1]