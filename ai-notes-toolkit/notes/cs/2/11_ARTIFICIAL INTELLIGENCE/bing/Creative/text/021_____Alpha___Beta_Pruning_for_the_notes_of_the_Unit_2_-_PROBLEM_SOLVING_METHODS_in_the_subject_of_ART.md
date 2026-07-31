### Alpha – Beta Pruning

- Alpha-beta pruning is a search algorithm that seeks to decrease the number of nodes that are evaluated by the minimax algorithm in its search tree.
- It is an adversarial search algorithm used commonly for machine playing of two-player games (Tic-tac-toe, Chess, Connect 4, etc.).
- It is an optimization technique for the minimax algorithm, which can cut the number of game states to examine by half.
- The idea is to maintain two values, alpha and beta, which represent the minimum score that the maximizing player is assured of and the maximum score that the minimizing player is assured of respectively.
- The algorithm can prune (ignore) a branch if its value is not going to affect the final decision, that is, if it is worse than the current best option for the player.
- The algorithm can be implemented recursively, with the initial call having alpha as negative infinity and beta as positive infinity.
- The algorithm returns the best value for the current node, along with the best move to make.
- The pseudo-code for alpha-beta pruning is as follows:

```
function minimax (node, depth, alpha, beta, maximizingPlayer) is
    if depth ==0 or node is a terminal node then
        return static evaluation of node
    if MaximizingPlayer then // for Maximizer Player
        maxEva= -infinity
        for each child of node do
            eva= minimax (child, depth-1, alpha, beta, false)
            maxEva= max(maxEva, eva)
            alpha= max(alpha, eva)
            if beta <= alpha then
                break // beta cut-off
        return maxEva
    else // for Minimizer Player
        minEva= +infinity
        for each child of node do
            eva= minimax (child, depth-1, alpha, beta, true)
            minEva= min(minEva, eva)
            beta= min(beta, eva)
            if beta <= alpha then
                break // alpha cut-off
        return minEva
```