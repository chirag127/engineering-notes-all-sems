### Beta Pruning

Beta pruning is a search algorithm that seeks to decrease the number of nodes that are evaluated by the minimax algorithm in its search tree. It is an adversarial search algorithm used commonly for machine playing of two-player games (Tic-tac-toe, Chess, Go, etc.). It stops evaluating a move when at least one possibility has been found that proves the move to be worse than a previously examined move. Such moves need not be evaluated further. When applied to a standard minimax tree, it returns the same move as minimax would, but prunes away branches that cannot possibly influence the final decision.

Here are some key points to remember about Beta pruning:
- It is a type of minimax algorithm.
- It is used to speed up the search process by eliminating irrelevant branches.
- It is commonly used in two-player games.
- It returns the same move as the minimax algorithm, but is more efficient.
