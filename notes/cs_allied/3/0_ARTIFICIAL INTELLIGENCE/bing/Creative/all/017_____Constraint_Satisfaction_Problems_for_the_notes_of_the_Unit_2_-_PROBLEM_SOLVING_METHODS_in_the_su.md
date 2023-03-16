# Constraint Satisfaction Problems

- Constraint satisfaction problems (CSPs) are a special subset of search problems that involve finding a solution that satisfies a set of constraints over a set of variables.
- A CSP is defined by three components :
  - A set of variables, each with a domain of possible values.
  - A set of constraints, each specifying a subset of the domain of one or more variables that are allowed or forbidden.
  - A goal test, which checks if a given assignment of values to variables satisfies all the constraints.
- Examples of CSPs include map coloring, sudoku, crossword puzzles, scheduling, and cryptarithmetic .
- CSPs can be solved by using general search algorithms, such as depth-first search or breadth-first search, with some modifications :
  - The state representation is a partial assignment of values to variables, rather than a black box.
  - The successor function assigns a value to an unassigned variable, subject to the constraints.
  - The goal test checks if the current assignment is complete and consistent, i.e., all variables have values and no constraints are violated.
- However, general search algorithms are often inefficient for solving CSPs, as they do not exploit the structure of the problem and generate many redundant or inconsistent states .
- Therefore, CSPs can benefit from using specialized techniques, such as :
  - Backtracking search, which is a depth-first search that prunes the search tree by applying the constraints at each node and backtracks when a dead end is reached.
  - Constraint propagation, which is a process of reducing the domain of variables by enforcing local consistency conditions, such as arc consistency or path consistency.
  - Forward checking, which is a form of constraint propagation that eliminates values from the domains of unassigned variables that are inconsistent with the current assignment.
  - Heuristics, such as the minimum remaining values (MRV) heuristic, which chooses the variable with the fewest legal values, or the least constraining value (LCV) heuristic, which chooses the value that rules out the fewest values in the remaining variables.
  - Local search, which is a search algorithm that starts from a random or greedy assignment and iteratively improves it by changing the value of one or more variables, using methods such as hill climbing, simulated annealing, or genetic algorithms.