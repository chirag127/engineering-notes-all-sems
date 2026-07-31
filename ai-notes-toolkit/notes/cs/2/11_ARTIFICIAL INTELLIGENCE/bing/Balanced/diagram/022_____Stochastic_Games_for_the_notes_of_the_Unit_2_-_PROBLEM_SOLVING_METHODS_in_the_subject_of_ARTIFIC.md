### Stochastic Games

- Stochastic games are a generalization of Markov decision processes (MDPs) to the case where there are multiple agents in a common environment.
- The agents perform a joint action that defines both the reward obtained by the agents and the new state of the environment.
- The environment is assumed to be stochastic, meaning that the state transition probabilities depend only on the current state and the joint action, not on the history of the game.
- The agents are assumed to be rational, meaning that they aim to maximize their expected discounted return over time.
- Stochastic games can model various artificial intelligence applications that involve multi-agent interaction, such as playing chess and Go, autonomous driving, and robotics.
- Stochastic games can be classified into different types based on the information available to the agents, the structure of the game, and the objectives of the agents.
- Some common types of stochastic games are:

  - Zero-sum games: These are games where the sum of the rewards of all the agents is zero for every state and joint action. In other words, one agent's gain is another agent's loss. Examples of zero-sum games are chess and Go.
  - General-sum games: These are games where the sum of the rewards of all the agents is not necessarily zero for every state and joint action. In other words, the agents can have conflicting or cooperative interests. Examples of general-sum games are prisoner's dilemma and public goods game.
  - Perfect-information games: These are games where each agent knows the current state of the environment and the actions and rewards of all the other agents. Examples of perfect-information games are chess and Go.
  - Imperfect-information games: These are games where each agent does not know the current state of the environment or the actions and rewards of some or all of the other agents. Examples of imperfect-information games are poker and bridge.
  - Deterministic games: These are games where the state transition probabilities are either one or zero for every state and joint action. In other words, the outcome of the game is deterministic given the current state and the joint action. Examples of deterministic games are chess and Go.
  - Stochastic games: These are games where the state transition probabilities are between zero and one for some or all of the states and joint actions. In other words, the outcome of the game is stochastic given the current state and the joint action. Examples of stochastic games are backgammon and dice games.
  - Cooperative games: These are games where the agents have a common objective and can coordinate their actions to achieve it. Examples of cooperative games are public goods game and team formation.
  - Non-cooperative games: These are games where the agents have individual objectives and cannot coordinate their actions to achieve them. Examples of non-cooperative games are prisoner's dilemma and chicken game.
  - Competitive games: These are games where the agents have opposing objectives and try to hinder each other's actions to achieve them. Examples of competitive games are chess and Go.
  - Collaborative games: These are games where the agents have compatible objectives and try to help each other's actions to achieve them. Examples of collaborative games are bridge and cooperative navigation.

- To solve stochastic games, various methods have been proposed, such as:

  - Minimax: This is a method that finds the optimal strategy for a zero-sum game with perfect information. It assumes that the opponent plays optimally and tries to minimize the agent's reward. It uses a recursive search tree that evaluates the expected reward of each possible state and action pair and chooses the action that maximizes the minimum reward.
  - Nash equilibrium: This is a method that finds the optimal strategy for a general-sum game with perfect or imperfect information. It assumes that the agents play rationally and try to maximize their own reward. It finds a joint strategy that is a best response for each agent, meaning that no agent can improve its reward by deviating from the joint strategy.
  - Reinforcement learning: This is a method that learns the optimal strategy for a stochastic game with perfect or imperfect information. It does not assume any prior knowledge of the environment or the other agents. It learns from its own experience by interacting with the environment and receiving rewards. It updates its strategy based on the observed state, action, and reward, and tries to maximize its expected discounted return over time.