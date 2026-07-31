Hello, I am Sydney, your AI assistant. I can help you with your notes on the topic of Informed Search for the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS. Here is the content in markdown format:

# Informed Search

- Informed search is a type of search strategy that uses additional information or heuristics to guide the search process towards the goal state.
- Heuristics are functions that estimate the cost or distance from a given state to the goal state, based on some domain knowledge or intuition.
- Informed search algorithms are also called heuristic search algorithms, as they use heuristics to select the most promising state to expand at each step.
- Informed search algorithms can be more efficient and effective than uninformed search algorithms, as they can avoid exploring irrelevant or suboptimal paths.
- Some examples of informed search algorithms are:

  - Best-first search: a general search strategy that selects the state with the lowest heuristic value to expand at each step. It can be seen as a combination of breadth-first search and depth-first search, as it balances exploration and exploitation.
  - Greedy best-first search: a special case of best-first search that only considers the heuristic value of the current state, ignoring the cost of the path so far. It is very fast and aggressive, but can be incomplete or suboptimal, as it can get stuck in local minima or dead ends.
  - A* search: a special case of best-first search that considers both the heuristic value of the current state and the cost of the path so far. It is optimal and complete, as long as the heuristic function is admissible and consistent. An admissible heuristic never overestimates the true cost to the goal, and a consistent heuristic satisfies the triangle inequality.
  - Iterative deepening A* search: a variation of A* search that uses a depth limit and increases it gradually until the goal is found or the search space is exhausted. It is useful when the search space is large or infinite, as it can save memory and avoid infinite loops.
  - Recursive best-first search: a variation of A* search that uses a recursive algorithm and a memory-bound to keep track of the best alternative path at each level of the search tree. It is useful when the search space is large or infinite, as it can save memory and avoid infinite loops.
  - Beam search: a variation of best-first search that uses a fixed-size queue to store the best states at each level of the search tree. It is useful when the search space is large or infinite, as it can save memory and avoid exploring unpromising paths. However, it can be incomplete or suboptimal, as it can lose the optimal path due to the limited queue size.