### Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS
#### Search Strategies

1. **Depth-first search (DFS)**: This strategy starts at the root node and explores as far as possible along each branch before backtracking.
2. **Breadth-first search (BFS)**: This strategy starts at the root node and explores all the neighboring nodes at the present depth level before moving on to the nodes at the next depth level.
3. **Uniform-cost search**: This strategy expands the node with the lowest path cost.
4. **Greedy search**: This strategy expands the node that is closest to the goal, as estimated by a heuristic function.
5. **A* search**: This strategy expands the node with the lowest value of f(n) = g(n) + h(n), where g(n) is the cost of the path from the initial state to node n and h(n) is the estimated cost of the cheapest path from n to the goal.
6. **Iterative deepening depth-first search (IDDFS)**: This strategy combines the benefits of depth-first search and breadth-first search by gradually increasing the depth limit of a depth-first search.
7. **Bidirectional search**: This strategy runs two simultaneous searches, one forward from the initial state and one backward from the goal, and stops when the two searches meet in the middle.
