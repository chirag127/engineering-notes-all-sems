### Stochastic Games

- Stochastic games are a generalization of Markov decision processes (MDPs) to the case where there are multiple agents in a common environment .
- The agents perform a joint action that defines both the reward obtained by the agents and the new state of the environment .
- The agents may have different objectives and preferences, and may cooperate or compete with each other .
- Stochastic games can model many artificial intelligence applications, such as playing chess and Go games, autonomous driving, and robotics .
- Stochastic games can be classified into different types, depending on the information available to the agents, the structure of the game, and the nature of the rewards .
- Some examples of stochastic game types are:
  - Zero-sum games: the sum of the rewards of the agents is zero for every state and action. These games capture the idea of pure competition .
  - General-sum games: the sum of the rewards of the agents is not necessarily zero. These games allow for cooperation and coordination among the agents .
  - Perfect-information games: the agents know the state of the environment and the actions of the other agents. These games are deterministic and can be solved by backward induction .
  - Imperfect-information games: the agents do not know the state of the environment and/or the actions of the other agents. These games are stochastic and require probabilistic reasoning .
  - Stationary games: the rewards and the transition probabilities of the environment do not depend on time. These games have a stationary equilibrium solution .
  - Non-stationary games: the rewards and the transition probabilities of the environment may change over time. These games require adaptive strategies and learning .
- Stochastic games can be solved by various methods, depending on the type of the game and the objectives of the agents .
- Some examples of solution methods are:
  - Minimax: a method for finding the optimal strategy for a zero-sum game, by minimizing the maximum possible loss .
  - Nash equilibrium: a method for finding a stable strategy profile for a general-sum game, where no agent can improve its payoff by deviating from its strategy .
  - Reinforcement learning: a method for learning from experience and feedback, by updating the value function and the policy of the agent .
  - Descent: a method for learning and planning in the context of two-player perfect-information games, by using gradient descent and Monte Carlo tree search.