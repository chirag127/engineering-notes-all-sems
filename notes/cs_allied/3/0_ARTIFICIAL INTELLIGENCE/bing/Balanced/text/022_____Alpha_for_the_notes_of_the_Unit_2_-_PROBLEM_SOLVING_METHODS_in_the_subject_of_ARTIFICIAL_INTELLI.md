### Alpha
- Alpha is a **search algorithm** that uses **heuristic evaluation functions** to guide the search process towards the most promising states.
- Alpha is based on the **minimax principle**, which assumes that both the maximizing player (MAX) and the minimizing player (MIN) play optimally.
- Alpha uses a **depth-limited search** to explore the game tree up to a certain depth, and then applies a **static evaluation function** to estimate the value of each leaf node.
- Alpha also uses **alpha-beta pruning**, which is a technique to **eliminate** branches of the game tree that are **provably worse** than the best option found so far, thus **reducing** the number of nodes that need to be examined.
- Alpha is an example of an **adversarial search** algorithm, which is a type of search that involves **multiple agents** with **conflicting goals**. Adversarial search algorithms are often used for **two-player zero-sum games**, such as chess, checkers, tic-tac-toe, etc.