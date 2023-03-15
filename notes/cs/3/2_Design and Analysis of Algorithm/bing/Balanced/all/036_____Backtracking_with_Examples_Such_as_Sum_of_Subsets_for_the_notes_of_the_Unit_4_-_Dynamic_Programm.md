# Backtracking with Examples Such as Sum of Subsets

- Backtracking is a class of algorithms for finding solutions to some computational problems, notably constraint satisfaction problems, that incrementally builds candidates to the solutions, and abandons a candidate ("backtracks") as soon as it determines that the candidate cannot possibly be completed to a valid solution. 
- Backtracking is an algorithmic technique for solving problems recursively by trying to build a solution incrementally, one piece at a time, removing those solutions that fail to satisfy the constraints of the problem at any point of time. 
- Backtracking can be applied to problems that can be represented as a state space tree, where each node is a partial solution and the leaves are the complete solutions. 
- The backtracking algorithm traverses the state space tree by exploring the children of each node, starting from the root. If a node is found to be invalid or a dead end, the algorithm backtracks to its parent and tries another child. The algorithm terminates when all the nodes have been visited or a solution is found.  
- The backtracking algorithm can be implemented using a recursive function that takes the current node as a parameter and performs the following steps: 
  - If the node is a solution, print or return it.
  - If the node is invalid or a dead end, return.
  - For each child of the node, call the recursive function with the child as the parameter.
- The backtracking algorithm can be optimized by using some techniques, such as pruning, ordering, and bounding, to reduce the number of nodes that need to be explored.  
- One example of a problem that can be solved by backtracking is the sum of subsets problem, which is to find all the subsets of a given set of positive integers that sum up to a given target value. 
- The sum of subsets problem can be represented as a state space tree, where each node is a subset of the given set and the root is the empty set. The children of a node are obtained by adding one element from the remaining set to the node. The node is a solution if the sum of its elements is equal to the target value. The node is invalid if the sum of its elements is greater than the target value. 
- The following is a pseudocode of the backtracking algorithm for the sum of subsets problem: 

```
function sumOfSubsets(set, target, index, subset, sum):
  # set is the given set of positive integers
  # target is the given target value
  # index is the current position in the set
  # subset is the current subset
  # sum is the current sum of the subset
  if sum == target: # if the subset is a solution
    print subset # print or return the subset
  elif sum < target and index < set.length: # if the subset is not a dead end
    # include the current element in the subset
    subset.add(set[index])
    sumOfSubsets(set, target, index + 1, subset, sum + set[index])
    # exclude the current element from the subset
    subset.remove(set[index])
    sumOfSubsets(set, target, index + 1, subset, sum)
```

- The following is an example of the sum of subsets problem with the set {10, 7, 5, 18, 12, 20, 15} and the target value 35: 

```
The state space tree for the problem is:

               {} (0)
              /      \
          {10} (10)   {} (0)
          /   \       /   \
      {10,7} (17) {7} (7) {5} (5) {} (0)
      /  \    / \   / \   / \   / \
  {10,7,5} (22) ... ... ... ... ... ...
  /  \    / \
{10,7,5,18} (40) {10,7,5,12} (34) {10,7,5,20} (42) {10,7,5,15} (37)
/ \ / \ / \ / \
... ... ... ... ... ...

The solutions are:

{10, 7, 18}
{10, 5, 20}
{