def reconstruct_path(node):
    path_list = []

    while node.parent:
        path_list.append(node.moved)
        node = node.parent
    return path_list[::-1]