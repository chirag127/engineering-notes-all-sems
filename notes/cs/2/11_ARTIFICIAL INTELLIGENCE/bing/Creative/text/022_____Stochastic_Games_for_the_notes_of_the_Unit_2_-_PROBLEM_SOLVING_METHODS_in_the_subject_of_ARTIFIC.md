### Stochastic Games

- Stochastic games are a generalization of Markov decision processes (MDPs) to the case where there are multiple agents in a common environment  .
- The agents perform a joint action that defines both the reward obtained by the agents and the new state of the environment .
- The agents may have different objectives and preferences, and may cooperate or compete with each other  .
- Stochastic games can model many artificial intelligence applications, such as chess, backgammon, autonomous driving, and robotics  .
- Stochastic games can be classified into different types, depending on the information available to the agents, the structure of the game, and the nature of the rewards .
- Some of the types of stochastic games are:

  - Zero-sum games: The agents have opposite and equal interests, and the sum of their rewards is zero for every state and action .
  - General-sum games: The agents have arbitrary and possibly conflicting interests, and the sum of their rewards is not necessarily zero .
  - Cooperative games: The agents have a common goal and can coordinate their actions and share information .
  - Non-cooperative games: The agents have individual goals and act independently and selfishly .
  - Perfect-information games: The agents know the current state of the environment and the rules of the game .
  - Imperfect-information games: The agents have incomplete or uncertain knowledge of the current state of the environment or the rules of the game .
  - Deterministic games: The transition function of the environment is deterministic, and the outcome of each action is certain .
  - Stochastic games: The transition function of the environment is probabilistic, and the outcome of each action is uncertain .

- The solution concepts for stochastic games depend on the type of the game and the assumptions made about the agents .
- Some of the solution concepts are:

  - Nash equilibrium: A joint strategy where no agent can improve its expected reward by deviating from its strategy, given the strategies of the other agents .
  - Pareto optimality: A joint strategy where no agent can improve its expected reward without decreasing the expected reward of another agent .
  - Correlated equilibrium: A joint strategy where the agents follow a probability distribution over the joint actions, and no agent can improve its expected reward by deviating from the distribution, given the actions of the other agents .
  - Subgame perfect equilibrium: A Nash equilibrium that is also a Nash equilibrium for every subgame of the original game .
  - Minimax: A joint strategy that minimizes the maximum possible loss for the worst-case scenario .

- The algorithms for finding the solution concepts for stochastic games vary depending on the type of the game and the information available to the agents .
- Some of the algorithms are:

  - Value iteration: An iterative algorithm that computes the optimal value function and policy for each agent, assuming perfect information and complete knowledge of the transition and reward functions .
  - Policy iteration: An iterative algorithm that alternates between evaluating and improving the current policy for each agent, assuming perfect information and complete knowledge of the transition and reward functions .
  - Q-learning: A reinforcement learning algorithm that learns the optimal action-value function for each agent, without requiring knowledge of the transition and reward functions .
  - Fictitious play: A learning algorithm that updates the beliefs and best responses of each agent, based on the observed actions of the other agents .
  - Regret minimization: A learning algorithm that updates the mixed strategy of each agent, based on the regret of not playing the best action in the past .
  - Monte Carlo tree search: A planning algorithm that builds a search tree of possible actions and outcomes