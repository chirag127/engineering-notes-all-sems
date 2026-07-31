Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes on the topic of uninformed search for the unit 2 of problem solving methods in artificial intelligence.

### Uninformed Search

- Uninformed search is a type of search strategy that does not use any domain-specific knowledge or heuristics to guide the search process.
- Uninformed search is also known as blind search or brute-force search, as it explores the search space exhaustively until a solution is found or the space is proven to be empty.
- Uninformed search can be classified into two categories: tree search and graph search.
- Tree search is a search strategy that expands the nodes of a search tree in some order, without checking for duplicates or loops.
- Graph search is a search strategy that avoids expanding the same node more than once by keeping track of the nodes that have been visited or expanded.
- Some common uninformed search algorithms are:
  - Breadth-first search (BFS): a tree search algorithm that expands the shallowest node first, using a queue as the data structure to store the nodes.
  - Depth-first search (DFS): a tree search algorithm that expands the deepest node first, using a stack as the data structure to store the nodes.
  - Uniform-cost search (UCS): a graph search algorithm that expands the node with the lowest path cost first, using a priority queue as the data structure to store the nodes.
  - Depth-limited search (DLS): a tree search algorithm that limits the depth of the search tree to a predefined value, and cuts off any branch that exceeds that limit.
  - Iterative deepening search (IDS): a tree search algorithm that combines the benefits of BFS and DFS, by performing a series of DLS with increasing depth limits, until a solution is found or the search space is exhausted.
  - Bidirectional search (BDS): a graph search algorithm that searches from both the initial state and the goal state simultaneously, and stops when the two search fronts meet.
- The performance of uninformed search algorithms can be measured by four criteria: completeness, optimality, time complexity, and space complexity.
- Completeness is the property of a search algorithm that guarantees to find a solution if one exists.
- Optimality is the property of a search algorithm that guarantees to find the least-cost solution among all possible solutions.
- Time complexity is the measure of how long a search algorithm takes to find a solution, in terms of the number of nodes generated or expanded.
- Space complexity is the measure of how much memory a search algorithm uses to store the nodes, in terms of the maximum size of the data structure used.
- The table below summarizes the performance of some uninformed search algorithms, assuming a branching factor of b, a solution depth of d, and a maximum depth of the search space of m.

| Algorithm | Completeness | Optimality | Time Complexity | Space Complexity |
|-----------|--------------|------------|-----------------|------------------|
| BFS       | Yes          | Yes        | O(b^d)          | O(b^d)           |
| DFS       | No           | No         | O(b^m)          | O(bm)            |
| UCS       | Yes          | Yes        | O(b^d)          | O(b^d)           |
| DLS       | No           | No         | O(b^l)          | O(bl)            |
| IDS       | Yes          | Yes        | O(b^d)          | O(bd)            |
| BDS       | Yes          | Yes        | O(b^(d/2))      | O(b^(d/2))       |

- Uninformed search is useful when the domain knowledge is scarce or unreliable, or when the search space is small and uniform.
- Uninformed search is not suitable when the search space is large and complex, or when the solution quality is important.