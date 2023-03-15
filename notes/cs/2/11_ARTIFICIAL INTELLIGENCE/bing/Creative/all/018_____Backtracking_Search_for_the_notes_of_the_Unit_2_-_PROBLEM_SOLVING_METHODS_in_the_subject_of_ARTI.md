# Backtracking Search

Backtracking search is a general algorithm for finding solutions to some computational problems, notably constraint satisfaction problems (CSPs), that incrementally builds candidates to the solutions, and abandons a candidate (“backtracks”) as soon as it determines that the candidate cannot possibly be completed to a valid solution.

## Basic Idea of Backtracking Search

- A CSP consists of a set of variables, each with a domain of possible values, and a set of constraints that restrict the values that the variables can take simultaneously.
- A solution to a CSP is an assignment of values to all the variables that satisfies all the constraints.
- Backtracking search starts with an empty assignment and tries to extend it by assigning values to one variable at a time.
- If the current assignment is consistent with all the constraints, the algorithm recursively tries to extend the assignment to the next variable.
- If the current assignment violates any constraint, the algorithm backtracks to the previous variable and tries a different value.
- The algorithm terminates when either a complete assignment is found or all the values for a variable have been exhausted.

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
- Some common heuristics are:

  - Variable ordering: choosing which variable to assign next. For example, the minimum remaining values (MRV) heuristic selects the variable with the fewest legal values in its domain, breaking ties by the degree heuristic, which selects the variable with the most constraints on the remaining variables.
  - Value ordering: choosing which value to assign to a variable. For example, the least constraining value (LCV) heuristic selects the value that rules out the fewest values in the domains of the neighboring variables.
  - Forward checking: keeping track of the remaining legal values for unassigned variables and pruning the domains of the variables that are affected by the current assignment. If any variable has an empty domain, the algorithm backtracks immediately.
  - Arc consistency: enforcing a stronger form of consistency that ensures that for every value in the domain of a variable, there exists a consistent value in the domain of every neighboring variable. This can be done by applying the AC-3 algorithm before or during the search.

## Advantages and Disadvantages of Backtracking Search

- Advantages:

  - It is a complete and optimal algorithm for solving CSPs, meaning that it will find a solution if one exists, and the solution will satisfy all the constraints.
  - It is a simple and general algorithm that can be applied to any CSP.
  - It can be enhanced by various heuristics and techniques to improve its performance and reduce the search space.

- Disadvantages:

  - It is an exponential-time algorithm in the worst case, meaning that it may take a long time to find a solution or prove that none exists, especially for large and complex CSPs.
  - It may revisit the same states multiple times, wasting computation and memory.
  - It may suffer from thrashing, meaning that it may repeatedly backtrack over the same variables without making any progress.