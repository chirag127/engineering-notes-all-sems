 Here are the notes for Unit 2 - Problem Solving Methods in Artificial Intelligence KCS:

### Uninformed Search Methods

- Breadth First Search: Explores neighboring nodes first before going to deeper levels. Searches level by level. Uses a FIFO queue.
 pros: Guaranteed to find a solution if one exists, finds the shortest path
 cons: May explore a large number of nodes if the solution is deep.

- Depth First Search: Explores as far as possible along each branch before backtracking. Uses a LIFO stack.
 pros: May find a solution faster if it is located deep in the search space.
 cons: May not find the optimal solution and can get stuck in infinite loops.

- Iterative Deepening Depth First Search: Runs repeated DFS iterations with increasing depth limits. Combines the pros of BFS and DFS.

Notes:

- Uninformed search methods do not use any problem-specific knowledge/heuristics to guide the search.
- They guarantee to find a solution (if one exists) but may be inefficient.
- The choice of uninformed method depends on the structure of the problem space and whether shortest path or fast solution is priority.
- BFS explores breadth-wise, DFS explores depth-wise.
- IDDFS combines BFS and DFS.

The content is written in Markdown format without any emojis or external links as required. I have tried to write in a formal tone and in points as instructed. Please let me know if you would like me to modify or expand the notes in any way.