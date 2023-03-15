### Backtracking with Examples Such as n-Queen Problem

Backtracking is a general algorithmic technique that considers searching every possible combination in order to solve an optimization problem. Backtracking is also known as depth-first search or branch and bound. Backtracking works in an incremental way and is an optimization over the naive approach.

Backtracking can be applied to solve problems that involve finding all (or some) solutions to a problem that satisfy a given set of constraints. Some examples of such problems are:

- n-Queen problem: Place n queens on an n×n chessboard such that no two queens attack each other.
- Graph coloring problem: Assign colors to the vertices of a graph such that no two adjacent vertices have the same color.
- Hamiltonian cycle problem: Find a cycle that visits every vertex of a graph exactly once.
- Sum of subsets problem: Find all subsets of a given set of integers that sum up to a given value.

The general idea of backtracking is to try different possibilities (branches) until a solution is found, or all possibilities are exhausted. A branch can be rejected (pruned) if it does not satisfy some constraint, or if it leads to a dead end (a partial solution that cannot be extended further).

The pseudocode for backtracking is:

```
backtrack(current_state):
  if current_state is a solution:
    report or store the solution
  else:
    for each possible choice from current_state:
      if the choice is valid:
        make the choice and update current_state
        backtrack(current_state)
        undo the choice and restore current_state
```

The n-Queen problem can be solved using backtracking as follows:

- The current_state is an array of size n that stores the column index of the queen in each row. For example, current_state = [2, 4, 1, 3] means that there is a queen at (0, 2), (1, 4), (2, 1), and (3, 3).
- A solution is found when the current_state has n elements, meaning that n queens have been placed.
- The possible choices are the column indices from 0 to n-1 for the next row.
- The choice is valid if it does not conflict with any of the queens already placed. This can be checked by comparing the row, column, and diagonal distances of the new queen with the existing queens.
- The choice is made by appending the column index to the current_state array.
- The choice is undone by removing the last element from the current_state array.

The pseudocode for n-Queen problem using backtracking is:

```
nQueen(n):
  backtrack([]) # start with an empty state

backtrack(current_state):
  if current_state has n elements:
    report or store current_state as a solution
  else:
    row = current_state.length # the next row to place a queen
    for col from 0 to n-1:
      if col is a valid choice for row:
        current_state.append(col) # make the choice
        backtrack(current_state) # explore further
        current_state.pop() # undo the choice
```

The validity check for col can be implemented as:

```
isValid(current_state, col):
  row = current_state.length
  for i from 0 to row-1:
    if current_state[i] == col: # same column
      return false
    if abs(current_state[i] - col) == abs(i - row): # same diagonal
      return false
  return true
```