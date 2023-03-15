### Optimal Decisions in Games

- In a normal search problem, the optimal solution would be a sequence of actions leading to a goal state-a terminal state that is a win .
- In a game, the optimal solution would be a strategy-a contingency plan that specifies the move for every possible situation throughout the game.
- A strategy is optimal if it guarantees the best possible outcome against any opponent strategy.
- Given a game tree, the optimal strategy can be determined from the minimax value of each node, which we write as MINIMAX(n) .
- The minimax value of a node is the utility (for MAX) of being in the corresponding state, assuming that both players play optimally from there to the end of the game .
- The minimax value of a terminal node is just the utility of the terminal state.
- The minimax value of a non-terminal node can be computed recursively from the minimax values of its children .
- If the node is a MAX node, the minimax value is the maximum of the minimax values of its children .
- If the node is a MIN node, the minimax value is the minimum of the minimax values of its children .
- The minimax algorithm is a depth-first, exhaustive search that computes the minimax values for all the nodes in the game tree .
- The minimax algorithm can be improved by using alpha-beta pruning, which eliminates branches that are provably worse than the best choice found so far .
- The minimax algorithm and alpha-beta pruning assume that the game is zero-sum, deterministic, and fully observable  .
- For games that are not zero-sum, the minimax criterion can be replaced by the maxn or the paranoid criterion.
- For games that are not deterministic, the minimax criterion can be replaced by the expectiminimax criterion, which takes into account the probabilities of chance events.
- For games that are not fully observable, the minimax criterion can be replaced by the minimax expectimax criterion, which takes into account the probabilities of hidden information.