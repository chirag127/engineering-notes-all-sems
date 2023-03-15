### Backtracking with Examples Such as Sum of Subsets

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.
- Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time.
- Backtracking can be viewed as a way of traversing a state space tree, which is a tree representing all the possible states (solution or nonsolution) of the problem.
- The basic idea of backtracking is to start from the root of the state space tree and explore the branches of the tree until a solution is found or all the possibilities are exhausted.
- The backtracking algorithm can be defined as follows:

```
procedure backtrack(P, c) is
  if reject(P, c) then return
  if accept(P, c) then output(P, c)
  s ← first(P, c)
  while s ≠ NULL do
    backtrack(P, s)
    s ← next(P, s)
```

- Here, P is the problem instance, c is a partial candidate solution, reject(P, c) is a function that returns true if c is not a valid solution or cannot be extended to a valid solution, accept(P, c) is a function that returns true if c is a valid solution, output(P, c) is a function that prints or stores the solution c, first(P, c) is a function that returns the first extension of c, and next(P, c, s) is a function that returns the next extension of c after s.
- An example of a problem that can be solved by backtracking is the sum of subsets problem, which is to find all the subsets of a given set of positive integers that sum up to a given target value.
- The state space tree for the sum of subsets problem can be constructed as follows:
  - The root node represents an empty subset with sum 0.
  - Each node has two children, one representing the inclusion of the next element in the subset, and the other representing the exclusion of the next element in the subset.
  - The nodes are labeled with the sum of the elements in the subset and the index of the next element to be considered.
  - The nodes that have a sum greater than the target value or have exhausted all the elements are rejected and pruned from the tree.
  - The nodes that have a sum equal to the target value and have exhausted all the elements are accepted and output as solutions.
- For example, consider the set {10, 7, 5, 18, 12, 20, 15} and the target value 35. The state space tree for this problem is shown below, where the nodes in green are accepted, the nodes in red are rejected, and the nodes in black are intermediate.

![State space tree for sum of subsets problem](https://i.imgur.com/9Zs0z0F.png)

- The solutions are {10, 7, 18}, {10, 5, 20}, {10, 12, 15}, {7, 5, 12, 15}, and {5, 18, 12}.