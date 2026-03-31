
"""
Heuristic Functions for the 8-Puzzle Problem
==========================================

This module implements heuristic functions used to evaluate states in the 8-puzzle problem.
The main heuristic implemented is the Linear Conflict heuristic, which is an enhancement
of the Manhattan Distance heuristic.

Overview
--------
The 8-puzzle is a sliding puzzle consisting of a 3x3 grid with tiles numbered 1 - 8 and one empty tile (0).
The goal is to transform a given initial state into a goal state using the minimum number of moves.

Heuristics
----------

1. Manhattan Distance
---------------------
The Manhattan Distance heuristic computes the sum of the distances of each tile from its
goal position. The distance is measured as:

    |current_row - goal_row| + |current_col - goal_col|

This heuristic is admissible and consistent.

2. Linear Conflict
------------------
The Linear Conflict heuristic improves upon Manhattan Distance by detecting additional constraints.

A linear conflict occurs when:
- Two tiles are in the same row (or column),
- Both belong in that row (or column) in the goal state,
- But their relative order is reversed.

In such a case, at least two additional moves are required to resolve the conflict.

Therefore, the heuristic is defined as:

    h(n) = Manhattan Distance
           + 2 * (number of row conflicts)
           + 2 * (number of column conflicts)

This heuristic is:
- Admissible (never overestimates the true cost)
- More informed than Manhattan Distance alone
- Suitable for use in A* search

Functions
---------

liniar_conflict(state)
    Computes the total heuristic value combining Manhattan Distance and linear conflicts.

manhattan_distance(state)
    Computes the sum of Manhattan distances for all tiles.

count_row_conflicts(state)
    Counts the number of linear conflicts within rows.

count_col_conflicts(state)
    Counts the number of linear conflicts within columns.

State Representation
--------------------
The state is represented as a 3x3 matrix (NumPy array or list of lists),
where:
    - Numbers 1-8 represent tiles
    - 0 represents the empty space

Example:
--------
    [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 0]]


Notes
-----
- The heuristic assumes the standard goal configuration.
- Tile '0' (empty space) is ignored in all calculations.
"""

def liniar_conflict(state):
    total = manhattan_distance(state)
    total += 2 * count_row_conflicts(state)
    total += 2 * count_col_conflicts(state)
    return total

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


def count_row_conflicts(state):
    sum = 0
    for row in range(3):
        curr_row = []
        for col in range(3):
            tile = state[row][col]
            if tile !=0:
                goal_row = tile // 3
                if row == goal_row:
                    curr_row.append(tile)
    
        for i in range(len(curr_row)):
             for j in range(i+1, len(curr_row)):
               if curr_row[i] > curr_row[j]:
                  sum += 1
    return sum

def count_col_conflicts(state):
    sum = 0
    for col in range(3):
        curr_col = []
        for row in range(3):
            tile = state[row][col]
            if tile !=0:
                goal_col = tile % 3
                if col == goal_col:
                    curr_col.append(tile)
    
        for i in range(len(curr_col)):
             for j in range(i+1, len(curr_col)):
               if curr_col[i] > curr_col[j]:
                  sum += 1
    return sum