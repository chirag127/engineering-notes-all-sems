### Backtracking with Examples Such as Sum of Subsets

- Backtracking is a general algorithmic technique that considers searching every possible combination in order to solve a computational problem.
- Backtracking is often implemented using recursion, which makes the code compact and elegant.
- Backtracking can be used to solve problems that involve finding all possible arrangements or permutations of a given set of elements, such as the n-queens problem, the sudoku problem, the crossword puzzle, etc.
- Backtracking can also be used to solve optimization problems, such as the knapsack problem, the traveling salesman problem, the graph coloring problem, etc.
- The basic idea of backtracking is to start from an empty solution vector and one by one add items (candidates) to the solution vector. For each item, we check if it is feasible to add it to the solution vector. If it is, we recursively explore further by adding more items. If it is not, we backtrack and remove the item from the solution vector and try a different item.
- The key to backtracking is to define the following components:
  - The solution vector: a data structure that holds the partial or complete solution to the problem.
  - The candidates: a set of possible items that can be added to the solution vector.
  - The feasibility function: a function that checks if a candidate can be added to the solution vector without violating any constraints.
  - The goal function: a function that checks if the solution vector is complete and satisfies the problem statement.
- One example of a problem that can be solved using backtracking is the sum of subsets problem. The problem is to find all subsets of a given set of positive integers that sum up to a given target value. For example, given the set {10, 7, 5, 18, 12, 20, 15} and the target value 35, the subsets are {10, 7, 18}, {10, 5, 20}, {10, 12, 13}, {7, 5, 12, 15}, {18, 17}, {20, 15}.
- To solve the sum of subsets problem using backtracking, we can define the following components:
  - The solution vector: an array of boolean values that indicate whether an element of the given set is included in the subset or not. For example, [true, false, true, false, false, false, false] means that the subset contains the first and the third element of the set, i.e., {10, 5}.
  - The candidates: the remaining elements of the given set that have not been considered yet. For example, if the solution vector is [true, false, true, false, false, false, false], the candidates are {18, 12, 20, 15}.
  - The feasibility function: a function that checks if adding a candidate to the solution vector will not exceed the target value. For example, if the solution vector is [true, false, true, false, false, false, false], the target value is 35, and the candidate is 18, the feasibility function will return false, because 10 + 5 + 18 > 35.
  - The goal function: a function that checks if the sum of the elements in the solution vector is equal to the target value. For example, if the solution vector is [true, false, true, false, false, false, false], the target value is 35, and the sum of the elements in the solution vector is 15, the goal function will return false, because 15 != 35.
- The pseudocode for the backtracking algorithm for the sum of subsets problem is as follows:

```
// n is the size of the given set, s is the array of the given set elements, t is the target value, x is the solution vector, and sum is the current sum of the elements in the solution vector
backtrack(n, s, t, x, sum) {
  // if the goal function is true, print the solution vector
  if (sum == t) {
    print(x)
    return
  }
  // if there are no more candidates, return
  if (n == 0) {
    return
  }
  // for each candidate
  for i from 0 to 1 {
    // set the ith element of the solution vector to true or false
    x[n-1] = i
    // if the feasibility function is true, recursively explore further
    if (sum + i *

```
