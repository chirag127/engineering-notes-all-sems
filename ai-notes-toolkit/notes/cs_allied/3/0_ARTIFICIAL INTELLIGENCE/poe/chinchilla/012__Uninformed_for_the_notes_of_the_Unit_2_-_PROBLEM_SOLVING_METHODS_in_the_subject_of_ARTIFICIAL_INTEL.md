### Uninformed Search for the Notes of the Unit 2 - PROBLEM SOLVING METHODS in the Subject of ARTIFICIAL INTELLIGENCE KCS

In the study of Artificial Intelligence, problem-solving is a fundamental task. One of the most common techniques used for problem-solving is search algorithms. Uninformed search algorithms are a type of search algorithm that does not have any information regarding the problem's domain. This means that the algorithm does not use any heuristic or prior knowledge to guide its search. In this section, we will discuss uninformed search algorithms and their different types.

#### Types of Uninformed Search Algorithms

1. Breadth-First Search (BFS): BFS is a search algorithm that explores all the neighboring nodes before moving on to the next level of nodes. It seeks to find the shallowest solution, i.e., the solution that requires the minimum number of steps. BFS is guaranteed to find the optimal solution in a tree or a graph with uniform cost.

2. Depth-First Search (DFS): DFS is a search algorithm that explores as far as possible along each branch before backtracking. It seeks to find the deepest solution, i.e., the solution that requires the maximum number of steps. DFS is not guaranteed to find the optimal solution, and it may get stuck in an infinite loop if the graph has cycles.

3. Uniform-Cost Search (UCS): UCS is a search algorithm that expands the node with the lowest cost g(n) first. The cost of a node is the sum of the costs of the path from the initial state to that node. UCS is guaranteed to find the optimal solution in a graph with a uniform cost.

4. Depth-Limited Search (DLS): DLS is a search algorithm that limits the depth of the search. It seeks to find the deepest solution within a specified depth limit. DLS is a variant of DFS and is not guaranteed to find the optimal solution.

5. Iterative-Deepening Depth-First Search (IDDFS): IDDFS is a search algorithm that combines the benefits of BFS and DFS. It performs a series of DFS with increasing depth limits, starting from the root node. IDDFS is guaranteed to find the optimal solution in a tree or a graph with uniform cost.

#### Advantages and Disadvantages of Uninformed Search Algorithms

Advantages:

- Uninformed search algorithms are simple and easy to implement.
- Uninformed search algorithms do not require any prior knowledge of the problem domain.
- Uninformed search algorithms can find a solution in a reasonable amount of time for small to medium-sized problems.

Disadvantages:

- Uninformed search algorithms may get stuck in an infinite loop if the graph has cycles.
- Uninformed search algorithms may expand too many nodes, leading to an exponential increase in search time for larger problems.
- Uninformed search algorithms cannot take advantage of any prior knowledge or heuristics to guide their search, leading to suboptimal solutions.

In conclusion, uninformed search algorithms are a simple and effective way to solve problems in Artificial Intelligence. Each type of uninformed search algorithm has its advantages and disadvantages, and their suitability depends on the problem's domain and size. Understanding the different types of uninformed search algorithms and their properties is essential for any AI practitioner.