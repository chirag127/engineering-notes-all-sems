 Here is the content in markdown format without any emojis or external links and in a formal tone:

### Search Strategies for the notes of the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS

1. Breadth First Search:
- Exploring all neighboring nodes of a root node before moving to the next level neighbors.
- Useful for searching in unweighted graphs.
- Guaranteed to find a solution if one exists.
- Not efficient if the goal node is deep within the graph.

2. Depth First Search:
- Exploring a single path as far as possible before backtracking.
- Useful for searching in weighted graphs and finding all possible paths/solutions.
- Not guaranteed to find an optimal solution.
- Uses extra space for storing the explored and unexplored paths.

3. Greedy Best First Search:
- Always expanding the node that appears to be the closest to the goal based on a heuristic function.
- Fast but not guaranteed to find the optimal solution.
- The choice of heuristic function impacts the performance.

4. A* Search:
- Combines greedy and breadth first search.
- Explores the node that minimizes `f(n) = g(n) + h(n)` where `g(n)` is the cost from start to current node `n` and `h(n)` is the heuristic estimate of cost from `n` to goal.
- Guaranteed to find an optimal solution if the heuristic function is consistent and admissible.
- Generally the most efficient search algorithm.