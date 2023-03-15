### Alpha – Beta Pruning

Alpha-Beta pruning is an optimization technique for the minimax algorithm used in decision-making processes, such as game-playing. It is a search algorithm that seeks to decrease the number of nodes evaluated by the minimax algorithm in its search tree. It is an adversarial search algorithm used commonly for machine playing of two-player games.

Here are the key points to remember about Alpha-Beta pruning:

1. Alpha-Beta pruning is an optimization technique for the minimax algorithm.
2. It reduces the number of nodes evaluated by the minimax algorithm in its search tree.
3. It is an adversarial search algorithm used commonly for machine playing of two-player games.
4. Alpha represents the maximum lower bound of possible solutions.
5. Beta represents the minimum upper bound of possible solutions.
6. The algorithm maintains two values, alpha and beta, which represent the minimum score that the maximizing player is assured of and the maximum score that the minimizing player is assured of respectively.
7. The algorithm terminates its search at a node when the value of that node can be determined to be worse for the player whose turn it is to move than the current best value for that player.
8. Alpha-Beta pruning can be applied to trees of any depth and can be used in conjunction with any heuristic evaluation function.
