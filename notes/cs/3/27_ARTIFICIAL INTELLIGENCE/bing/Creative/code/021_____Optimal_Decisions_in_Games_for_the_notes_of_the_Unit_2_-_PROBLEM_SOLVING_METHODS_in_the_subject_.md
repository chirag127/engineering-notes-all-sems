### Optimal Decisions in Games

- In a normal search problem, the optimal solution would be a sequence of actions leading to a goal state-a terminal state that is a win .
- In a game, the optimal solution would be a strategy-a function that specifies the move to make in each situation.
- A strategy is optimal if it guarantees the best possible outcome against any strategy of the opponent.
- Given a game tree, the optimal strategy can be determined from the minimax value of each node, which we write as MINIMAX(n) .
- The minimax value of a node is the utility (for MAX) of being in the corresponding state, assuming that both players play optimally from there to the end of the game .
- The minimax value of a terminal node is just the utility of that node.
- The minimax value of a non-terminal node is the minimum or maximum of the minimax values of its children, depending on whether it is a MIN or a MAX node .
- The minimax algorithm is a recursive procedure that computes the minimax values of all the nodes in the game tree .
- The minimax algorithm can be implemented using depth-first search with backtracking .
- The minimax algorithm is optimal, but it is also inefficient, as it explores the entire game tree, which can be exponentially large .
- Some techniques to improve the efficiency of the minimax algorithm are alpha-beta pruning, move ordering, iterative deepening, and heuristic evaluation functions .
- Alpha-beta pruning is a technique that eliminates branches of the game tree that are provably worse than the best choice found so far .
- Move ordering is a technique that sorts the moves in each node according to some heuristic, so that the best moves are examined first, increasing the chances of pruning .
- Iterative deepening is a technique that applies the minimax algorithm with increasing depth limits, until the time runs out or the optimal solution is found .
- Heuristic evaluation functions are functions that estimate the utility of a non-terminal node, based on some features of the state, such as material balance, mobility, king safety, etc .
- Heuristic evaluation functions are used to terminate the search at some depth limit, and return an approximate minimax value for the node .
- Heuristic evaluation functions should be consistent, meaning that they should not overestimate the utility of a node .