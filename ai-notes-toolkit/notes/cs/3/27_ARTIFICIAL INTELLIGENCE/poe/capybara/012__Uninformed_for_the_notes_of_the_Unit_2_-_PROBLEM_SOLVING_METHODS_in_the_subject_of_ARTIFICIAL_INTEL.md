### Uninformed

In the field of Artificial Intelligence, problem-solving plays a crucial role. Uninformed problem-solving methods are those where the algorithm does not have any prior knowledge about the problem or the environment. Here are some methods used for solving problems in AI:

- Breadth-First Search (BFS): This method is used to search for a solution by exploring all the nodes at the current level before moving to the next level. It is a complete algorithm and is guaranteed to find the shortest path to the solution. However, it can be memory-intensive and time-consuming.

- Depth-First Search (DFS): This method is used to search for a solution by exploring the deepest node first before backtracking to explore other nodes. It is not guaranteed to find the shortest path to the solution and can get stuck in infinite loops. However, it is memory-efficient and can be useful in specific situations.

- Iterative Deepening Search (IDS): This method is a combination of BFS and DFS. It performs DFS with a limited depth, gradually increasing the depth limit until a solution is found. It is complete, optimal, and memory-efficient, making it a popular choice for solving problems.

- Uniform-Cost Search: This method is used to search for a solution by exploring the nodes with the lowest cost first. It is optimal and guarantees finding the shortest path to the solution. However, it can be time-consuming, especially if the cost of each node is not known beforehand.

- Bidirectional Search: This method is used to search for a solution by exploring from both the initial state and the goal state simultaneously. It is an optimal algorithm and can be very efficient in finding the shortest path. However, it requires two search trees and can be complex to implement.

These are some of the methods used for uninformed problem-solving in Artificial Intelligence. Each method has its advantages and disadvantages, and the choice of algorithm depends on the specific problem to be solved.