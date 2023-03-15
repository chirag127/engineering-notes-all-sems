# Backtracking with Examples Such as n-Queen Problem

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 
- Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time. 
- Backtracking can be viewed as a depth-first search of a state space tree, where each node represents a partial solution, and the branches are the possible extensions of the solution. 
- Backtracking can be applied to problems that can be formulated as finding a path from the root to a leaf node in a state space tree, where each leaf node is a possible solution. 
- Backtracking can be implemented using recursion or iteration, with the help of a stack to store the partial solutions. 
- Backtracking can be optimized by using heuristics, pruning, and memoization techniques to reduce the size of the search space and avoid repeated computations. 

## Example: n-Queen Problem

- The n-queen problem is a classic example of a constraint satisfaction problem, where the goal is to place n queens on an n x n chessboard, such that no two queens can attack each other. 
- A queen can attack another queen if they are on the same row, column, or diagonal. 
- A possible solution to the n-queen problem is a configuration of n queens on the board, where none of them can attack each other. 
- A partial solution to the n-queen problem is a configuration of k queens on the board, where k < n, and none of them can attack each other. 
- A partial solution can be extended by placing a queen on an empty row, and checking if it is safe to do so, i.e., it does not conflict with any of the existing queens. 
- If a partial solution cannot be extended, then it is rejected, and the algorithm backtracks to the previous partial solution, and tries a different extension. 
- If a partial solution can be extended to a complete solution, then it is outputted as a valid solution. 
- The algorithm terminates when all possible extensions have been explored, or when a desired number of solutions have been found. 

### Pseudocode

```
procedure nQueen(n)
  create an empty stack S
  push the empty board configuration to S
  while S is not empty
    pop the top configuration C from S
    if C is a complete solution
      output C
    else
      for each possible extension E of C
        if E is safe
          push E to S
```

### Example

- Suppose we want to find one solution to the 4-queen problem. 
- We start with an empty board configuration, and push it to the stack. 
- We pop the top configuration from the stack, and try to extend it by placing a queen on the first row. 
- We have four possible extensions, one for each column. We check if each extension is safe, i.e., it does not conflict with any existing queen. 
- We find that the extension with the queen on the first column is safe, so we push it to the stack. 
- We pop the top configuration from the stack, and try to extend it by placing a queen on the second row. 
- We have four possible extensions, one for each column. We check if each extension is safe, i.e., it does not conflict with any existing queen. 
- We find that the extension with the queen on the fourth column is safe, so we push it to the stack. 
- We pop the top configuration from the stack, and try to extend it by placing a queen on the third row. 
- We have four possible extensions, one for each column. We check if each extension is safe, i.e., it does not conflict with any existing queen. 
- We