Hello, I am Sydney, your AI assistant. I can help you with writing notes on various topics. Here are some notes on the topic of uninformed search for the unit 2 of problem solving methods in artificial intelligence.

# Uninformed Search

- Uninformed search is a type of search strategy that does not use any domain-specific knowledge or heuristics to guide the search process.
- Uninformed search is also known as blind search or brute-force search, as it explores the search space exhaustively until a goal state is found or the search space is exhausted.
- Uninformed search is useful when there is no information available about the problem domain or the goal state, or when the problem is simple enough that any solution is acceptable.
- Uninformed search can be classified into two categories: tree search and graph search.
  - Tree search is a search strategy that expands the nodes of a search tree in a systematic order, such as breadth-first, depth-first, or uniform-cost.
  - Graph search is a search strategy that avoids expanding the same node more than once by keeping track of the nodes that have been visited or expanded.
- Some of the common uninformed search algorithms are:
  - Breadth-first search (BFS): a tree search algorithm that expands the shallowest node in the frontier (the set of nodes that are waiting to be expanded).
  - Depth-first search (DFS): a tree search algorithm that expands the deepest node in the frontier (the set of nodes that are waiting to be expanded).
  - Uniform-cost search (UCS): a tree search algorithm that expands the node with the lowest path cost from the initial state to the node.
  - Depth-limited search (DLS): a tree search algorithm that limits the depth of the search tree to a predefined limit.
  - Iterative deepening search (IDS): a tree search algorithm that repeatedly applies depth-limited search with increasing depth limits until a goal state is found or the search space is exhausted.
  - Bidirectional search: a graph search algorithm that simultaneously searches forward from the initial state and backward from the goal state, and stops when the two searches meet in the middle.