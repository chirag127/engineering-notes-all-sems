### Backtracking with Examples Such as n-Queen Problem

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 
- The backtracking algorithm enumerates a set of partial candidates that, in principle, could be completed in various ways to give all the possible solutions to the given problem. The completion is done incrementally, by a sequence of candidate extension steps. 
- Backtracking can be applied to problems that can be formulated as a state space tree, where each node represents a partial solution and each edge represents a possible extension of the solution. 
- The backtracking algorithm traverses the state space tree in a depth-first manner, exploring one branch of the tree until it reaches a dead end or a solution, and then backtracks to the previous node and tries another branch. 
- The backtracking algorithm can be generalized by the following pseudocode: 

```
procedure backtrack(P, c) is
    if reject(P, c) then return
    if accept(P, c) then output(P, c)
    s ← first(P, c)
    while s ≠ NULL do
        backtrack(P, s)
        s ← next(P, s)
```

- Here, P is the problem instance, c is a partial candidate, reject(P, c) is a function that returns true if c is not a valid partial solution, accept(P, c) is a function that returns true if c is a complete and valid solution, output(P, c) is a function that prints or stores the solution, first(P, c) is a function that returns the first extension of c, and next(P, c) is a function that returns the next extension of c after s. 
- The functions reject, accept, first, and next depend on the specific problem and the representation of the candidates. They can be implemented using various techniques, such as pruning, bounding, heuristics, or symmetry breaking. 
- One example of a problem that can be solved by backtracking is the n-queen problem, where the goal is to place n queens on an n×n chessboard such that no two queens attack each other. 
- A possible representation of a candidate is a one-dimensional array of size n, where each element denotes the column number of the queen in the corresponding row. For example, [2, 4, 1, 3] represents a solution for n = 4, where the queens are placed at (1, 2), (2, 4), (3, 1), and (4, 3). 
- The function reject can check if the current candidate violates the constraint of no two queens attacking each other by comparing the column and diagonal values of the last queen with the previous ones. The function accept can check if the current candidate is a complete solution by verifying if the array is filled with n values. The function first can return the first possible column value for the next row, which is 1. The function next can return the next possible column value for the same row, which is the previous value plus 1, until it reaches n. 
- The following is a possible implementation of the backtracking algorithm for the n-queen problem in Python: 

```python
def backtrack(n, c):
    if reject(n, c):
        return
    if accept(n, c):
        output(n, c)
    s = first(n, c)
    while s != None:
        backtrack(n, s)
        s = next(n, s)

def reject(n, c):
    # check if the last queen conflicts with any previous one
    k = len(c) - 1
    for i in range(k):
        if c[i] == c[k] or abs(c[i] - c[k]) == k - i:
            return True
    return False

def accept(n, c):
    # check if the array is complete
    return len(c) == n

def output(n, c):
    # print the solution
    print(c)

def first(n, c):
    # return the first column value for the next row
    return [1]

def next(n, s):
    # return the next column value for the