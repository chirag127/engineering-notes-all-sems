# Alpha-Beta Pruning

- Alpha-beta pruning is a search algorithm that seeks to decrease the number of nodes that are evaluated by the minimax algorithm in its search tree.
- It is an adversarial search algorithm used commonly for machine playing of two-player games (Tic-tac-toe, Chess, Connect 4, etc.).
- It is an optimization technique for the minimax algorithm, which can cut the number of game states to examine by half.
- It works by assigning two values, alpha and beta, to each node in the search tree, which represent the minimum score that the maximizing player is assured of and the maximum score that the minimizing player is assured of respectively.
- The algorithm maintains these values and updates them as it traverses the tree. It prunes (ignores) any branch that cannot possibly improve the score of the player whose turn it is to move.
- The algorithm can be implemented recursively as follows:

```
function minimax (node, depth, alpha, beta, maximizingPlayer) is
    if depth == 0 or node is a terminal node then
        return static evaluation of node
    if maximizingPlayer then
        // for Maximizer Player
        maxEva = -infinity
        for each child of node do
            eva = minimax (child, depth - 1, alpha, beta, false)
            maxEva = max(maxEva, eva)
            alpha = max(alpha, eva)
            if beta <= alpha then
                break // beta cut-off
        return maxEva
    else
        // for Minimizer Player
        minEva = +infinity
        for each child of node do
            eva = minimax (child, depth - 1, alpha, beta, true)
            minEva = min(minEva, eva)
            beta = min(beta, eva)
            if beta <= alpha then
                break // alpha cut-off
        return minEva
```

- The algorithm can be visualized using a game tree, where each node represents a game state and each edge represents a possible move. The leaf nodes are assigned values based on the outcome of the game from that state. The algorithm then propagates these values up the tree, using the minimax principle, and prunes any branch that does not affect the final decision.
- An example of alpha-beta pruning on a game tree is shown below:

![alpha-beta pruning example](https://www.mygreatlearning.com/blog/wp-content/uploads/2021/10/Alpha-Beta-Pruning-Example.png)

- In this example, the algorithm starts from the leftmost branch and assigns alpha and beta values to each node. The root node has alpha = -infinity and beta = +infinity. The algorithm then updates these values as it explores the tree. For example, when it reaches node B, it updates alpha to 3, since that is the best score that the maximizer can get from that branch. When it reaches node C, it updates beta to 2, since that is the worst score that the minimizer can get from that branch. Since beta is less than or equal to alpha at node C, the algorithm can prune the remaining branches of node C, as they cannot improve the score for either player. Similarly, the algorithm can prune the branches of node F and node I, as they also have beta less than or equal to alpha. The final value of the root node is 5, which is the best score that the maximizer can achieve.

- The benefits of alpha-beta pruning are that it can reduce the time and space complexity of the minimax algorithm, as it does not need to explore all possible branches of the search tree. It can also improve the quality of the search, as it can focus on the most promising branches and avoid wasting time on irrelevant ones.
- The drawbacks of alpha-beta pruning are that it still depends on the order of the branches, as it can prune more branches if they are ordered from best to worst or from worst to best, depending on the player. It also does not guarantee to find the optimal solution, as it may prune some branches that contain better moves than the ones explored.