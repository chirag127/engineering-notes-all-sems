Hello, I am Sydney, your AI assistant. I can help you with your study material for the subject of Artificial Intelligence KCS. Here are some notes on the topic of Uninformed Search for the Unit 2 - Problem Solving Methods.

### Uninformed Search

- Uninformed search is a type of search strategy that does not use any domain-specific knowledge or heuristics to guide the search process.
- Uninformed search is also known as blind search or brute-force search, as it explores the search space exhaustively until a solution is found or the search space is exhausted.
- Uninformed search can be classified into two categories: tree search and graph search.
- Tree search is a search strategy that expands the nodes of a search tree in some order, without checking for repeated states or loops.
- Graph search is a search strategy that avoids expanding the same state more than once by keeping track of the visited states in a data structure called a closed list or an explored set.
- Some common uninformed search algorithms are:
  - Breadth-first search (BFS): a tree search algorithm that expands the shallowest node first, using a queue as the data structure for the frontier or open list.
  - Depth-first search (DFS): a tree search algorithm that expands the deepest node first, using a stack as the data structure for the frontier or open list.
  - Uniform-cost search (UCS): a graph search algorithm that expands the node with the lowest path cost from the initial state to the current state, using a priority queue as the data structure for the frontier or open list.
  - Depth-limited search (DLS): a tree search algorithm that limits the depth of the search tree to a predefined value, using a stack as the data structure for the frontier or open list.
  - Iterative deepening depth-first search (IDDFS): a tree search algorithm that combines the benefits of BFS and DFS, by performing a series of DLS with increasing depth limits, until a solution is found or the search space is exhausted.
  - Bidirectional search (BDS): a graph search algorithm that searches from both the initial state and the goal state simultaneously, using two queues as the data structures for the frontiers or open lists, and stopping when the two searches meet in the middle.