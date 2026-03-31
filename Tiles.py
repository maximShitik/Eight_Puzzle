import sys
import numpy as np
from puzzle import EightPuzzle
from bfs import BFS
from a_star import aStar

def print_results(algo_name,path,length,expanded):
    print(f"Algorithm:{algo_name}\nPath: {' '.join(str(tile) for tile in path)}\nLength: {length}\nExpanded: {expanded}")

GOAL = [0,1,2,3,4,5,6,7,8]
if __name__ == "__main__":
    numbers = sys.argv[1:]

    numbers = [int(x) for x in numbers]
    initial_state  = np.array(numbers,dtype=np.uint8).reshape(3,3)

    goal_state = np.array(GOAL, dtype=np.uint8).reshape(3,3)
    puzzle = EightPuzzle(initial_state,goal_state)

    path, length, expanded = BFS(puzzle, initial_state)
    path_2, length_2, expanded_2 = aStar(puzzle, initial_state)


    print_results("BFS",path,length,expanded)
    print_results("A*",path_2,length_2,expanded_2)
