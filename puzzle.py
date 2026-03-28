
import numpy as np

LEFT = (0,-1)
RIGHT = (0,1)
UP = (-1,0)
DOWN = (1,0)


class Node:
    def __init__(self, state,parent,action ,heuristics=0):
        self.state = state
        self.parent = parent
        self.depth = 0 if not parent else parent.depth + 1
        self.action = action
        self.heuristics = heuristics
        self.f = self.depth + self.heuristics

class EightPuzzle:
    def __init__(self,initial_state,goal):
        self.initial_state = initial_state
        self.goal = goal

    def is_goal(self,state)->bool:
        return np.array_equal(state, self.goal)


    def find_blank_pos(self,state)->tuple:
        pos = np.where(state == 0)
        row = pos[0][0]
        col = pos[1][0]
        return (row,col)

    def get_moves(self,state)->list:

        curr_blank = self.find_blank_pos(state)
        blank_row = curr_blank[0]
        blank_col = curr_blank[1]

        possible_moves = []

        for action in [LEFT, RIGHT, UP, DOWN]:
            new_row = blank_row + action[0]
            new_col = blank_col + action[1]
            
            if 0<= new_row < 3 and 0 <= new_col < 3:
                possible_moves.append(action)
        return possible_moves



    def apply_move (self,state,action):
        pass

    


