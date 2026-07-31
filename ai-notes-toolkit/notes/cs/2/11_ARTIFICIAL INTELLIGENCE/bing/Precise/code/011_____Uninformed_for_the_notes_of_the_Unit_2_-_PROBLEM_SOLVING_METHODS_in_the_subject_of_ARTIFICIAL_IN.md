### Uninformed Search

Uninformed search, also known as blind search, is a search strategy that uses no problem-specific knowledge. It is a basic search technique used in artificial intelligence for traversing and searching tree or graph data structures. Uninformed search algorithms do not have additional information about the state space other than the provided problem definition.

Some common uninformed search algorithms include:
1. Breadth-first search (BFS)
2. Depth-first search (DFS)
3. Uniform-cost search (UCS)
4. Iterative deepening depth-first search (IDDFS)

These algorithms are called "uninformed" because they do not use any information about the goal state to guide the search. Instead, they explore the search space systematically until the goal state is found. The choice of which algorithm to use depends on the specific problem and the desired properties of the solution, such as optimality, completeness, and time and space complexity.

Breadth-first search (BFS) explores the search space level by level, expanding all nodes at a given depth before moving on to the next level. This ensures that the first solution found is the shortest path to the goal state.

Depth-first search (DFS) explores the search space by always expanding the deepest node in the current frontier. This can lead to long, winding paths that may not be optimal.

Uniform-cost search (UCS) expands the node with the lowest path cost from the start state. This ensures that the first solution found is the optimal solution in terms of path cost.

Iterative deepening depth-first search (IDDFS) combines the benefits of BFS and DFS by performing a series of depth-limited DFS searches, increasing the depth limit with each iteration until the goal state is found.

In summary, uninformed search algorithms are basic search techniques that do not use problem-specific knowledge to guide the search. They can be useful for solving problems where little is known about the state space, but may not be the most efficient choice for problems where additional information is available.