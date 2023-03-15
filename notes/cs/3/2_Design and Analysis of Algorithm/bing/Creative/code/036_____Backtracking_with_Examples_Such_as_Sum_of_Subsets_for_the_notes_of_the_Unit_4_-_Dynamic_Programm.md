# Backtracking with Examples Such as Sum of Subsets

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 
- Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time. 
- Backtracking can be viewed as a systematic way of exploring a state space tree, which is a tree representing all the possible states (solution or nonsolution) of the problem. 
- The backtracking algorithm reduces the problem to the call `backtrack(root(P))`, where `backtrack` is the following recursive procedure: 

```
procedure backtrack(P, c) is
    if reject(P, c) then return
    if accept(P, c) then output(P, c)
    s ← first(P, c)
    while s ≠ NULL do
        backtrack(P, s)
        s ← next(P, s)
```

- The procedure `backtrack` takes two arguments: a problem instance `P` and a candidate `c`. The procedure `reject` tests whether the candidate is worth completing, and returns true if it is not. The procedure `accept` tests whether the candidate is a solution, and returns true if it is. The procedure `output` processes the solution in some way. The procedure `first` generates the first extension of the candidate, and `next` generates the next alternative extension after a given one. If there are no more extensions, `next` returns `NULL`.
- A common example of a problem that can be solved by backtracking is the sum of subsets problem, which is to find all subsets of a given set of positive integers that sum up to a given target value. 
- The state space tree for the sum of subsets problem can be constructed as follows: 

  - The root node represents an empty subset with sum zero.
  - Each node has two children: one that includes the next element of the set in the subset, and one that excludes it.
  - The nodes are labeled with the sum of the elements in the subset.
  - The nodes that have a sum greater than the target value are rejected and pruned from the tree.
  - The nodes that have a sum equal to the target value are accepted and output as solutions.

- For example, consider the set {10, 7, 5, 18, 12, 20, 15} and the target value 35. The state space tree for this problem is shown below, where the rejected nodes are crossed out and the accepted nodes are highlighted in green.

![sum of subsets state space tree](https://www.programiz.com/sites/tutorial2program/files/sum-of-subsets-state-space-tree.png)

- The backtracking algorithm for the sum of subsets problem can be implemented as follows: 

```
procedure sum_of_subsets(set, target) is
    backtrack(set, target, 0, 0, [])
    
procedure backtrack(set, target, sum, index, subset) is
    if sum > target then return // reject
    if sum == target then output(subset) // accept
    if index == length(set) then return // no more elements
    // include the next element in the subset
    backtrack(set, target, sum + set[index], index + 1, subset + [set[index]])
    // exclude the next element from the subset
    backtrack(set, target, sum, index + 1, subset)
```

- The procedure `sum_of_subsets` takes a set of positive integers and a target value as arguments, and calls the `backtrack` procedure with the initial values of sum, index, and subset. The procedure `backtrack` takes the set, the target, the current sum, the current index, and the current subset as arguments, and recursively explores the state space tree. If the sum is greater than the target, the candidate is rejected and the recursion returns. If the sum is equal to the target, the candidate is accepted and the subset is output. If the index reaches the end of the set, the recursion returns. Otherwise, the procedure tries both possibilities of including and excluding the next element in the subset, and updates