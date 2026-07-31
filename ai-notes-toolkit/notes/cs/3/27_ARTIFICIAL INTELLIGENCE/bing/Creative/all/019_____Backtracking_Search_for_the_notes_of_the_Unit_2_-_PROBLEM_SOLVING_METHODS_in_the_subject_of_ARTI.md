# Backtracking Search

Backtracking search is a general algorithm for finding solutions to some computational problems, especially constraint satisfaction problems (CSPs), that incrementally builds candidates to the solutions, and abandons a candidate (“backtracks”) as soon as it determines that the candidate cannot possibly be completed to a valid solution.

## Basic Idea of Backtracking Search

- A CSP consists of a set of variables, each with a domain of possible values, and a set of constraints that restrict the values that the variables can take simultaneously.
- A solution to a CSP is an assignment of values to all the variables that satisfies all the constraints.
- Backtracking search searches a space of consistent partial assignments to variables, in the sense that all constraints among instantiated variables are satisfied, and looks for a complete consistent assignment to the variables, or in other words a solution .
- Backtracking search is a depth-first search (DFS) with single-variable assignments for a CSP.
- Backtracking search can be implemented as a recursive procedure that tries all possible values for one variable at a time until a solution is found or all possibilities are exhausted.
- If a variable has no legal values left to assign, the algorithm backtracks to the previous variable and tries a different value for it. This process is repeated until a solution is found or all values for all variables are tried.

## Pseudocode of Backtracking Search

```
function BACKTRACKING-SEARCH(csp) returns a solution or failure
  return BACKTRACK({}, csp)

function BACKTRACK(assignment, csp) returns a solution or failure
  if assignment is complete then return assignment
  var ← SELECT-UNASSIGNED-VARIABLE(csp)
  for each value in ORDER-DOMAIN-VALUES(var, assignment, csp) do
    if value is consistent with assignment according to csp then
      add {var = value} to assignment
      result ← BACKTRACK(assignment, csp)
      if result ≠ failure then return result
      remove {var = value} from assignment
  return failure
```

## Heuristics for Backtracking Search

- Heuristics are used to improve the efficiency of backtracking search by reducing the size of the search space and the number of backtracks.
- Heuristics can be applied to select the next variable to assign, the order of the values to try for each variable, and the inference to perform at each step of the search.
- Some common heuristics are:

  - Minimum remaining values (MRV): choose the variable with the fewest legal values left in its domain.
  - Degree heuristic: break ties among MRV variables by choosing the one that is involved in the largest number of constraints on other unassigned variables.
  - Least constraining value (LCV): order the values of a variable by the number of constraints they impose on other unassigned variables, and choose the one that imposes the least constraints.
  - Forward checking: keep track of the remaining legal values for unassigned variables and prune the values that are inconsistent with the assignment of the current variable.
  - Arc consistency: ensure that for every binary constraint between two variables, every value in the domain of one variable has a consistent value in the domain of the other variable.

## Applications of Backtracking Search

- Backtracking search is used in various applications, including:

  - The N-queen problem: place N queens on an N×N chessboard such that no two queens attack each other.
  - The knight tour problem: find a sequence of moves of a knight on a chessboard such that the knight visits every square only once.
  - Maze solving problems: find a path from a starting point to a goal point in a maze with obstacles.
  - The search for all Hamilton paths in a graph: find all paths in a graph that visit each vertex exactly once.
  - Sudoku puzzles: fill in a 9×9 grid with digits so that each row, column, and 3×3 subgrid contains all of the digits from 1 to 9.