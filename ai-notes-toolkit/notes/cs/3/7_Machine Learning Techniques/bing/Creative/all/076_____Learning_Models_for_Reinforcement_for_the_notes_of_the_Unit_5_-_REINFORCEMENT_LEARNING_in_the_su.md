# Learning Models for Reinforcement Learning

Reinforcement learning is a type of machine learning that enables an agent to learn from its own actions and rewards in an environment. The agent does not have a supervisor or a teacher, but learns by trial and error. The goal of reinforcement learning is to find an optimal policy that maximizes the expected cumulative reward over time.

There are two important learning models in reinforcement learning: Markov Decision Process and Q-learning.

## Markov Decision Process

A Markov Decision Process (MDP) is a mathematical framework that models the interaction between an agent and an environment as a sequence of discrete time steps. At each time step, the agent observes the state of the environment, chooses an action, and receives a reward. The environment then transitions to a new state according to a probability distribution that depends on the previous state and action. The agent's objective is to maximize the expected sum of discounted rewards over time.

An MDP is defined by the following components:

- A set of states S, which represent the possible configurations of the environment.
- A set of actions A, which represent the possible choices of the agent.
- A transition function T(s, a, s'), which gives the probability of the environment transitioning from state s to state s' after the agent takes action a.
- A reward function R(s, a, s'), which gives the immediate reward that the agent receives after taking action a in state s and reaching state s'.
- A discount factor γ, which determines how much the agent values future rewards compared to immediate rewards.

An MDP is said to be fully observable if the agent can access the complete state of the environment at each time step. Otherwise, the MDP is partially observable and the agent has to rely on observations or beliefs to infer the state.

An MDP is said to be deterministic if the transition and reward functions are deterministic, meaning that there is only one possible outcome for each state-action pair. Otherwise, the MDP is stochastic and the outcomes are probabilistic.

An MDP is said to be episodic if the interaction between the agent and the environment terminates after a finite number of time steps, and the agent's goal is to maximize the total reward within each episode. Otherwise, the MDP is continuing and the interaction is infinite, and the agent's goal is to maximize the average reward per time step.

## Q-learning

Q-learning is a model-free reinforcement learning algorithm that does not require a model of the environment's dynamics. Instead, it learns a value function that estimates the expected future reward for each state-action pair. The value function is denoted by Q(s, a) and is updated iteratively using the following rule:

Q(s, a) ← Q(s, a) + α [r + γ max Q(s', a') - Q(s, a)]

where α is the learning rate, r is the reward, γ is the discount factor, and s' is the next state.

The agent follows an exploration-exploitation trade-off strategy to balance between learning new information and exploiting the current knowledge. One common strategy is ε-greedy, which means that the agent chooses a random action with probability ε and the action that maximizes Q(s, a) with probability 1 - ε.

Q-learning is guaranteed to converge to the optimal value function and policy under certain conditions, such as infinite visits to each state-action pair and a decreasing learning rate.

Q-learning can be extended to handle continuous state and action spaces by using function approximation techniques, such as neural networks, to represent the Q-function. This leads to deep Q-learning, which combines Q-learning with deep learning.