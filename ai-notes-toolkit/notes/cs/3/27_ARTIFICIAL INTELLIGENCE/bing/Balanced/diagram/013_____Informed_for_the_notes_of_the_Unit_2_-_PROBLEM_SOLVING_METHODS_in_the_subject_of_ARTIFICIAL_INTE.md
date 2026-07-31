### Informed Search

- Informed search is a type of search algorithm that uses additional information to guide the search process, allowing for more efficient problem-solving compared to uninformed search algorithms  .
- This information can be in the form of heuristics, estimates of cost, or other relevant data to prioritize which states to expand and explore  .
- Informed search algorithms are also called heuristic search algorithms, as they use a heuristic function to evaluate the quality of each state.
- A heuristic function is a function that estimates the cost of reaching the goal from a given state, based on some domain knowledge or intuition .
- The lower the heuristic value, the more promising the state is for reaching the goal.
- Some examples of informed search algorithms are:
  - Best-first search: a search algorithm that uses a priority queue or heap to store the states with the lowest heuristic value, and expands the most promising state first.
  - Greedy search: a special case of best-first search that uses only the heuristic function to evaluate the states, ignoring the actual cost of reaching them.
  - A* search: a search algorithm that combines the heuristic function and the actual cost of reaching the state, and expands the state with the lowest sum of both values.
  - Hill-climbing search: a search algorithm that starts from a random state and moves to a neighboring state with a lower heuristic value, until it reaches a local minimum or maximum.
  - Beam search: a search algorithm that keeps a fixed number of states with the lowest heuristic value in memory, and expands only those states in each iteration.