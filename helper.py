from puzzle import Node


def reconstruct_path(node):
    path_list = []

    while node.parent:
        path_list.append(node.moved)
        node = node.parent
    return path_list[::-1]


def expand(node, puzzle,heuristic=None):
    children = []
    moves = puzzle.get_moves(node.state)
    curr_blank = puzzle.find_blank_pos(node.state)
    
    for move in moves:
        new_state = puzzle.apply_move(node.state, move)
        tile_moved = int(node.state[curr_blank[0] + move[0], 
                                    curr_blank[1] + move[1]])
        h = heuristic(new_state) if heuristic else 0
        new_node = Node(new_state, node, tile_moved, heuristics=h)
        children.append(new_node)
    
    return children