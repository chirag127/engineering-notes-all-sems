### Alpha – Beta Pruning

- Alpha-beta pruning is a **search algorithm** that seeks to **decrease the number of nodes** that are evaluated by the **minimax algorithm** in its search tree.
- It is an **adversarial search algorithm** used commonly for machine playing of **two-player games** (Tic-tac-toe, Chess, Connect 4, etc.).
- It is an **optimization technique** for the minimax algorithm that **cuts off** the branches of the search tree that are **not relevant** for the final decision.
- It uses two parameters, **alpha** and **beta**, to keep track of the **best value** for the **maximizing player** and the **minimizing player** respectively.
- Alpha is the **maximum lower bound** of possible solutions, and beta is the **minimum upper bound** of possible solutions.
- The algorithm **prunes** a branch when the value of the node becomes **less than alpha** or **greater than beta**.
- The algorithm can be implemented using a **recursive function** that takes the node, the depth, the alpha, the beta, and the maximizing player as arguments.
- The algorithm returns the **static evaluation** of the node if the depth is zero or the node is a **terminal node**.
- The algorithm updates the alpha and beta values based on the **evaluation** of the child nodes and the **maximizing or minimizing player**.
- The algorithm **stops exploring** a branch if the alpha value is **greater than or equal to** the beta value, as this means that the branch will not affect the final decision.
- The algorithm can **improve the efficiency** of the minimax algorithm by **reducing the search space**.
- The algorithm can also **improve the performance** of the machine playing the game by **allowing deeper search** within the same time limit.
- The algorithm can be **illustrated** using a **tree diagram** that shows the nodes, the values, the alpha and beta values, and the pruned branches.