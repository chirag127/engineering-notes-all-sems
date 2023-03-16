Hello, I am Sydney, your AI assistant. I can help you with your notes on the topic of Informed Search for the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS. Here is a summary of the main points:

- Informed search is a type of search strategy that uses additional information or heuristics to guide the search process and find solutions more efficiently.
- A heuristic is a function that estimates the cost or distance from a given state to the goal state. A good heuristic should be consistent, admissible, and informative.
- Consistent means that the heuristic value of a state is never greater than the cost of reaching a neighboring state plus the heuristic value of that state.
- Admissible means that the heuristic value of a state is never greater than the actual cost of reaching the goal from that state.
- Informative means that the heuristic value of a state is close to the actual cost of reaching the goal from that state, and that different states have different heuristic values.
- Some examples of informed search algorithms are:
  - Greedy best-first search: This algorithm selects the state with the lowest heuristic value at each step, without considering the cost of reaching that state. It is fast but not optimal or complete.
  - A* search: This algorithm selects the state with the lowest sum of the cost of reaching that state and the heuristic value of that state at each step. It is optimal and complete if the heuristic is consistent and admissible, but it can be memory-intensive.
  - Iterative deepening A* search: This algorithm performs A* search with a limit on the sum of the cost and the heuristic value, and increases the limit iteratively until a solution is found. It is optimal, complete, and memory-efficient, but it can be slow.
  - Recursive best-first search: This algorithm performs a depth-first search with a limit on the sum of the cost and the heuristic value, and updates the limit based on the best alternative path. It is optimal, complete, and memory-efficient, but it can be slow and complex.
  - Beam search: This algorithm keeps a fixed number of states with the lowest sum of the cost and the heuristic value at each level, and discards the rest. It is fast and memory-efficient, but not optimal or complete.