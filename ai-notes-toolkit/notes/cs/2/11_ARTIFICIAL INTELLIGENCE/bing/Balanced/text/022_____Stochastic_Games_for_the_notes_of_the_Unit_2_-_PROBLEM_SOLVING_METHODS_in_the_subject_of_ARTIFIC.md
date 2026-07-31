### Stochastic Games

- Stochastic games are a generalization of Markov decision processes (MDPs) to the case where there are multiple agents in a common environment.
- The agents perform joint actions that determine both the rewards obtained by the agents and the new state of the environment.
- The agents may have different objectives and preferences, and may act cooperatively or competitively.
- Stochastic games can model many artificial intelligence applications, such as multi-agent reinforcement learning, game theory, and robotics.
- A stochastic game is defined by a set of states, a set of agents, a set of actions for each agent, a transition function, and a reward function for each agent.
- A state is a description of the environment and the agents' positions and statuses.
- An agent is an entity that can perceive the state and choose an action.
- An action is a possible move or operation that an agent can perform.
- A transition function is a probability distribution that specifies the next state given the current state and the joint action of the agents.
- A reward function is a function that assigns a numerical value to each state and action for each agent, representing the agent's preference or utility.
- A stochastic game can be represented by a game tree, where each node is a state, each branch is an action, and each leaf is a terminal state with a payoff vector for the agents.
- A stochastic game can also be represented by a game matrix, where each row is a joint action, each column is a state, and each cell is a probability distribution over the next states and a payoff vector for the agents.
- A solution concept for a stochastic game is a strategy profile, which is a collection of strategies for each agent, where a strategy is a function that maps each state to an action or a probability distribution over actions.
- A strategy profile can be evaluated by its expected value, which is the average payoff vector for the agents over all possible outcomes of the game, or by its Pareto optimality, which is a property that means no agent can improve its payoff without hurting another agent's payoff.
- Some common solution concepts for stochastic games are Nash equilibrium, subgame perfect equilibrium, correlated equilibrium, and cooperative equilibrium.