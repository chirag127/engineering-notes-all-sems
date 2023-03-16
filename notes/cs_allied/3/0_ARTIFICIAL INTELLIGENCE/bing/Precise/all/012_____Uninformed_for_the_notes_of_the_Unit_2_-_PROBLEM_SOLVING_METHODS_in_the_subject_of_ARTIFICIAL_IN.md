# Uninformed Search

Uninformed search, also known as blind search, is a type of search algorithm used in Artificial Intelligence for traversing and searching tree or graph data structures. It is called "uninformed" because it does not have any additional information about the states beyond what is provided in the problem definition.

Some common types of uninformed search algorithms include:
- **Breadth-first search (BFS)**: This algorithm expands the shallowest node in the search tree first. It is complete and optimal for problems with a branching factor less than infinity and a finite depth.
- **Depth-first search (DFS)**: This algorithm expands the deepest node in the search tree first. It is not complete and not optimal, but has a low memory requirement.
- **Uniform-cost search**: This algorithm expands the node with the lowest path cost first. It is complete and optimal for problems with a non-negative step cost.
- **Depth-limited search**: This algorithm is similar to DFS, but with a predetermined depth limit. It is not complete and not optimal, but can be useful for problems with a large search space and unknown depth.
- **Iterative deepening depth-first search (IDDFS)**: This algorithm combines the benefits of BFS and DFS by performing a series of depth-limited searches with increasing depth limits. It is complete and optimal for problems with a branching factor less than infinity and a finite depth.

These algorithms can be used to solve a variety of problems, including pathfinding, puzzle solving, and game playing. They are generally less efficient than informed search algorithms, which use additional information to guide the search, but can still be useful in certain situations.