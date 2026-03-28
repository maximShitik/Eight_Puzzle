
import numpy as np

from Tiles import RIGHT,LEFT,UP,DOWN


"""

This module defines the core data structures for the 8-puzzle problem.

Classes:
- Node:
  Represents a search node in the search tree. Stores the current state,
  parent node, action used to reach this state, depth, heuristic value,
  and f-value for informed search.

- EightPuzzle:
  Represents the 8-puzzle problem itself. Includes:
  - the initial state
  - the goal state
  - goal test
  - locating the blank tile (0)
  - finding legal moves
  - applying a move to create a new state

The state is represented as a 3x3 NumPy array.
The blank tile is represented by 0.
Moves are based on shifting the blank tile in one of four directions:
LEFT, RIGHT, UP, DOWN.
"""



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
        self.state = initial_state
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



    def apply_move (self,state,action) -> any:

        curr_blank = self.find_blank_pos(state)
      
        new_state = state.copy()
        new_position = (curr_blank[0] + action[0], curr_blank[1] + action[1])

        new_state[curr_blank], new_state[new_position] = new_state[new_position], new_state[curr_blank]
    
        return new_state


