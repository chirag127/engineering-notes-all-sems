### Beta Pruning

- Beta pruning is an optimization technique for the minimax algorithm, which is used to find the optimal move in a two-player game.
- The minimax algorithm evaluates the game tree by assigning a value to each node, which represents the best possible outcome for the player at that node.
- The minimax algorithm alternates between maximizing and minimizing the value of the nodes, depending on whose turn it is to move.
- The alpha-beta pruning technique improves the efficiency of the minimax algorithm by eliminating the nodes that are not relevant for the final decision.
- The alpha-beta pruning technique uses two parameters, alpha and beta, to keep track of the lower and upper bounds of the possible values of the nodes.
- Alpha is the best value that the maximizing player can guarantee at that level or above. Beta is the best value that the minimizing player can guarantee at that level or below.
- The initial value of alpha is -infinity and the initial value of beta is +infinity.
- The alpha-beta pruning technique prunes a node when alpha becomes greater than or equal to beta, which means that the node cannot improve the value of the parent node and is therefore irrelevant.
- The alpha-beta pruning technique can reduce the number of nodes that need to be evaluated by a large factor, which allows the algorithm to search deeper in the game tree and find better moves.