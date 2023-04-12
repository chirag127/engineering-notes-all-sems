### Backtracking with Examples Such as Sum of Subsets

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 
- The backtracking algorithm enumerates a set of partial candidates that, in principle, could be completed in various ways to give all the possible solutions to the given problem. The completion is done incrementally, by a sequence of candidate extension steps. 
- The backtracking algorithm reduces the problem to the call `backtrack (root (P))`, where `backtrack` is the following recursive procedure: 

```
procedure backtrack (P, c) is
    if reject (P, c) then return
    if accept (P, c) then output (P, c)
    s ← first (P, c)
    while s ≠ NULL do
        backtrack (P, s)
        s ← next (P, s)
```

- The procedure `backtrack` takes two arguments: a problem `P` and a candidate `c`. The problem `P` defines the constraints and the goal of the problem, and the candidate `c` is a partial solution that may or may not satisfy the constraints or the goal. 
- The procedure `reject` returns `true` if the candidate `c` violates any of the constraints of `P`, and `false` otherwise. The procedure `accept` returns `true` if the candidate `c` satisfies the goal of `P`, and `false` otherwise. The procedure `output` prints or stores the solution `c`. 
- The procedure `first` returns the first extension of the candidate `c`, and the procedure `next` returns the next extension of the candidate `c`, or `NULL` if there is no more extension. The extensions are the possible ways of adding one more element to the partial solution `c`. 
- The backtracking algorithm works by exploring the state space tree of the problem, where each node represents a partial solution. The root node is the empty solution, and the leaves are the complete solutions. The algorithm traverses the tree in depth-first order, pruning the branches that do not lead to valid solutions. 
- An example of a problem that can be solved by backtracking is the sum of subsets problem, which is to find all the subsets of a given set of positive integers that sum up to a given target value. 
- The sum of subsets problem can be formulated as follows: 

```
Given a set S = {s1, s2, ..., sn} of n positive integers and a target value t, find all the subsets of S that sum up to t.
```

- A possible solution using backtracking is to use an array `x` of size `n` to store the inclusion status of each element in `S`. That is, `x[i] = 1` if `si` is included in the subset, and `x[i] = 0` otherwise. 
- The algorithm starts with an empty subset (`x[i] = 0` for all `i`) and a sum of zero. It then tries to add the first element `s1` to the subset, and checks if the sum is equal to, less than, or greater than the target value. If the sum is equal to the target value, it outputs the subset and backtracks. If the sum is less than the target value, it recursively explores the remaining elements. If the sum is greater than the target value, it prunes the branch and backtracks. 
- The algorithm repeats the same process for the case when the first element `s1` is not included in the subset, and continues until all the elements are considered. 
- The pseudocode of the algorithm is as follows: 

```
procedure sum_of_subsets (S, t) is
    n ← length of S
    x ← an array of size n initialized to 0
    backtrack (S, t, x, 0, 0)

procedure backtrack (S, t, x, k, sum) is
    if sum = t then
        output x
    else if sum < t and k < n then

```
