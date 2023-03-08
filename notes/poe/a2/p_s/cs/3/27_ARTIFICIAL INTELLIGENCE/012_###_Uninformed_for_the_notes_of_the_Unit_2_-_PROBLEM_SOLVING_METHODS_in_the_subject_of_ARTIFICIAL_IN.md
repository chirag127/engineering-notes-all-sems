 Here is the content in markdown format for the given topic:

### Uninformed Search Methods

Uninformed search methods do not use any problem-specific information to guide the search. They are generic methods that explore the search space systematically. Following are the commonly used uninformed search methods:

1. Breadth-First Search (BFS): In BFS, the neighbors of the start node are explored first before going to the next level neighbors. It explores the shallowest unexplored nodes first. The BFS uses a FIFO queue to expand the nodes in level order. The advantages of BFS are that it is guaranteed to find the shortest path and it does not go into infinite loops. The disadvantages are that it searches unnecessary nodes and has high memory requirements as the explored nodes cannot be discarded.

2. Depth-First Search (DFS): In DFS, the neighbors of a node are explored as far as possible before backtracking. The DFS uses a LIFO stack to expand the nodes in depth order. The advantage of DFS is that it does not consume much memory as the explored nodes can be discarded. The disadvantages are that it may go into infinite loops and does not guarantee the shortest path.

3. Bidirectional Search: The bidirectional search initializes two search trees - one grows from the start node and the other grows from the goal node. This has the advantage of finding the shortest path faster than unidirectional search. But the disadvantages are high memory requirements and the possibility of exploring redundant paths between the two search trees.

The uninformed search methods can be used when no problem-specific heuristic knowledge is available to guide the search. They can be applied to various problems like maze navigation, 8-puzzle, etc. The performance of these methods depends on the structure and nature of the search space.

[You can include diagrams and examples here to illustrate the methods]

[You can include advantages, disadvantages, applications, etc. for each method here]