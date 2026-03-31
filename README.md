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
  - Contains:
    - `reconstruct_path(node)` – reconstructs the solution path from the goal node back to the start node
    - `expand(node, puzzle, heuristic=None)` – generates all valid successor nodes from a given state, and optionally computes heuristic values for informed search

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
[[1, 4, 0],
 [5, 8, 2],
 [3, 6, 7]]
```

#### Manhattan Distance

We compute the distance of each tile from its goal position:

- Tile 1 → (0,0) → goal (0,1) → distance = 1  
- Tile 4 → (0,1) → goal (1,1) → distance = 1  
- Tile 5 → (1,0) → goal (1,2) → distance = 2  
- Tile 8 → (1,1) → goal (2,2) → distance = 2  
- Tile 2 → (1,2) → goal (0,2) → distance = 1  
- Tile 3 → (2,0) → goal (1,0) → distance = 1  
- Tile 6 → (2,1) → goal (2,0) → distance = 1  
- Tile 7 → (2,2) → goal (2,1) → distance = 1  

Total Manhattan Distance:

```
h = 1 + 1 + 2 + 2 + 1 + 1 + 1 + 1 = 10
```

---

#### Linear Conflicts

- **Row 2**: tiles [3, 6, 7] all belong in this row  
  Their correct order should be [6, 7, 8], but:
  - 6 appears after 3 → conflict
  - 7 appears after 6 → conflict  
  → 2 conflicts

- **Column 1**: tiles [4, 8, 6] belong in this column  
  Their correct order should be [3, 4, 5], but:
  - 8 and 6 are reversed  
  → 1 conflict

Total conflicts = 3

Each conflict adds +2:

```
2 × 3 = 6
```

---

#### Final Heuristic Value

```
h(n) = Manhattan + Linear Conflict
     = 10 + 6
     = 16
```

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
