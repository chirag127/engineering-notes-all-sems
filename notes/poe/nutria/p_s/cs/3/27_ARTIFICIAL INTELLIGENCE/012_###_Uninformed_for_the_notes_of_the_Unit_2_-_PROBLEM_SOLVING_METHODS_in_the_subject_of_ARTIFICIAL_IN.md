
### Uninformed for the notes of the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS

Uninformed search methods, also known as blind search, are problem-solving techniques used in Artificial Intelligence (AI) that do not require any knowledge about the problem domain. Instead, these methods rely on a simple, brute-force approach to explore the search space. Uninformed search algorithms are typically used to solve problems that have a large search space and no information about the goal state.

Uninformed search algorithms can be divided into two categories: **breadth-first search** and **depth-first search**.

**Breadth-first search** (BFS) is an algorithm that starts at the root node of a tree and explores all of the neighbor nodes at the present depth before moving on to the nodes at the next depth level. It uses a queue to keep track of the nodes that need to be explored.

**Depth-first search** (DFS) is an algorithm that starts at the root node of a tree and explores as far as possible along each branch before backtracking. It uses a stack to keep track of the nodes that need to be explored.

Both of these algorithms have their advantages and disadvantages. BFS is complete and optimal, meaning it will always find the shortest path to the goal state. However, it is also very memory-intensive and can be slow for large search spaces. DFS is much faster and more memory-efficient, but it is not complete or optimal and can get stuck in an infinite loop.

Uninformed search algorithms are used in many areas, such as robotics, natural language processing, and game playing. For example, they can be used to solve the traveling salesman problem, where the goal is to find the shortest path between a set of cities.