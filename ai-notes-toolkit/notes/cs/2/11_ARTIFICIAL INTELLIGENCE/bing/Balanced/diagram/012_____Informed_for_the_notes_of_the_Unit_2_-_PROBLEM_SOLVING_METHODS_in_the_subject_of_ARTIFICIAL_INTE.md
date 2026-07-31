### Informed

Informed is a term used to describe a problem-solving method in artificial intelligence that uses additional information or heuristics to guide the search process towards the goal state. Informed methods are contrasted with uninformed methods, which do not use any domain-specific knowledge and rely only on the problem definition.

Some of the informed problem-solving methods in AI are:

- **Heuristic search**: A heuristic search is a search strategy that uses a heuristic function to estimate the cost or distance from the current state to the goal state. A heuristic function is a function that maps a state to a non-negative real number, which represents how close the state is to the goal. The lower the heuristic value, the more promising the state. Heuristic search algorithms use the heuristic function to rank the states in the search space and select the most promising one to expand. Examples of heuristic search algorithms are best-first search, greedy best-first search, A* search, and iterative deepening A* search  .

- **Local search**: A local search is a search strategy that operates on a single current state and moves to a neighboring state if it is better than the current state. A neighboring state is a state that can be reached by applying a single operator or action to the current state. Local search algorithms do not keep track of the path or the explored states, and they only aim to find a local optimum or a global optimum in the search space. Examples of local search algorithms are hill-climbing, simulated annealing, genetic algorithms, and tabu search  .

- **Constraint satisfaction**: A constraint satisfaction problem (CSP) is a problem that consists of a set of variables, a set of domains for each variable, and a set of constraints that specify the allowed combinations of values for the variables. A solution to a CSP is an assignment of values to all the variables that satisfies all the constraints. Constraint satisfaction is a search strategy that uses techniques such as backtracking, forward checking, arc consistency, and heuristic ordering to find a solution to a CSP or determine that no solution exists  .

- **Adversarial search**: An adversarial search is a search strategy that is used to solve problems that involve two or more agents that have conflicting goals, such as games. An adversarial search algorithm assumes that the agents take turns to make moves, and that each agent knows the state of the game and the possible moves at each point. The algorithm evaluates the outcomes of the moves using a utility function or a payoff function, which assigns a numerical value to each terminal state. The algorithm tries to find the optimal move for the agent by maximizing its utility and minimizing the utility of the opponent. Examples of adversarial search algorithms are minimax, alpha-beta pruning, and expectimax  .

: Problem Solving Techniques in AI - Javatpoint
: Problem Solving Techniques In AI | 4 Existing Problems - BlueFireFlys
: Search Algorithms in AI - Javatpoint
: Problem Solving in Artificial Intelligence - GeeksforGeeks
: An Introduction to Problem-Solving using Search Algorithms for Beginners
: Artificial Intelligence: Principles and Techniques | Course | Stanford Online