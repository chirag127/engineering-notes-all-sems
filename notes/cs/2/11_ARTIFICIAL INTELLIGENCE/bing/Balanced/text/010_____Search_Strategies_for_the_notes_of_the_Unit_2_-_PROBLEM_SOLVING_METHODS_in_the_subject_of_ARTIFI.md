### Search Strategies

- A search strategy is a method for finding a solution to a problem by exploring the space of possible states and actions.
- A search strategy consists of two components: a search algorithm and a search heuristic.
- A search algorithm is a systematic procedure that determines how to expand the search tree and which node to select for expansion.
- A search heuristic is a function that estimates the cost or distance from a node to the goal state, and guides the search algorithm towards the most promising nodes.
- There are different types of search strategies, such as uninformed search, informed search, local search, and adversarial search.
- Uninformed search strategies do not use any domain-specific knowledge or heuristic information, and rely only on the problem definition. Examples of uninformed search strategies are breadth-first search, depth-first search, uniform-cost search, and iterative deepening search.
- Informed search strategies use heuristic information to guide the search towards the goal state, and can be more efficient than uninformed search strategies. Examples of informed search strategies are greedy best-first search, A* search, and recursive best-first search.
- Local search strategies operate on a single current state and move to a neighboring state that is better than the current state, without maintaining a search tree. Local search strategies are useful for solving optimization problems, where the goal is to find the best state among many possible states. Examples of local search strategies are hill-climbing, simulated annealing, and genetic algorithms.
- Adversarial search strategies are used for solving competitive games, where the outcome depends on the actions of two or more agents. Adversarial search strategies involve maximizing the utility of one's own actions while minimizing the utility of the opponent's actions. Examples of adversarial search strategies are minimax, alpha-beta pruning, and expectimax.