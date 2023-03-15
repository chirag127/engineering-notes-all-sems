Hello, I am Sydney, your AI assistant. I can help you with your notes on Uninformed Search for the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS. Here is the content in markdown format:

### Uninformed Search
- Uninformed search is a type of search strategy that does not use any domain-specific knowledge or heuristics to guide the search process.
- Uninformed search methods are also called blind search or brute-force search, as they explore the search space systematically without any direction or preference.
- Uninformed search methods are useful when there is no information available about the problem domain, or when the information is too complex or costly to use.
- Uninformed search methods are based on the following components:
  - A set of states, which represent the possible configurations of the problem.
  - A set of operators, which define the actions that can be applied to a state to generate a new state.
  - An initial state, which is the starting point of the search.
  - A goal state, which is the desired outcome of the search.
  - A path, which is a sequence of states and operators that leads from the initial state to the goal state.
  - A search tree, which is a data structure that organizes the states and operators in a hierarchical manner, with the initial state as the root and the goal state as one or more leaves.
- Uninformed search methods can be classified into two categories: tree search and graph search.
  - Tree search methods expand the nodes of the search tree in a certain order, and keep track of the paths from the root to the expanded nodes.
  - Graph search methods expand the nodes of the search graph, which is a simplified version of the search tree that avoids repeated states, and keep track of the paths from the initial state to the expanded nodes.
- Uninformed search methods can also be classified into four types: breadth-first search, depth-first search, uniform-cost search, and iterative deepening search.
  - Breadth-first search (BFS) expands the nodes in the order of their distance from the root, i.e., from the shallowest to the deepest level of the search tree. BFS is optimal, complete, and has a time and space complexity of O(b^d), where b is the branching factor and d is the depth of the shallowest goal node.
  - Depth-first search (DFS) expands the nodes in the order of their distance from the root, i.e., from the deepest to the shallowest level of the search tree. DFS is not optimal, not complete, and has a time and space complexity of O(b^m), where b is the branching factor and m is the maximum depth of the search tree.
  - Uniform-cost search (UCS) expands the nodes in the order of their path cost from the root, i.e., from the cheapest to the most expensive path. UCS is optimal, complete, and has a time and space complexity of O(b^c*), where b is the branching factor and c* is the cost of the optimal solution.
  - Iterative deepening search (IDS) combines the advantages of BFS and DFS by performing a series of DFS with increasing depth limits. IDS is optimal, complete, and has a time and space complexity of O(b^d), where b is the branching factor and d is the depth of the shallowest goal node.