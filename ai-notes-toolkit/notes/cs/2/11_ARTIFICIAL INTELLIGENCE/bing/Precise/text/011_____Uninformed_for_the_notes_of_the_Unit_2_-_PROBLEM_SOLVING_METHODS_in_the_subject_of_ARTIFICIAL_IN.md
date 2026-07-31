### Uninformed Search

Uninformed search, also known as blind search, is a search strategy that does not use any problem-specific knowledge. It is a basic search method that is used to solve problems where little to no information is available about the search space. Uninformed search methods include:

1. **Breadth-first search (BFS):** This method explores all the nodes at the present depth level before moving on to the nodes at the next depth level.

2. **Depth-first search (DFS):** This method explores as far as possible along each branch before backtracking.

3. **Uniform-cost search (UCS):** This method expands the node with the lowest path cost.

4. **Depth-limited search (DLS):** This method is similar to DFS, but the search is limited to a predetermined depth.

5. **Iterative deepening depth-first search (IDDFS):** This method is a combination of BFS and DFS. It performs a DFS to a limited depth, and if the goal is not found, the depth is increased and the search is repeated.

Uninformed search methods are generally less efficient than informed search methods, which use problem-specific knowledge to guide the search. However, uninformed search methods can still be useful in certain situations where little to no information is available about the search space.