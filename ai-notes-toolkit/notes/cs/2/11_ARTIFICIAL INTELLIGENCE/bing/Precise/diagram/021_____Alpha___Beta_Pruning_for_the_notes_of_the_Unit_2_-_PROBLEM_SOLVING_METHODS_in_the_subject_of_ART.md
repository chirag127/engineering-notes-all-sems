### Alpha – Beta Pruning

Alpha-Beta pruning is an optimization technique for the minimax algorithm used in decision-making processes, such as game-playing. It reduces the number of nodes that need to be evaluated in the search tree by eliminating branches that do not affect the final decision.

Here are the key points to remember about Alpha-Beta pruning:

1. Alpha-Beta pruning is applied to two-player games where one player tries to maximize their score while the other tries to minimize it.
2. The algorithm maintains two values, alpha and beta, which represent the minimum score that the maximizing player is assured of and the maximum score that the minimizing player is assured of, respectively.
3. Alpha is initialized to negative infinity and beta to positive infinity.
4. The algorithm prunes a branch when the value of the current node is worse than alpha for the maximizing player or beta for the minimizing player.
5. Alpha-Beta pruning does not affect the final result of the minimax algorithm, it only makes it faster by reducing the number of nodes that need to be evaluated.

This technique is commonly used in game-playing AI, such as chess or tic-tac-toe, to speed up the decision-making process. It can significantly reduce the time it takes for the AI to make a move, allowing it to search deeper into the game tree and make better decisions.