 Here is the content in Markdown format without any emojis or external links:

### Search Strategies for the notes of the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS

1. Breadth First Search (BFS):
- Explores adjacent nodes first before going to deeper levels.
- Uses a queue data structure.
- Guarantees the shortest path.
- Complexity: O(b^d) where b is the branching factor and d is the depth of the tree.

2. Depth First Search (DFS):
- Goes deeper into the tree along each branch before backtracking.
- Uses a stack data structure.
- Does not guarantee the shortest path.
- Complexity: O(b^d) where b is the branching factor and d is the depth of the tree.

3. Greedy Best First Search:
- Estimates the cost to reach the goal and always expands the node that appears to be the best choice.
- Does not guarantee optimal solutions.
- Complexity: Difficult to analyze.

4. A* Search:
- Combines greedy and breadth first approach.
- Calculates a score (f(n)) = g(n) + h(n) to determine which node to expand next where g(n) is the real cost to reach the node and h(n) is the estimated cost to reach goal from that node.
- Guarantees optimal solutions if the heuristic (h(n)) underestimates the real cost to reach the goal.
- Complexity: O(b^d) where b is the branching factor and d is the depth of the tree.

The content is written in a formal tone with points and without any emojis or external links as requested. Please let me know if you would like me to modify or expand the content in any way.