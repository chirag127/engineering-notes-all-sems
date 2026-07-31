### Stochastic Games

- Stochastic games are a generalization of Markov decision processes (MDPs) to the case where there are multiple agents in a common environment  .
- Stochastic games are also called Markov games, and they are suitable for modeling situations where agents have to cooperate or compete with each other under uncertainty .
- A stochastic game is defined by a set of states, a set of agents, a set of actions for each agent, a transition function that maps a state and a joint action to a probability distribution over the next state, and a reward function that maps a state and a joint action to a real-valued reward for each agent  .
- A solution concept for stochastic games is a strategy profile, which specifies a policy for each agent that maps a state to an action. A strategy profile can be pure (deterministic) or mixed (randomized) .
- The goal of each agent is to maximize its expected discounted return, which is the sum of the discounted rewards over an infinite horizon. The discount factor is a parameter that controls how much the agent values future rewards compared to immediate rewards  .
- Stochastic games can be classified into different types based on the properties of the game, such as the number of agents, the information available to the agents, the nature of the rewards, and the structure of the state space .
- Some examples of stochastic games are:

  - Zero-sum games: These are games where the sum of the rewards of all agents is zero for every state and joint action. In other words, one agent's gain is another agent's loss. Chess and Go are examples of zero-sum games .
  - General-sum games: These are games where the sum of the rewards of all agents is not necessarily zero for every state and joint action. In other words, agents can have conflicting or aligned interests. Prisoner's dilemma and chicken are examples of general-sum games .
  - Cooperative games: These are games where the agents have a common goal and can communicate and coordinate their actions. The reward function is shared by all agents, and the agents can form coalitions to increase their payoff. Public goods game and team Markov games are examples of cooperative games .
  - Non-cooperative games: These are games where the agents have individual goals and cannot communicate or coordinate their actions. The reward function is different for each agent, and the agents act selfishly to maximize their own payoff. Nash equilibrium and Stackelberg equilibrium are examples of solution concepts for non-cooperative games .
  - Perfect-information games: These are games where the agents know the state of the game and the actions of the other agents at every time step. Chess and Go are examples of perfect-information games  .
  - Imperfect-information games: These are games where the agents do not know the state of the game or the actions of the other agents at every time step. Poker and bridge are examples of imperfect-information games .
  - Deterministic games: These are games where the transition function is deterministic, meaning that the next state is uniquely determined by the current state and the joint action. Chess and Go are examples of deterministic games .
  - Stochastic games: These are games where the transition function is stochastic, meaning that the next state is a random variable that depends on the current state and the joint action. Backgammon and dice games are examples of stochastic games .

- Stochastic games are challenging to solve because they involve multiple agents with possibly conflicting objectives, uncertainty about the outcomes of actions, and complex interactions among the agents  .
- Various algorithms have been proposed to find optimal or approximate solutions for stochastic games, such as value iteration, policy iteration, linear programming, reinforcement learning, and evolutionary algorithms   .
- Stochastic games have many applications in artificial intelligence, such as game theory, multi-agent systems, robotics, economics, social sciences, and security  [^