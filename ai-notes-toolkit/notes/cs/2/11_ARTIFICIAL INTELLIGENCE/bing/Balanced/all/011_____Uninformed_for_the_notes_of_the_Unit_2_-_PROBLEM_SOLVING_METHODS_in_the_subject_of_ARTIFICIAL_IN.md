Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here are some notes on the topic of uninformed search for the unit 2 of the subject of artificial intelligence KCS:

# Uninformed Search

- Uninformed search is a type of search strategy that does not use any domain-specific knowledge or heuristics to guide the search process.
- Uninformed search is also known as blind search or brute-force search, as it explores the search space systematically without any direction or preference.
- Uninformed search is useful when the problem domain is simple, the solution path is short, or the domain-specific knowledge is not available or reliable.
- Uninformed search can be classified into two categories: tree search and graph search.
  - Tree search is a search strategy that expands the nodes of a search tree in a certain order, without checking for repeated states or loops.
  - Graph search is a search strategy that expands the nodes of a search graph in a certain order, while keeping track of visited states or loops to avoid redundant exploration.
- Some common uninformed search algorithms are:
  - Breadth-first search (BFS): a tree search or graph search algorithm that expands the shallowest node first, i.e., the node with the lowest depth in the search tree or graph.
  - Depth-first search (DFS): a tree search or graph search algorithm that expands the deepest node first, i.e., the node with the highest depth in the search tree or graph.
  - Uniform-cost search (UCS): a tree search or graph search algorithm that expands the node with the lowest path cost first, i.e., the node with the lowest sum of edge weights from the root to the node in the search tree or graph.
  - Depth-limited search (DLS): a tree search or graph search algorithm that expands the nodes up to a predefined depth limit, and returns a failure if the solution is not found within the limit.
  - Iterative deepening search (IDS): a tree search or graph search algorithm that performs a series of depth-limited searches with increasing depth limits, until the solution is found or the search space is exhausted.