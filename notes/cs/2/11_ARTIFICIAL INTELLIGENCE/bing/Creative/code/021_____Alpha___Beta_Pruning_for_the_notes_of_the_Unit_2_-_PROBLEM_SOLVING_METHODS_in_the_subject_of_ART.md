Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Alpha – Beta Pruning for the notes of the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS:

```markdown
### Alpha – Beta Pruning

- Alpha – Beta Pruning is an optimization technique for minimizing the number of nodes evaluated by the minimax algorithm in a game tree.
- It reduces the search space by eliminating the branches that are not relevant for the optimal decision.
- It is based on the idea that if a player has a better move available, he or she will not choose a worse one.
- It uses two values, alpha and beta, to keep track of the lower and upper bounds of the best move for each player.
- Alpha is the best value that the maximizing player can guarantee so far, and beta is the best value that the minimizing player can guarantee so far.
- Initially, alpha is set to negative infinity and beta is set to positive infinity.
- The algorithm works as follows:

  - Start from the root node and apply the minimax algorithm recursively.
  - At each node, compare the current value with alpha and beta values.
  - If the current value is greater than or equal to beta at a maximizing node, or less than or equal to alpha at a minimizing node, then stop expanding that node and return the current value. This is called a cutoff.
  - Otherwise, update alpha or beta value according to the current value and the type of node (maximizing or minimizing).
  - Return the best value found at the root node as the optimal decision.

- The following diagram illustrates the alpha – beta pruning algorithm on a game tree:

```
![alpha-beta-pruning](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/AB_pruning.svg/1200px-AB_pruning.svg.png)
```

- The nodes marked with X are pruned, as they are not relevant for the optimal decision.
- The optimal value for the root node is 5, and the optimal move is B.
- The algorithm evaluates only 11 nodes out of 21, reducing the search space by almost 50%.
- The effectiveness of alpha – beta pruning depends on the order of the nodes. If the best moves are examined first, then more nodes can be pruned.
- A heuristic function can be used to order the nodes based on some criteria, such as the number of possible moves, the material advantage, the board position, etc.
- Alpha – beta pruning does not affect the correctness of the minimax algorithm, as it only eliminates the nodes that do not influence the final decision.
- It is a widely used technique for implementing artificial intelligence in games, such as chess, checkers, tic-tac-toe, etc.
```