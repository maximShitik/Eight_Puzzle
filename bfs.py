from collections import deque
from puzzle import Node
from helper import reconstruct_path , expand

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

        children = expand(node,puzzle)
        for child in children:
            if child.state.tobytes() not in visited:
                if puzzle.is_goal(child.state):
                    path = reconstruct_path(child)
                    return path, child.depth, expanded_counter
                queue.append(child)
                visited.add(child.state.tobytes())
    return None, 0, expanded_counter
            

