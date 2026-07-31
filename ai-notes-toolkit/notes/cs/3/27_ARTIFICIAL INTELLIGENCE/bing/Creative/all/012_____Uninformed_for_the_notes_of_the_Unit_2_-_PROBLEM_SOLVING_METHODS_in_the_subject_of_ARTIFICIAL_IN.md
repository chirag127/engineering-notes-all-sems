Hello, I am Sydney, your AI assistant. I can help you with your notes on the topic of uninformed search for the unit 2 of the subject of artificial intelligence. Here are some points you can use:

# Uninformed Search

- Uninformed search is a type of search strategy that does not use any domain-specific knowledge or heuristics to guide the search process.
- Uninformed search is also known as blind search or brute-force search, as it explores the search space exhaustively until a solution is found or the space is proven to be empty.
- Uninformed search can be classified into two categories: tree search and graph search.
- Tree search is a search strategy that expands the nodes of a search tree in some order, without checking for repeated states or loops.
- Graph search is a search strategy that avoids expanding any node more than once by keeping track of the nodes that have been visited or are in the frontier.
- Some common uninformed search algorithms are:
  - Breadth-first search (BFS): It expands the shallowest nodes first, using a queue as the data structure for the frontier. It is optimal, complete, and has a time and space complexity of O(b^d), where b is the branching factor and d is the depth of the solution.
  - Depth-first search (DFS): It expands the deepest nodes first, using a stack as the data structure for the frontier. It is not optimal, not complete in infinite spaces, and has a time complexity of O(b^m) and a space complexity of O(bm), where m is the maximum depth of the search tree.
  - Uniform-cost search (UCS): It expands the nodes with the lowest path cost first, using a priority queue as the data structure for the frontier. It is optimal, complete, and has a time and space complexity of O(b^1 + C*), where C* is the cost of the optimal solution.
  - Depth-limited search (DLS): It is a variant of DFS that imposes a limit on the depth of the search tree. It is not optimal, complete only if the solution is within the limit, and has a time complexity of O(b^l) and a space complexity of O(bl), where l is the depth limit.
  - Iterative deepening search (IDS): It is a combination of BFS and DLS that gradually increases the depth limit until a solution is found or the search space is exhausted. It is optimal, complete, and has a time complexity of O(b^d) and a space complexity of O(bd).