### Stochastic Games

- Stochastic games are a generalization of Markov decision processes (MDPs) to the case where there are multiple agents in a common environment.
- The agents perform a joint action that defines both the reward obtained by the agents and the new state of the environment.
- The environment is assumed to be stochastic, meaning that the state transition probabilities depend only on the current state and the joint action, not on the history of the game.
- The agents are assumed to be rational, meaning that they aim to maximize their expected discounted return over time.
- Stochastic games can model various artificial intelligence applications that involve multiple agents, such as board games, robotics, autonomous driving, etc.
- Stochastic games can be classified into different types based on the information available to the agents, the structure of the game, and the objectives of the agents.
- Some common types of stochastic games are:

  - Zero-sum games: These are games where the sum of the rewards of the agents is zero for every state and joint action. In other words, one agent's gain is another agent's loss. Examples of zero-sum games are chess, go, and tic-tac-toe.
  - General-sum games: These are games where the sum of the rewards of the agents is not necessarily zero for every state and joint action. In other words, the agents can have conflicting or cooperative interests. Examples of general-sum games are prisoner's dilemma, chicken, and public goods games.
  - Perfect-information games: These are games where the agents know the current state of the environment and the actions and rewards of the other agents at every step. Examples of perfect-information games are chess, go, and backgammon.
  - Imperfect-information games: These are games where the agents do not know the current state of the environment or the actions and rewards of the other agents at every step. Examples of imperfect-information games are poker, bridge, and battleship.
  - Deterministic games: These are games where the state transition probabilities are either one or zero for every state and joint action. In other words, the outcome of the game is deterministic given the actions of the agents. Examples of deterministic games are chess, go, and tic-tac-toe.
  - Stochastic games: These are games where the state transition probabilities are between zero and one for some states and joint actions. In other words, the outcome of the game is stochastic given the actions of the agents. Examples of stochastic games are backgammon, dice, and roulette.

- The main challenge of stochastic games is to find the optimal strategies for the agents, which specify the best action to take in each state of the game.
- The optimal strategies depend on the type of the game, the information available to the agents, and the objectives of the agents.
- Some common solution concepts for stochastic games are:

  - Nash equilibrium: This is a set of strategies for the agents such that no agent can improve its expected return by deviating from its strategy, given that the other agents do not deviate from their strategies. Nash equilibrium is a general solution concept that applies to any type of stochastic game.
  - Minimax: This is a special case of Nash equilibrium for zero-sum games, where the agents try to minimize their maximum possible loss or maximize their minimum possible gain. Minimax is a pessimistic solution concept that assumes the worst-case scenario for the agents.
  - Maximin: This is another special case of Nash equilibrium for zero-sum games, where the agents try to maximize their minimum possible gain or minimize their maximum possible loss. Maximin is an optimistic solution concept that assumes the best-case scenario for the agents.
  - Pareto optimality: This is a set of strategies for the agents such that no agent can improve its expected return without making another agent worse off. Pareto optimality is a cooperative solution concept that applies to general-sum games.
  - Correlated equilibrium: This is a set of strategies for the agents such that they can coordinate their actions based on a random signal that is correlated with the optimal joint action. Correlated equilibrium is a generalization of Nash equilibrium that allows for more efficient outcomes in some games.

- There are various algorithms for finding the optimal strategies for stochastic games, depending on the type of the game, the information available to the agents, and the solution concept desired.
- Some common algorithms for stochastic games are:

  - Minimax search: This is a recursive algorithm that alternates between minimizing and maximizing the expected return of the agents at each level of the game tree. Minimax search can find the minimax or maximin strategies for zero-sum games with perfect information and deterministic outcomes