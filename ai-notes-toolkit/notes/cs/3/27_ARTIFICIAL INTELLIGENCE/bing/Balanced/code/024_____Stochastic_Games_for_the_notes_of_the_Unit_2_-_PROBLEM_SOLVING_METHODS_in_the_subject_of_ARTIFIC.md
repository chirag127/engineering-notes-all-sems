### Stochastic Games

- Stochastic games are a generalization of Markov decision processes (MDPs) to the case where there are multiple agents in a common environment.
- The agents perform joint actions that define both the rewards obtained by the agents and the new state of the environment.
- The environment is assumed to be stochastic, meaning that the transition probabilities and the rewards depend on the current state and the joint action, but not on the history of the game.
- The agents are assumed to be rational, meaning that they aim to maximize their expected discounted rewards over time.
- The agents may have different objectives and preferences, and may cooperate or compete with each other.
- The solution concept for stochastic games is the Nash equilibrium, which is a joint strategy profile such that no agent can improve its expected payoff by deviating from its strategy, given the strategies of the other agents.
- Finding a Nash equilibrium for stochastic games is computationally hard in general, and may not be unique or exist at all.
- Various algorithms have been proposed to approximate or compute Nash equilibria for stochastic games, such as value iteration, policy iteration, linear programming, fictitious play, regret minimization, and reinforcement learning.