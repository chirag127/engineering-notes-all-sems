# Search Strategies

Search strategies are methods used to solve problems in Artificial Intelligence. These strategies are used to find a solution to a problem by exploring the search space of the problem. The search space is the set of all possible solutions to the problem. The search strategies can be divided into two categories: uninformed search and informed search.

## Uninformed Search

Uninformed search strategies do not have any information about the problem other than its definition. These strategies are also known as blind search strategies. Some of the common uninformed search strategies are:

1. **Breadth-first search:** This strategy starts at the root node and explores all the neighboring nodes at the present depth level before moving on to the nodes at the next depth level.

2. **Depth-first search:** This strategy starts at the root node and explores as far as possible along each branch before backtracking.

3. **Uniform-cost search:** This strategy expands the node with the lowest path cost.

4. **Depth-limited search:** This strategy is similar to depth-first search, but the search is limited to a predetermined depth.

5. **Iterative deepening depth-first search:** This strategy is a combination of breadth-first search and depth-limited search. The search is performed iteratively with increasing depth limits until a solution is found.

## Informed Search

Informed search strategies use problem-specific knowledge to find solutions more efficiently. These strategies are also known as heuristic search strategies. Some of the common informed search strategies are:

1. **Best-first search:** This strategy uses an evaluation function to determine the order in which the nodes are expanded. The evaluation function is an estimate of the cost of the cheapest solution through the node.

2. **Greedy best-first search:** This strategy expands the node that is closest to the goal, as estimated by a heuristic function.

3. **A* search:** This strategy is a combination of uniform-cost search and greedy best-first search. The evaluation function is the sum of the path cost and the heuristic function.

4. **Recursive best-first search:** This strategy is similar to depth-first search, but it uses an evaluation function to determine the order in which the nodes are expanded.

5. **Hill-climbing search:** This strategy moves in the direction of increasing heuristic value until a local maximum is reached.

These are some of the search strategies used in Artificial Intelligence to solve problems. Each strategy has its own advantages and disadvantages, and the choice of strategy depends on the specific problem at hand.