### Beta Pruning

- Beta pruning is an optimization technique for the minimax algorithm, which is used to find the optimal move in a two-player game.
- The minimax algorithm evaluates the game tree by assigning a value to each node, which represents the best possible outcome for the player at that node.
- The minimax algorithm alternates between maximizing and minimizing the value of the nodes, depending on whose turn it is.
- The value of a node is determined by either the utility function (if it is a terminal node) or the value of its children (if it is a non-terminal node).
- The value of a non-terminal node is the maximum of its children's values if it is a maximizing node, or the minimum of its children's values if it is a minimizing node.
- Beta pruning is based on the idea that some nodes can be ignored (pruned) if they do not affect the final decision of the minimax algorithm.
- Beta pruning uses two variables, alpha and beta, to keep track of the best value found so far by the maximizing and minimizing players, respectively.
- Alpha is initialized to -infinity and beta is initialized to +infinity.
- Alpha is updated whenever a new maximum value is found by the maximizing player, and beta is updated whenever a new minimum value is found by the minimizing player.
- A node can be pruned if its value is less than or equal to alpha (for a maximizing node) or greater than or equal to beta (for a minimizing node).
- This means that the node's value is worse than the best value already found by the opponent, and therefore it will not be chosen by the current player.
- Beta pruning reduces the number of nodes that need to be evaluated by the minimax algorithm, and thus improves its efficiency and speed.