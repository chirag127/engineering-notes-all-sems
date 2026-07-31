### Optimal Decisions in Games

- In a normal search problem, the optimal solution would be a sequence of actions leading to a goal state-a terminal state that is a win .
- In a game, the optimal solution would be a strategy-a contingency plan that specifies the move for every possible situation throughout the game.
- A strategy is optimal if it guarantees the best possible outcome against any strategy of the opponent.
- Given a game tree, the optimal strategy can be determined from the minimax value of each node, which we write as MINIMAX(n) .
- The minimax value of a node is the utility (for MAX) of being in the corresponding state, assuming that both players play optimally from there to the end of the game .
- The minimax value of a terminal node is just the utility of that node .
- The minimax value of a non-terminal node is the minimum or maximum of the minimax values of its children, depending on whether the node is a MIN or a MAX node .
- The minimax algorithm is a recursive procedure that computes the minimax values of all the nodes in the game tree .
- The minimax algorithm can be implemented using depth-first search with backtracking .
- The minimax algorithm is optimal, but it is also inefficient, as it explores the entire game tree, which can be very large .
- Some techniques to improve the efficiency of the minimax algorithm are alpha-beta pruning, move ordering, iterative deepening, and heuristic evaluation functions  .