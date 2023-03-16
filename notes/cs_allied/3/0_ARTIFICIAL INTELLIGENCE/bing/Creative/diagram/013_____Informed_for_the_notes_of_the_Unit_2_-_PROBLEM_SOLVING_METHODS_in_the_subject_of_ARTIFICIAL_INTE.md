Hello, I am Sydney, your AI assistant. I can help you with your notes on the topic of Informed Search for the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS. Here is the content I have generated for you in markdown format:

# Informed Search

Informed search is a type of search strategy that uses additional information or heuristics to guide the search process towards the goal state. Informed search algorithms are also called heuristic search algorithms.

## Advantages of Informed Search

- Informed search can reduce the search space and the number of nodes expanded by the search algorithm, compared to uninformed search.
- Informed search can find optimal or near-optimal solutions in complex and large problems, where uninformed search may fail or take too long.
- Informed search can incorporate domain-specific knowledge and preferences into the search process, making it more flexible and adaptable.

## Disadvantages of Informed Search

- Informed search requires the availability and quality of heuristic functions, which may not be easy to design or obtain for some problems.
- Informed search may not guarantee optimality or completeness of the solution, depending on the heuristic function and the search algorithm used.
- Informed search may be affected by local optima or plateaus, where the heuristic function does not provide useful guidance or misleads the search.

## Types of Informed Search Algorithms

Some of the common informed search algorithms are:

- **Best-first search**: A general search strategy that expands the most promising node according to a heuristic function, which evaluates the quality or desirability of each node. Best-first search can be seen as a combination of breadth-first search and depth-first search, where the order of node expansion is determined by the heuristic function.
- **Greedy best-first search**: A type of best-first search that uses a heuristic function that estimates the cost or distance from the current node to the goal node. Greedy best-first search always expands the node that is closest to the goal, according to the heuristic function. Greedy best-first search is not optimal and not complete, as it may get stuck in local optima or loops.
- **A* search**: A type of best-first search that uses a heuristic function that estimates the total cost or distance from the initial node to the goal node, through the current node. A* search always expands the node that has the lowest total cost, according to the heuristic function. A* search is optimal and complete, if the heuristic function is admissible and consistent, meaning that it never overestimates the actual cost and it is monotonic.
- **Iterative deepening A* search (IDA*)**: A variation of A* search that uses iterative deepening to limit the memory usage of the search algorithm. IDA* search performs a series of depth-limited searches, where the depth limit is determined by the heuristic function. IDA* search is optimal and complete, if the heuristic function is admissible and consistent, and the depth limit is increased by a constant factor at each iteration.
- **Beam search**: A type of best-first search that uses a fixed-size queue to store the nodes to be expanded. Beam search only keeps the best k nodes in the queue, where k is the beam width. Beam search is not optimal and not complete, as it may discard promising nodes or miss the goal node. Beam search can be seen as a trade-off between breadth-first search and depth-first search, where the beam width controls the balance between exploration and exploitation.