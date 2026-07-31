# Backtracking Search

Backtracking search is a general algorithm for finding solutions to some computational problems, especially constraint satisfaction problems (CSPs). A CSP is a problem where a set of variables must be assigned values from a given domain, subject to some constraints that restrict the possible combinations of values. For example, the n-queens problem is a CSP where n variables represent the positions of n queens on a chessboard, and the constraints are that no two queens can attack each other.

Backtracking search works by incrementally building candidates to the solutions, and abandoning a candidate (backtracking) as soon as it determines that the candidate cannot possibly be completed to a valid solution. The algorithm maintains a partial assignment of values to variables, and tries to extend it by assigning a value to an unassigned variable. If the assignment is consistent with the constraints, the algorithm recurses on the remaining variables. If the assignment is inconsistent, or if there are no more values to try, the algorithm backtracks and tries a different value for the previous variable.

The basic backtracking search algorithm can be improved by using various heuristics, such as:

- Variable ordering: choosing which variable to assign next, based on some criteria such as the minimum remaining values (MRV) heuristic, which picks the variable with the fewest legal values left.
- Value ordering: choosing which value to assign to a variable, based on some criteria such as the least constraining value (LCV) heuristic, which picks the value that rules out the fewest values for the remaining variables.
- Forward checking: keeping track of the remaining legal values for unassigned variables, and pruning them whenever a variable is assigned.
- Arc consistency: enforcing a stronger form of consistency between pairs of variables, such that for every value of one variable, there is at least one consistent value for the other variable.
- Backjumping: backtracking to the most recent variable that caused the failure, rather than the previous one, and skipping the values that are inconsistent with the current assignment.

Backtracking search is a complete and optimal algorithm for solving CSPs, meaning that it will find all solutions if they exist, and the solutions will satisfy the constraints. However, it is also an exponential algorithm in the worst case, meaning that the time and space complexity can grow exponentially with the size of the problem. Therefore, backtracking search is not feasible for large or complex CSPs, and other methods such as local search or approximation algorithms may be preferred.