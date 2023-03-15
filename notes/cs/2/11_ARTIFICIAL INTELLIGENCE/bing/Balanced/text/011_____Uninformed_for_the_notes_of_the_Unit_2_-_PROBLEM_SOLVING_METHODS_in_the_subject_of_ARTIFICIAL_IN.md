### Uninformed Search

- Uninformed search is a type of search strategy that does not use any domain-specific knowledge or heuristics to guide the search process.
- Uninformed search methods are also called blind search or brute-force search, because they explore the search space systematically without any guidance or direction.
- Uninformed search methods are useful when there is no information available about the problem domain, or when the information is too complex or costly to use.
- Uninformed search methods can be classified into two categories: tree search and graph search.
- Tree search is a search method that expands the nodes of a search tree in some order, and keeps track of the nodes that have been generated but not yet expanded. Tree search does not check for repeated states or loops in the search space.
- Graph search is a search method that expands the nodes of a search graph in some order, and keeps track of the nodes that have been visited or expanded. Graph search avoids expanding the same node more than once, and can detect loops or cycles in the search space.
- Some common uninformed search methods are:

  - Breadth-first search (BFS): A tree search method that expands the shallowest node first, i.e., the node with the lowest depth in the search tree. BFS is optimal and complete, but has high space complexity.
  - Depth-first search (DFS): A tree search method that expands the deepest node first, i.e., the node with the highest depth in the search tree. DFS is neither optimal nor complete, but has low space complexity.
  - Uniform-cost search (UCS): A tree search method that expands the node with the lowest path cost first, i.e., the node with the lowest sum of edge costs from the root to the node. UCS is optimal and complete, but has high space complexity.
  - Depth-limited search (DLS): A tree search method that limits the depth of the search tree to a predefined value, and does not expand any node beyond that depth. DLS is neither optimal nor complete, but has low space complexity.
  - Iterative deepening search (IDS): A tree search method that performs a series of depth-limited searches with increasing depth limits, until a solution is found or the search space is exhausted. IDS is optimal and complete, and has low space complexity.