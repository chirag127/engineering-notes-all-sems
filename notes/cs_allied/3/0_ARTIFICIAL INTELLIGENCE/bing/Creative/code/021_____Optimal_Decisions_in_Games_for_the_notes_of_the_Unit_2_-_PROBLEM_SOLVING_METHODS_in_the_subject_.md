### Optimal Decisions in Games

- In a normal search problem, the optimal solution would be a sequence of actions leading to a goal state-a terminal state that is a win .
- In a game, the optimal solution would be a strategy-a function that specifies the move to make in each situation .
- A strategy is optimal if it guarantees the best possible outcome against any strategy of the opponent .
- Given a game tree, the optimal strategy can be determined from the minimax value of each node, which we write as MINIMAX(n) .
- The minimax value of a node is the utility (for MAX) of being in the corresponding state, assuming that both players play optimally from there to the end of the game .
- The minimax value of a terminal node is just its utility value .
- The minimax value of a non-terminal node can be computed recursively from the minimax values of its children .
- If the node is a MAX node, the minimax value is the maximum of the minimax values of its children .
- If the node is a MIN node, the minimax value is the minimum of the minimax values of its children .
- The minimax algorithm is a depth-first, exhaustive search that computes the minimax values of all the nodes in the game tree .
- The minimax algorithm can be improved by using alpha-beta pruning, which eliminates branches that are provably worse than the best move found so far .
- The minimax algorithm and alpha-beta pruning assume that the game is zero-sum, deterministic, and fully observable  .
- For games that are not zero-sum, the minimax criterion can be replaced by the Nash equilibrium, which is a pair of strategies that are optimal for both players.
- For games that are stochastic, the minimax criterion can be replaced by the expectimax criterion, which is the expected utility of a node, taking into account the probabilities of the random outcomes.
- For games that are partially observable, the minimax criterion can be replaced by the maxmin criterion, which is the maximum of the minimum utilities of a node, taking into account the possible states of the world.