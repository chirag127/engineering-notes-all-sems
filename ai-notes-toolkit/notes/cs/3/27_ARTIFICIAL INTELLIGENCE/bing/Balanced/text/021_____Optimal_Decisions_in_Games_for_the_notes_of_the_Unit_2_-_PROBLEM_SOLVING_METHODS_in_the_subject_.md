### Optimal Decisions in Games

- In a normal search problem, the optimal solution would be a sequence of actions leading to a goal state-a terminal state that is a win .
- In a game, the optimal solution would be a strategy-a function that specifies the move to make in each situation.
- A strategy is optimal if it guarantees the best possible outcome against any opponent.
- Given a game tree, the optimal strategy can be determined from the minimax value of each node, which we write as MINIMAX(n) .
- The minimax value of a node is the utility (for MAX) of being in the corresponding state, assuming that both players play optimally from there to the end of the game .
- The minimax value of a terminal node is just the utility of the state .
- The minimax value of a non-terminal node can be computed recursively by applying the following rules :
  - If n is a MAX node, then MINIMAX(n) = max(MINIMAX(c) for c in children(n))
  - If n is a MIN node, then MINIMAX(n) = min(MINIMAX(c) for c in children(n))
- The minimax algorithm is a depth-first, exhaustive search that computes the minimax value of the root node and returns the optimal move for MAX .
- The minimax algorithm is optimal, but it is also inefficient, as it explores the entire game tree, which can be very large for complex games .
- Some techniques to improve the efficiency of the minimax algorithm are :
  - Alpha-beta pruning: a technique that eliminates branches of the game tree that are provably worse than the current best option, without affecting the minimax value of the root node.
  - Move ordering: a technique that orders the moves to be explored based on some heuristic, so that the most promising moves are explored first, increasing the chances of pruning.
  - Depth-limited search: a technique that limits the depth of the search to a fixed value, and uses an evaluation function to estimate the utility of non-terminal nodes.
  - Iterative deepening: a technique that combines depth-limited search with increasing depth limits, until the time runs out or the optimal solution is found.