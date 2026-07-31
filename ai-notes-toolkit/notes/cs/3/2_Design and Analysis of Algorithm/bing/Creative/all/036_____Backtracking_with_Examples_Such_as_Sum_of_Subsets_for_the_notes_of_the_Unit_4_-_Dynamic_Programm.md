# Backtracking with Examples Such as Sum of Subsets

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution.
- Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time.
- Backtracking can be viewed as a way of traversing a state space tree, which is a tree representing all the possible states (solution or nonsolution) of the problem. The root of the tree is the initial state, and the leaves are the final states. The intermediate nodes are the partial solutions.
- A general pseudo-code for backtracking algorithm is:

```
procedure backtrack(P, c) is
  if reject(P, c) then
    return
  if accept(P, c) then
    output(P, c)
  s ← first(P, c)
  while s ≠ NULL do
    backtrack(P, s)
    s ← next(P, s)
```

- Here, P is the problem, c is the current candidate, reject is a function that checks if the candidate violates any constraint, accept is a function that checks if the candidate is a complete solution, output is a function that prints or stores the solution, first is a function that returns the first extension of the candidate, and next is a function that returns the next extension of the candidate.
- One example of backtracking problem is the sum of subsets problem, which is to find all the subsets of a given set of positive integers that sum up to a given target value. For example, given the set {10, 7, 5, 18, 12, 20, 15} and the target value 35, the subsets are {10, 7, 18}, {10, 5, 20}, {10, 12, 13}, {7, 5, 12, 15}, {18, 17}, and {20, 15}.
- A possible solution using backtracking is:

```
procedure sum_of_subsets(S, t) is
  n ← length(S)
  x ← array of n boolean values, initialized to false
  backtrack(S, t, 0, 0, x)

procedure backtrack(S, t, i, s, x) is
  if s = t then
    output the subset corresponding to x
  else if i < n then
    x[i] ← true
    backtrack(S, t, i + 1, s + S[i], x)
    x[i] ← false
    backtrack(S, t, i + 1, s, x)
```

- Here, S is the set of integers, t is the target value, n is the size of the set, x is an array of boolean values that indicates whether an element is in the subset or not, i is the index of the current element, and s is the sum of the elements in the subset so far. The algorithm recursively explores all the possible subsets by setting x[i] to true or false, and checks if the sum equals the target value. If so, it outputs the subset. If not, it continues to the next element. The algorithm terminates when all the elements are processed or the sum exceeds the target value.