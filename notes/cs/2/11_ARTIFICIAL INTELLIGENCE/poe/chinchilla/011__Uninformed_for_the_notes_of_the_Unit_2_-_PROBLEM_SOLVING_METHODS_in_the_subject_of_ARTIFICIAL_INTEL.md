### Uninformed Search

In artificial intelligence, solving problems is a fundamental task. Problem-solving methods help AI systems to find solutions to a given problem. One such method is uninformed search. In this method, the search algorithm does not have any information about the problem other than its initial state and the set of possible actions that can be taken from that state. The following are the characteristics and techniques of uninformed search:

- Uninformed search is also known as blind search because the algorithm does not have any information about the problem other than the initial state and possible actions.
- The search algorithm starts from the initial state and moves towards the goal state by expanding the nodes and checking if they match the goal state.
- The search algorithm uses a queue or stack to store the nodes that need to be expanded.
- There are various techniques for uninformed search, including breadth-first search, depth-first search, uniform-cost search, and iterative deepening search.
- Breadth-first search is a technique where the search algorithm explores all the nodes at a given depth before moving to the next depth. This technique is guaranteed to find the optimal solution if one exists but may take a long time and require a lot of memory.
- Depth-first search is a technique where the search algorithm explores a path as far as possible before backtracking. This technique is memory-efficient but may not find the optimal solution.
- Uniform-cost search is a technique where the search algorithm expands the node with the lowest cost first. This technique is guaranteed to find the optimal solution if the cost function is non-negative and the goal state is reachable.
- Iterative deepening search is a technique where the search algorithm performs a depth-first search with a depth limit and gradually increases the depth limit until the goal state is found.

In conclusion, uninformed search is a problem-solving method used in artificial intelligence that does not have any additional information about the problem other than the initial state and possible actions. There are various techniques for uninformed search, including breadth-first search, depth-first search, uniform-cost search, and iterative deepening search, each with its advantages and disadvantages. The choice of technique depends on the problem's nature, complexity, and available resources.