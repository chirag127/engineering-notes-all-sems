### Optimal Decisions in Games

- In a normal search problem, the optimal solution would be a sequence of actions leading to a goal state-a terminal state that is a win .
- In a game, the optimal solution would be a strategy-a function that specifies the move to make in each situation.
- A strategy is optimal if it guarantees the best possible outcome against any strategy of the opponent.
- Given a game tree, the optimal strategy can be determined from the minimax value of each node, which we write as MINIMAX(n) .
- The minimax value of a node is the utility (for MAX) of being in the corresponding state, assuming that both players play optimally from there to the end of the game .
- The minimax value of a terminal node is just the utility of that node.
- The minimax value of a non-terminal node is the minimum or maximum of the minimax values of its children, depending on whether the node is a MIN or a MAX node .
- The minimax algorithm is a recursive procedure that computes the minimax value of each node by performing a depth-first search of the game tree .
- The minimax algorithm can be improved by using alpha-beta pruning, which is a technique that eliminates branches of the game tree that are provably worse than the current best option .
- Alpha-beta pruning maintains two values, alpha and beta, that represent the lower and upper bounds of the possible minimax values of the nodes along the current path of the search .
- Alpha-beta pruning can prune a branch when alpha is greater than or equal to beta, meaning that the current node cannot improve the minimax value of its parent .
- Alpha-beta pruning can reduce the effective branching factor of the game tree, making the search more efficient .
- Game playing in artificial intelligence can also use other methods, such as rule-based systems and machine learning-based systems.
- Rule-based systems use a set of fixed rules to play the game, whereas machine learning-based systems use algorithms to learn from experience and make decisions based on that experience.
- Some examples of rule-based systems are chess programs that use heuristics and evaluation functions to guide the search.
- Some examples of machine learning-based systems are neural networks and reinforcement learning agents that learn from self-play or human data.