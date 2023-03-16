### Uninformed Search

Uninformed search, also known as blind search, is a type of search algorithm used in artificial intelligence for problem-solving. It is called "uninformed" because it does not use any domain-specific knowledge or heuristics to guide the search. Instead, it explores the search space systematically until a solution is found.

Some common types of uninformed search algorithms include:

1. **Breadth-first search (BFS):** This algorithm explores the search space level by level, starting from the root node and expanding all its successors before moving on to the next level. It is guaranteed to find the shallowest solution, but it can be slow and memory-intensive for large search spaces.

2. **Depth-first search (DFS):** This algorithm explores the search space by going as deep as possible along each branch before backtracking. It is faster and uses less memory than BFS, but it is not guaranteed to find the shallowest solution.

3. **Uniform-cost search (UCS):** This algorithm expands the node with the lowest path cost first. It is guaranteed to find the optimal solution, but it can be slow for large search spaces.

4. **Iterative deepening search (IDS):** This algorithm combines the advantages of BFS and DFS by performing a series of depth-limited DFS searches with increasing depth limits. It is guaranteed to find the shallowest solution and uses less memory than BFS, but it can be slower for large search spaces.

Uninformed search algorithms are useful for problems where the solution is not known in advance and there is no domain-specific knowledge to guide the search. However, they can be slow and inefficient for large search spaces, and more informed search algorithms may be preferred in such cases.