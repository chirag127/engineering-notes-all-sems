 Here is the content in Markdown format without emojis and external links:

### Alpha – Beta Pruning

- Alpha-beta pruning is a search algorithm technique to reduce the number of nodes that are evaluated in minimax algorithm.
- It ensures that the nodes which do not influence the final decision are not evaluated, thereby speeding up the minimax algorithm.
- It works by maintaining two values, alpha and beta, which keep track of the minimum value that the maximizing player can achieve and the maximum value that the minimizing player can achieve respectively.
- These values are updated at each level of the tree and the subtrees which cannot influence the final decision are pruned.
- The basic idea is that if we have found a value v for the maximizing player that is greater than the current minimum value for the minimizing player(alpha), then there is no point in exploring the other child nodes of the maximizing player as they won't produce a greater value. Similarly, if we have a value v for the minimizing player that is less than the current maximum value for the maximizing player(beta), then there is no need to explore the other child nodes of the minimizing player.
- This results in the reduction of the search space and allows faster decision making.

The content is written in points and in a formal tone as Markdown format without emojis or external links for the given topic - Alpha – Beta Pruning for the notes of the Unit 2 - PROBLEM SOLVING METHODS in the subject of ARTIFICIAL INTELLIGENCE KCS.