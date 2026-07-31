### Uninformed Search

Uninformed search, also known as blind search, is a type of search algorithm used in artificial intelligence for problem-solving. It is called "uninformed" because it does not use any domain-specific knowledge or heuristics to guide the search process. Instead, it relies on general search strategies to explore the search space and find a solution.

Some common uninformed search algorithms include:

1. **Breadth-first search (BFS):** This algorithm explores the search space level by level, starting from the root node and expanding all its neighbors before moving on to the next level. It is guaranteed to find the shallowest solution, but it can be slow and memory-intensive for large search spaces.

2. **Depth-first search (DFS):** This algorithm explores the search space by going as deep as possible along a branch before backtracking and exploring other branches. It is faster and less memory-intensive than BFS, but it is not guaranteed to find the shallowest solution.

3. **Uniform-cost search (UCS):** This algorithm expands the node with the lowest path cost first. It is guaranteed to find the optimal solution, but it can be slow for large search spaces.

4. **Iterative deepening search (IDS):** This algorithm combines the advantages of BFS and DFS by performing a series of depth-limited DFS searches with increasing depth limits. It is guaranteed to find the shallowest solution and is faster and less memory-intensive than BFS.

These are some of the basic uninformed search algorithms used in artificial intelligence for problem-solving. They can be useful for solving problems where domain-specific knowledge or heuristics are not available or not effective. However, they can be slow and inefficient for large or complex search spaces, and in such cases, informed search algorithms may be more effective.