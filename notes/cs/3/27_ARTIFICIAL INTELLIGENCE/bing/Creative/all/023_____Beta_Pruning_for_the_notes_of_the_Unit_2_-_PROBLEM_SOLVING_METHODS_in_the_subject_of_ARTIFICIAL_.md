# Beta Pruning for the notes of the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS

- Beta pruning is an optimization technique for the minimax algorithm, which is used to find the optimal move in a two-player game.
- The minimax algorithm evaluates the game tree by assigning a value to each node, which represents the best possible outcome for the player at that node.
- The minimax algorithm alternates between two types of nodes: max nodes, where the player tries to maximize the value, and min nodes, where the player tries to minimize the value.
- The minimax algorithm explores the game tree in a depth-first manner, and backtracks when it reaches a terminal node or a predefined depth limit.
- The minimax algorithm can be improved by using alpha-beta pruning, which eliminates the branches of the game tree that are not relevant for the final decision.
- Alpha-beta pruning uses two parameters, alpha and beta, to keep track of the lower and upper bounds of the possible values at each node.
- Alpha is the best value that the max player can guarantee at that level or above, and beta is the best value that the min player can guarantee at that level or below.
- The initial values of alpha and beta are -infinity and +infinity, respectively.
- The alpha-beta pruning algorithm works as follows:
  - At a max node, if the value of the node is greater than or equal to beta, then the node is pruned, as the min player will never choose this branch.
  - At a min node, if the value of the node is less than or equal to alpha, then the node is pruned, as the max player will never choose this branch.
  - Otherwise, the value of the node is updated with the maximum or minimum of its children, and the alpha or beta value is updated accordingly.
- Alpha-beta pruning does not change the final result of the minimax algorithm, but it reduces the number of nodes that need to be evaluated, thus making the algorithm faster and more efficient.
- Alpha-beta pruning can be applied to any game tree that satisfies the following properties:
  - The game tree is finite and has a fixed branching factor.
  - The game tree is ordered, meaning that the children of a node are sorted by their values in decreasing order for max nodes and increasing order for min nodes.
  - The evaluation function is consistent, meaning that it does not change the relative order of the nodes at different levels of the game tree.