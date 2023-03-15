### Stochastic Games

- Stochastic games are a generalization of Markov decision processes (MDPs) to the case where there are multiple agents in a common environment.
- The agents perform joint actions that determine both the rewards obtained by the agents and the new state of the environment.
- The agents may have different objectives and preferences, and may act cooperatively or competitively.
- Stochastic games can model various artificial intelligence applications, such as multi-agent reinforcement learning, game theory, and robotics.
- A stochastic game is defined by a set of states, a set of agents, a set of actions for each agent, a transition function, and a reward function for each agent.
- A state is a description of the environment and the agents' positions or statuses.
- An agent is an entity that can perceive the state and choose an action.
- An action is a possible move or operation that an agent can perform.
- A transition function is a probability distribution that specifies the next state given the current state and the joint action of the agents.
- A reward function is a function that assigns a numerical value to each state and action for each agent, representing the agent's preference or utility.
- A stochastic game can be represented by a game tree, where each node is a state, each branch is an action, and each leaf is a terminal state with a payoff vector for the agents.
- A stochastic game can also be represented by a game matrix, where each row is a joint action, each column is a state, and each entry is a payoff vector and a transition probability.
- A solution concept for a stochastic game is a strategy profile, which is a specification of the action that each agent will choose in each state.
- A strategy can be deterministic or stochastic, pure or mixed, stationary or non-stationary, depending on whether the action is fixed or random, single or multiple, independent or dependent on the state.
- A common solution concept for stochastic games is the Nash equilibrium, which is a strategy profile where no agent can improve its expected payoff by deviating from its strategy, given the strategies of the other agents.
- A Nash equilibrium can be computed by various algorithms, such as value iteration, policy iteration, linear programming, or reinforcement learning.
- A Nash equilibrium may not exist, be unique, or be efficient for a stochastic game, depending on the properties of the game, such as zero-sum, cooperative, or general-sum.