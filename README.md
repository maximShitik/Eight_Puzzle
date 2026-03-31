# 8-Puzzle Solver  
**Author: Maxim Shitik**

---

## 1. General Description of the Program

This program implements a solver for the 8-puzzle problem using two search algorithms:

- Breadth-First Search (BFS)
- A* Search (A*)

### Structure and Components

The system is composed of several modules:

- **main.py**
  - Handles input from command line arguments
  - Initializes the puzzle
  - Runs both BFS and A* algorithms
  - Prints results (path, length, expanded nodes)

- **puzzle.py**
  - Contains core classes:
    - `Node` – represents a search node (state, parent, depth, heuristic, f-value)
    - `EightPuzzle` – defines the problem (goal test, moves, transitions)

- **bfs.py**
  - Implements Breadth-First Search using a queue (`deque`)
  - Uses a `visited` set to avoid revisiting states

- **a_star.py**
  - Implements A* search using a priority queue (`heapq`)
  - Uses `f(n) = g(n) + h(n)`

- **heuristics.py**
  - Implements:
    - Manhattan Distance - Artificial Intelligence a modern Approach 4th edition page 116.
    - Linear Conflict heuristic - https://www.cse.sc.edu/~mgv/csce580sp15/gradPres/HanssonMayerYung1992.pdf or https://youtu.be/8t3lPD2Qtao?si=H2hDI_KZBXNAl3Xw

- **helper.py**
  - Contains `reconstruct_path` to extract the solution path

### Data Structures Used

- Queue (`deque`) – BFS
- Priority Queue (`heapq`) – A*
- Set – visited states
- NumPy arrays – state representation
- Tree structure via `Node` class

---

## 2. Problem Representation

### State Representation

Each state is represented as a 3×3 NumPy array:

```
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 0]]
```

- Numbers 1–8 represent tiles
- 0 represents the blank tile

States are stored and compared using `state.tobytes()` for hashing.

---

### Actions

The possible actions are movements of the blank tile:

- LEFT  → (0, -1)
- RIGHT → (0, 1)
- UP    → (-1, 0)
- DOWN  → (1, 0)

---

### Transition Model

- The blank tile is located
- A legal move is selected
- The blank is swapped with the adjacent tile
- A new state is generated

This is implemented in:

```
apply_move(state, action)
```

---

## 3. Heuristic Description

### Manhattan Distance

The Manhattan Distance heuristic computes:

```
h(n) = Σ |row - goal_row| + |col - goal_col|
```

for each tile.

It is:
- Admissible
- Consistent

---

### Linear Conflict Heuristic

The Linear Conflict heuristic improves Manhattan Distance.

A conflict occurs when:
- Two tiles are in the same row/column
- Both belong in that row/column in the goal
- Their order is reversed

Each conflict requires at least 2 additional moves.

Therefore:

```
h(n) = Manhattan Distance
       + 2 × (# row conflicts)
       + 2 × (# column conflicts)
```

---

### Example Calculation

For a given state:

```
[[2, 1, 3],
 [4, 5, 6],
 [7, 8, 0]]
```

- Manhattan Distance = 2 (tiles 1 and 2 misplaced)
- Linear conflict between 2 and 1 in row 0 → +2

Total:

```
h(n) = 2 + 2 = 4
```

---

### Consistency

Both Manhattan Distance and Linear Conflict are:

- Admissible (never overestimate)
- Consistent (triangle inequality holds)

Therefore, they guarantee optimality in A*.

---

## 4. Optimality of the Algorithms

### BFS (Breadth-First Search)

  Optimal **only when all step costs are equal**

- BFS explores nodes level by level
- In the 8-puzzle, each move has cost = 1
- Therefore BFS always finds the shortest path (minimum number of moves)

---

### A* Search

 Optimal **if the heuristic is admissible (and consistent)**

In this implementation:

- Heuristic = Manhattan Distance (or Linear Conflict)
- Both are admissible and consistent

Therefore:

    A* is optimal  
    A* finds the shortest path  

---

### Comparison

| Algorithm | Optimal | Condition |
|----------|--------|----------|
| BFS      | Yes    | Equal step cost |
| A*       | Yes    | Admissible heuristic |

---

## Summary

- The program solves the 8-puzzle using BFS and A*
- States are represented using NumPy arrays
- BFS guarantees optimal solutions with uniform costs
- A* uses heuristics to improve efficiency
- Manhattan and Linear Conflict heuristics ensure optimality

---
