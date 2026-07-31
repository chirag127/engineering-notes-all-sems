Hello, I am Sydney, your AI assistant. I can help you with your notes on optimal decisions in games for the unit 2 of artificial intelligence KCS. Here is a summary of the topic:

### Optimal Decisions in Games

- A game is a kind of search problem where two or more agents (players) take turns to perform actions that affect the state of the game.
- The goal of each player is to reach a terminal state (a win, a loss, or a draw) that maximizes their utility (a numerical value that represents their preference).
- In a normal search problem, the optimal solution is a sequence of actions leading to a goal state. In a game, the optimal solution is a strategy, a function that specifies what action to take in each state.
- A strategy is optimal if it guarantees the best possible outcome for a player, no matter what the other players do.
- Given a game tree, the optimal strategy can be determined from the minimax value of each node, which is the utility (for MAX) of being in the corresponding state, assuming that both players play optimally from there to the end of the game.
- The minimax value of a node can be computed recursively by applying the following rules:
  - If the node is a terminal node, return the utility of the node.
  - If the node is a MAX node, return the maximum of the minimax values of its children.
  - If the node is a MIN node, return the minimum of the minimax values of its children.
- The minimax algorithm is a way of implementing the minimax value computation using depth-first search. It can be improved by using alpha-beta pruning, a technique that eliminates branches of the game tree that are provably irrelevant.
- The minimax algorithm assumes that the game is zero-sum (the utility values at the end of the game are always equal and opposite), deterministic (the outcome of each action is certain), and fully observable (the state of the game is known to both players).
- In reality, many games are not zero-sum, deterministic, or fully observable. To deal with these situations, some extensions of the minimax algorithm are:
  - For non-zero-sum games, use the maxn algorithm, which computes the utility vector (a list of utilities for each player) of each node and returns the maximum component for the current player.
  - For stochastic games, use the expectiminimax algorithm, which computes the expected utility of each node by averaging over the possible outcomes of each action, weighted by their probabilities.
  - For partially observable games, use the paranoid algorithm, which assumes that the other players know the state of the game and act to minimize the current player's utility.