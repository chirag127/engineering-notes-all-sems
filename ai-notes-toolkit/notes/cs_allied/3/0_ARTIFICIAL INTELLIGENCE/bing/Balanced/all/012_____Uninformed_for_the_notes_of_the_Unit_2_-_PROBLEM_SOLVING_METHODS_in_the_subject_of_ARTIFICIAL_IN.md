Hello, I am Sydney, your AI assistant. I can help you with writing notes on the topic of Uninformed Search for the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS. Here is the content I have generated for you in markdown format:

# Uninformed Search

- Uninformed search is a type of search strategy that does not use any domain-specific knowledge or heuristics to guide the search process.
- Uninformed search methods are also called blind search or brute-force search, as they explore the search space systematically without any direction or preference.
- Uninformed search methods are useful when there is no information available about the problem domain, or when the information is too complex or costly to use.
- Uninformed search methods can be classified into two categories: tree search and graph search.
- Tree search methods expand the nodes of a search tree, which represents the possible paths from the initial state to the goal state. Tree search methods do not keep track of the nodes that have been visited before, and may generate duplicate nodes or infinite paths.
- Graph search methods expand the nodes of a search graph, which represents the state space of the problem. Graph search methods avoid expanding the same node more than once, and can detect cycles or dead ends in the search space.
- Some of the common uninformed search methods are:

  - Breadth-first search (BFS): It expands the shallowest node in the frontier, which is a queue of nodes that are waiting to be explored. BFS is complete, meaning it will find a solution if one exists, and optimal, meaning it will find the shortest path to the goal.
  - Depth-first search (DFS): It expands the deepest node in the frontier, which is a stack of nodes that are waiting to be explored. DFS is incomplete, meaning it may get stuck in an infinite loop or a dead end, and non-optimal, meaning it may find a longer path to the goal.
  - Uniform-cost search (UCS): It expands the node with the lowest path cost in the frontier, which is a priority queue of nodes that are waiting to be explored. UCS is complete and optimal, as long as the path cost is non-negative and monotonic, meaning it never decreases along a path.
  - Depth-limited search (DLS): It is a variant of DFS that imposes a limit on the depth of the search tree. DLS is complete and optimal up to the depth limit, but may miss a solution if the limit is too low or waste time if the limit is too high.
  - Iterative deepening search (IDS): It is a combination of BFS and DLS that performs a series of DLS with increasing depth limits until a solution is found or the search space is exhausted. IDS is complete and optimal, and uses less memory than BFS.