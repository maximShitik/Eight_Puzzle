def liniar_conflict():
    pass



def manhattan_distance(state):
    total = 0
    for row in range(3):
        for col in range(3):
            tile = state[row][col]
            if tile !=0:
                goal_row = tile // 3
                goal_col = tile % 3
                
                total += abs(row - goal_row) + abs(col - goal_col)
    return total


