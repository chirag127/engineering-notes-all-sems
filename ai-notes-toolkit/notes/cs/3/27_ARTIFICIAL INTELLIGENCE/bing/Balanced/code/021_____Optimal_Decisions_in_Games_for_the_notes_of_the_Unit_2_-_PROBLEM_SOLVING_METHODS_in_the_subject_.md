### Optimal Decisions in Games

- In a normal search problem, the optimal solution would be a sequence of actions leading to a goal state-a terminal state that is a win .
- In a game, the optimal solution would be a strategy-a contingency plan that specifies the move for every possible situation throughout the game.
- A strategy is optimal if it guarantees the best possible outcome for a player, no matter what the opponent does.
- Given a game tree, the optimal strategy can be determined from the minimax value of each node, which we write as MINIMAX(n) .
- The minimax value of a node is the utility (for MAX) of being in the corresponding state, assuming that both players play optimally from there to the end of the game .
- The minimax value of a terminal node is just the utility of the state.
- The minimax value of a non-terminal node can be computed recursively from the minimax values of its children .
- If the node is a MAX node, the minimax value is the maximum of the minimax values of its children .
- If the node is a MIN node, the minimax value is the minimum of the minimax values of its children .
- The minimax algorithm is a depth-first, exhaustive search that computes the minimax values for all the nodes in the game tree .
- The minimax algorithm can be improved by using alpha-beta pruning, which eliminates branches of the game tree that are provably irrelevant .
- Alpha-beta pruning keeps track of two values, alpha and beta, which represent the lower and upper bounds of the possible minimax values of the nodes along the current path of the search .
- Alpha is the best value that MAX can guarantee so far, and beta is the best value that MIN can guarantee so far .
- Alpha-beta pruning can prune a branch when alpha is greater than or equal to beta, meaning that the current node cannot improve the value for the player who is to move .
- Alpha-beta pruning does not affect the correctness of the minimax algorithm, but it can reduce the number of nodes that need to be explored .
- The effectiveness of alpha-beta pruning depends on the order of the nodes in the game tree. The best case is when the best moves are examined first, and the worst case is when the best moves are examined last .
- The optimal decision for a player in a game is to choose the move that leads to the node with the highest minimax value .
- The optimal decision for a player in a game depends on the game tree, the utility function, and the opponent's strategy .