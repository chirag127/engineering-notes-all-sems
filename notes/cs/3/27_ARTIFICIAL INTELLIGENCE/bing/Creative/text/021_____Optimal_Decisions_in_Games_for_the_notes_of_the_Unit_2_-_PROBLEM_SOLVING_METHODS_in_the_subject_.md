### Optimal Decisions in Games

- In a normal search problem, the optimal solution would be a sequence of actions leading to a goal state-a terminal state that is a win .
- In a game, the optimal solution would be a strategy-a function that specifies the move to make in every possible situation.
- A strategy is optimal if it guarantees the best possible outcome against any other strategy.
- Given a game tree, the optimal strategy can be determined from the minimax value of each node, which we write as MINIMAX(n) .
- The minimax value of a node is the utility (for MAX) of being in the corresponding state, assuming that both players play optimally from there to the end of the game .
- The minimax value of a terminal node is just the utility of that node .
- The minimax value of a non-terminal node can be computed recursively from the minimax values of its children .
- If the node is a MAX node, the minimax value is the maximum of the minimax values of its children .
- If the node is a MIN node, the minimax value is the minimum of the minimax values of its children .
- The minimax algorithm is a depth-first, exhaustive search that computes the minimax values of all the nodes in the game tree .
- The minimax algorithm can be improved by using alpha-beta pruning, which eliminates branches that are provably worse than the best option found so far .
- The minimax algorithm can also be improved by using heuristic evaluation functions, which estimate the utility of a state without expanding the whole subtree below it .
- The minimax algorithm can be applied to different types of games, such as perfect information games, imperfect information games, stochastic games, and multiplayer games, with some modifications .
- The minimax algorithm is an example of game playing in artificial intelligence, which is the study of how to design agents that can play games intelligently.