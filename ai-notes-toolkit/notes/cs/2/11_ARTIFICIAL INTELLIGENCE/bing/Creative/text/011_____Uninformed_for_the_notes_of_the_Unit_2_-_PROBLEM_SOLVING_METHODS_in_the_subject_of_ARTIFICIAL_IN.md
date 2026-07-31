### Uninformed Search

- Uninformed search is a type of search strategy that does not use any domain-specific knowledge or heuristics to guide the search process.
- Uninformed search is also known as blind search or brute-force search, as it explores the search space systematically without any direction or preference.
- Uninformed search algorithms are based on the following components:
  - A set of states, which represent the possible configurations of the problem.
  - A set of actions, which define the transitions between states.
  - A start state, which is the initial configuration of the problem.
  - A goal test, which determines whether a state is a solution or not.
  - A path cost, which assigns a numerical value to each path from the start state to a state.
- Uninformed search algorithms can be classified into two categories: tree search and graph search.
  - Tree search algorithms expand the nodes of a search tree, which is a data structure that represents the branching of the search space. Tree search algorithms do not keep track of the nodes that have been visited before, and may generate duplicate nodes or infinite loops.
  - Graph search algorithms expand the nodes of a search graph, which is a data structure that represents the connectivity of the search space. Graph search algorithms avoid generating duplicate nodes or infinite loops by using a data structure called a closed list, which stores the nodes that have been visited before.
- Some examples of uninformed search algorithms are:
  - Breadth-first search (BFS), which expands the shallowest nodes first, and uses a queue as the data structure for storing the nodes to be expanded. BFS is complete, meaning that it will find a solution if one exists, and optimal, meaning that it will find the least-cost solution if the path cost is a non-decreasing function of the depth.
  - Depth-first search (DFS), which expands the deepest nodes first, and uses a stack as the data structure for storing the nodes to be expanded. DFS is incomplete, meaning that it may not find a solution even if one exists, and non-optimal, meaning that it may not find the least-cost solution. DFS has a low memory requirement, as it only stores the nodes along the current path.
  - Uniform-cost search (UCS), which expands the nodes with the lowest path cost first, and uses a priority queue as the data structure for storing the nodes to be expanded. UCS is complete and optimal, as it will find the least-cost solution regardless of the path cost function. UCS is a generalization of BFS, as it reduces to BFS when the path cost is a constant function of the depth.
  - Depth-limited search (DLS), which is a variant of DFS that imposes a limit on the maximum depth of the search. DLS is incomplete and non-optimal, but it avoids infinite loops and can be used to explore large or infinite search spaces. DLS can be combined with iterative deepening, which is a technique that gradually increases the depth limit until a solution is found or the search space is exhausted. Iterative deepening is complete and optimal, and has a low memory requirement.