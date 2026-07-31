Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content for the topic of Alpha – Beta Pruning for the notes of the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS:

```markdown
### Alpha – Beta Pruning

- Alpha – Beta Pruning is a search algorithm that reduces the number of nodes evaluated by the minimax algorithm in its search tree.
- It is an adversarial search technique used in two-player games, such as chess, tic-tac-toe, etc.
- It stops evaluating a move when at least one possibility has been found that proves the move to be worse than a previously examined move.
- The algorithm maintains two values, alpha and beta, which represent the minimum score that the maximizing player is assured of and the maximum score that the minimizing player is assured of respectively.
- Initially, alpha is negative infinity and beta is positive infinity, meaning that the players have no information about the possible outcome.
- As the algorithm progresses, the values of alpha and beta are updated based on the scores obtained from the child nodes.
- The pruning occurs when the value of alpha is greater than or equal to the value of beta, meaning that there is no need to explore further nodes, as the current node will not be chosen by the parent node.
- The algorithm can be applied to any game tree, but it is more effective when the nodes are ordered such that the best moves are examined first.
- The algorithm can also be implemented with iterative deepening, which allows it to search deeper and faster with the same amount of memory.
- The algorithm can be summarized as follows:

```
function alphabeta(node, depth, alpha, beta, maximizingPlayer) returns a value
  if depth = 0 or node is a terminal node then
    return the heuristic value of node
  if maximizingPlayer then
    value := -infinity
    for each child of node do
      value := max(value, alphabeta(child, depth - 1, alpha, beta, false))
      alpha := max(alpha, value)
      if alpha >= beta then
        break (* beta cut-off *)
    return value
  else
    value := +infinity
    for each child of node do
      value := min(value, alphabeta(child, depth - 1, alpha, beta, true))
      beta := min(beta, value)
      if alpha >= beta then
        break (* alpha cut-off *)
    return value
```
- The following diagram illustrates an example of alpha-beta pruning on a game tree:

![alpha-beta pruning example](https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/AB_pruning.svg/1200px-AB_pruning.svg.png)
```