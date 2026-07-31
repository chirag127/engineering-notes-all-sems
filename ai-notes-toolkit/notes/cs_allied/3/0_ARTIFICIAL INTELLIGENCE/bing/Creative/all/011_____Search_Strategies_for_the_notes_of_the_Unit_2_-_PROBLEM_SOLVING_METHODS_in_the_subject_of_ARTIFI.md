# Search Strategies for the notes of the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS

- Search strategies are methods to find solutions to problems in artificial intelligence (AI)   .
- Search strategies can be classified into two types: uninformed search and informed search .
- Uninformed search strategies do not use any domain-specific knowledge or heuristic information to guide the search. They only use the problem definition, which consists of the initial state, the goal state, and the possible actions .
- Informed search strategies use heuristic information or domain-specific knowledge to estimate the cost or the likelihood of reaching the goal state from a given state. They try to find the optimal or the most efficient solution  .
- Some of the common uninformed search strategies are:
  - Depth-first search (DFS): It explores the deepest node in the search tree first, then backtracks to explore other branches. It uses a stack data structure to store the nodes .
  - Breadth-first search (BFS): It explores the nodes in the order of their distance from the root node, i.e., level by level. It uses a queue data structure to store the nodes .
  - Depth-limited search (DLS): It is a variation of DFS that limits the depth of the search tree to a predefined value. It avoids infinite loops and memory issues .
  - Uniform-cost search (UCS): It explores the nodes in the order of their path cost from the root node, i.e., the lowest cost first. It uses a priority queue data structure to store the nodes .
  - Iterative deepening depth-first search (IDDFS): It is a combination of DFS and DLS that iteratively increases the depth limit until the goal is found or the search space is exhausted. It combines the advantages of DFS and BFS .
  - Bidirectional search (BDS): It simultaneously searches from the initial state and the goal state, and stops when the two searches meet. It reduces the search space and the time complexity  .
- Some of the common informed search strategies are:
  - Greedy search (best-first search): It expands the node that appears to be closest to the goal state, according to a heuristic function. It is fast but not optimal  .
  - A* search: It expands the node that has the lowest estimated total cost, which includes the cost of reaching the node and the cost of reaching the goal from the node, according to a heuristic function. It is optimal and complete, but can be memory-intensive  .
  - Hill-climbing search: It is a local search algorithm that moves from the current state to a better state, according to a heuristic function. It terminates when it reaches a local maximum or a plateau. It is simple but can get stuck in local optima .
  - Simulated annealing: It is a variation of hill-climbing search that allows some random moves to escape from local optima. It gradually reduces the probability of random moves as the search progresses, mimicking the cooling process of metals. It can find a global optimum with high probability .
  - Genetic algorithms: They are population-based search algorithms that use the principles of natural selection and evolution to generate new solutions. They use operators such as crossover, mutation, and selection to manipulate a set of candidate solutions. They can find near-optimal solutions for complex problems .
- Search algorithms are useful for solving various AI tasks, such as planning, scheduling, optimization, game playing, natural language processing, computer vision, etc.  .