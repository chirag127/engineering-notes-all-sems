### Alpha – Beta Pruning

Alpha-Beta pruning is an optimization technique for the minimax algorithm used in decision-making processes, such as game-playing. It reduces the number of nodes that need to be evaluated in the search tree by eliminating branches that do not affect the final decision.

Here are some key points to remember about Alpha-Beta pruning:

1. Alpha-Beta pruning is applied to two-player games where one player tries to maximize their score while the other tries to minimize it.
2. The algorithm maintains two values, alpha and beta, which represent the minimum score that the maximizing player is assured of and the maximum score that the minimizing player is assured of, respectively.
3. Alpha is initialized to negative infinity and beta to positive infinity.
4. The algorithm prunes branches in the search tree by not exploring nodes that are guaranteed to not affect the final decision.
5. Alpha-Beta pruning can significantly reduce the number of nodes that need to be evaluated, resulting in faster decision-making.

This technique is commonly used in game-playing AI, such as chess and tic-tac-toe, to make the decision-making process more efficient. It is an important concept in the study of Artificial Intelligence and is covered in Unit 2 - PROBLEM SOLVING METHODS of the subject of ARTIFICIAL INTELLIGENCE KCS.