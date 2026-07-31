# Heuristics for Problem Solving Methods in Artificial Intelligence

- Heuristics are techniques that use readily accessible information to guide problem-solving processes in humans and machines .
- Heuristics can help to find faster or approximate solutions when classical methods are too slow or impractical.
- Heuristics can also help to reduce the search space of possible solutions by eliminating unlikely or suboptimal candidates.
- Heuristics are often domain-specific and depend on the nature and structure of the problem.
- Some examples of heuristic search techniques in artificial intelligence are:
  - Direct heuristic search: It includes blind search, uninformed search, and blind control strategy. It does not use any domain knowledge or heuristic function to guide the search.
  - Weak heuristic search: It includes informed search, heuristic search, and heuristic control strategy. It uses a heuristic function to estimate the cost or distance to the goal state from any given state.
  - Hill climbing algorithm: It is a technique for optimizing mathematical problems. It starts from a random state and moves to a better state by making small changes until no improvement is possible.
  - Best first search: It is a technique that expands the most promising node according to a heuristic function. It can be seen as a combination of breadth-first search and depth-first search.
  - A* search algorithm: It is a technique that combines the cost of reaching a state and the estimated cost of reaching the goal state from that state. It guarantees to find the optimal solution if the heuristic function is admissible and consistent.
- Some examples of problem types in artificial intelligence are:
  - Ignorable: In which solution steps can be ignored.
  - Recoverable: In which solution steps can be undone.
  - Irrecoverable: In which solution steps cannot be undone.