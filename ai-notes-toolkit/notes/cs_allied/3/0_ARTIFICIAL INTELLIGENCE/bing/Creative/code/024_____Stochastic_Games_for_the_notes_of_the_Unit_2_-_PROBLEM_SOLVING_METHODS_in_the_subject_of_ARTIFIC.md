### Stochastic Games

- Stochastic games are a generalization of Markov decision processes (MDPs) to the case where there are multiple agents in a common environment.
- The agents perform a joint action that defines both the reward obtained by the agents and the new state of the environment.
- The environment is assumed to be stochastic, meaning that the state transition probabilities depend only on the current state and the joint action, not on the history of the game.
- The agents are assumed to be rational, meaning that they aim to maximize their expected discounted return over time.
- Stochastic games can be classified into different types based on the following criteria:
  - The number of agents: two-player or multi-player.
  - The information available to the agents: perfect-information or imperfect-information.
  - The nature of the rewards: zero-sum or general-sum.
  - The horizon of the game: finite or infinite.
- Some examples of stochastic games are backgammon, poker, chess with dice, and robot soccer.
- Stochastic games are challenging to solve because of the following reasons:
  - The state space and the action space grow exponentially with the number of agents.
  - The agents may have conflicting or cooperative interests, which require different solution concepts such as Nash equilibrium or Pareto optimality.
  - The agents may have incomplete or asymmetric information about the state, the actions, or the rewards of other agents, which require sophisticated belief updating and reasoning mechanisms.
- Various resolution algorithms have been proposed for stochastic games, such as value iteration, policy iteration, linear programming, reinforcement learning, and Monte Carlo methods.