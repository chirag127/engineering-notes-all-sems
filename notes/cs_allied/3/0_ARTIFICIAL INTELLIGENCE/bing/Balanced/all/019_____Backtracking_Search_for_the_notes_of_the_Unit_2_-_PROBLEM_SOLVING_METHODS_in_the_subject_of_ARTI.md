# Backtracking Search

- Backtracking search is a technique for solving constraint satisfaction problems (CSPs), which are problems where the goal is to find an assignment of values to a set of variables that satisfies a set of constraints.
- A CSP can be represented by a set of variables, a set of domains for each variable, and a set of constraints that specify the allowed combinations of values for some subset of variables.
- A solution to a CSP is a complete assignment of values to all variables that satisfies all constraints.
- Backtracking search is a recursive algorithm that tries to find a solution by assigning values to variables one by one, and checking if the assignment is consistent with the constraints.
- If the assignment is consistent, the algorithm moves on to the next variable. If the assignment is inconsistent, the algorithm backtracks to the previous variable and tries a different value.
- The algorithm terminates when either a solution is found or all possible assignments have been tried and none of them is consistent.
- Backtracking search can be improved by using various heuristics, such as:
  - Variable ordering: choosing the next variable to assign based on some criteria, such as the minimum remaining values (MRV) heuristic, which selects the variable with the fewest legal values left in its domain.
  - Value ordering: choosing the next value to assign based on some criteria, such as the least constraining value (LCV) heuristic, which selects the value that rules out the fewest values in the domains of the remaining variables.
  - Forward checking: keeping track of the remaining legal values for unassigned variables and pruning the domains of the variables that are affected by each assignment.
  - Arc consistency: enforcing a stronger form of consistency that ensures that for every pair of variables that share a constraint, there is at least one legal value for each variable that satisfies the constraint.
  - Backjumping: backtracking to the most recent variable that caused a failure, rather than the previous one, and skipping the values that have already been tried.