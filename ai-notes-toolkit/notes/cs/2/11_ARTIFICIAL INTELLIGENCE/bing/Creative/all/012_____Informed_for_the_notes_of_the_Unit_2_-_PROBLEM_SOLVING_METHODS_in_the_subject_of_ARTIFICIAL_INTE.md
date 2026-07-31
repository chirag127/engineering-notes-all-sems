Hello, I am Sydney, your AI assistant. I can help you with your study material. Here are some notes for the topic of Informed Search in the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS:

# Informed Search

- Informed search is a type of search strategy that uses additional information or heuristics to guide the search process towards the goal state.
- Heuristics are estimates of the cost, distance, or quality of a solution from a given state.
- Informed search algorithms are also called heuristic search algorithms, as they use heuristics to evaluate the nodes in the search space.
- Informed search algorithms can be more efficient and effective than uninformed search algorithms, as they can avoid exploring irrelevant or suboptimal paths.
- Some examples of informed search algorithms are:

  - Best-first search: a general search strategy that expands the most promising node according to a given heuristic function.
  - Greedy best-first search: a type of best-first search that uses a heuristic function that estimates the cost or distance from the current node to the goal node. It always chooses the node that is closest to the goal, regardless of the path cost.
  - A* search: a type of best-first search that uses a heuristic function that combines the cost or distance from the start node to the current node and the estimated cost or distance from the current node to the goal node. It always chooses the node that has the lowest total cost, balancing the path cost and the goal proximity.
  - Hill-climbing search: a type of local search that starts from a random initial state and moves to a neighboring state that has a higher value according to a given objective function. It terminates when it reaches a local maximum or a plateau, where no neighbor has a higher value.
  - Simulated annealing: a type of local search that starts from a random initial state and moves to a neighboring state that has a higher value or a lower value with some probability that decreases over time. It simulates the process of cooling a metal, where the temperature controls the degree of exploration. It can escape from local maxima by accepting worse moves at high temperatures, and converge to a global maximum by accepting only better moves at low temperatures.
  - Genetic algorithms: a type of population-based search that starts from a set of random initial states and applies genetic operators such as selection, crossover, and mutation to generate new states. It simulates the process of natural evolution, where the fitness function determines the survival and reproduction of the states. It can explore a large and diverse search space and converge to a near-optimal solution.