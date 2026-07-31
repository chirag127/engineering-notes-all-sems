### Uninformed Search

Uninformed search, also known as blind search, is a type of search algorithm used in Artificial Intelligence for traversing and searching tree or graph data structures. It is called "uninformed" because it does not have any additional information about the states beyond what is provided in the problem definition.

Some common types of uninformed search algorithms include:

1. **Breadth-first search (BFS)**: This algorithm explores all the neighboring nodes at the present depth level before moving on to the nodes at the next depth level.

2. **Depth-first search (DFS)**: This algorithm explores as far as possible along each branch before backtracking.

3. **Uniform-cost search**: This algorithm expands the node with the lowest path cost.

4. **Iterative deepening depth-first search (IDDFS)**: This algorithm combines the benefits of DFS and BFS by performing DFS to a limited depth, and gradually increasing the depth limit until the goal is found.

Uninformed search algorithms are generally not preferred for large, complex problems as they can be slow and inefficient. However, they can be useful for smaller problems or as a starting point for more advanced search algorithms.