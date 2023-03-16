### Uninformed Search

- Uninformed search is a type of search strategy that does not use any domain-specific knowledge or heuristics to guide the search process.
- Uninformed search methods are also called blind search or brute-force search, because they explore the search space systematically without any guidance or direction.
- Uninformed search methods are useful when there is no information available about the problem domain, or when the information is too complex or costly to use.
- Uninformed search methods are based on the following components:
  - A set of states, which represent the possible configurations of the problem.
  - A set of operators, which define the actions that can be applied to a state to generate a new state.
  - A start state, which is the initial configuration of the problem.
  - A goal state, or a set of goal states, which represent the desired configuration of the problem.
  - A path, which is a sequence of states and operators that leads from the start state to a goal state.
  - A search tree, which is a data structure that organizes the states and operators in a hierarchical manner, with the start state as the root and the goal states as the leaves.
- Uninformed search methods can be classified into two categories: tree search and graph search.
  - Tree search methods expand the nodes of the search tree in a certain order, and keep track of the paths from the root to the nodes.
  - Graph search methods expand the nodes of the search graph, which is a simplified version of the search tree that eliminates duplicate states, and keep track of the nodes that have been visited.
- Uninformed search methods can also be classified into four types: breadth-first search, depth-first search, uniform-cost search, and iterative deepening search.
  - Breadth-first search (BFS) expands the nodes of the search tree in a level-by-level order, starting from the root and moving to the lower levels. BFS is optimal and complete, meaning that it can find the shortest path to a goal state and guarantee to find a solution if one exists, but it is also memory-intensive, meaning that it requires a lot of space to store the nodes in the search tree.
  - Depth-first search (DFS) expands the nodes of the search tree in a depth-first order, starting from the root and moving to the deeper levels. DFS is neither optimal nor complete, meaning that it can find a suboptimal or even infinite path to a goal state and fail to find a solution even if one exists, but it is also memory-efficient, meaning that it requires a small amount of space to store the nodes in the search tree.
  - Uniform-cost search (UCS) expands the nodes of the search tree in a cost-based order, starting from the root and moving to the lower-cost nodes. UCS is optimal and complete, meaning that it can find the lowest-cost path to a goal state and guarantee to find a solution if one exists, but it is also memory-intensive, meaning that it requires a lot of space to store the nodes in the search tree.
  - Iterative deepening search (IDS) combines the advantages of BFS and DFS, by performing a series of DFS with increasing depth limits. IDS is optimal and complete, meaning that it can find the shortest path to a goal state and guarantee to find a solution if one exists, but it is also memory-efficient, meaning that it requires a small amount of space to store the nodes in the search tree.