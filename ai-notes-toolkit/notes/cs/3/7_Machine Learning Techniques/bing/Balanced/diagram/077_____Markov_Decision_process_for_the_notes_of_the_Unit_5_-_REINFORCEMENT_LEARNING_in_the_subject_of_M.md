### Markov Decision Process

A Markov decision process (MDP) is a mathematical framework for modeling decision-making problems where the outcomes are partly random and partly controllable by an agent. It is a framework that can address most reinforcement learning (RL) problems .

An MDP consists of four components :

- A set of states **S** that the agent can be in. For example, the location of a robot in a grid world.
- A set of actions **A** that the agent can take in each state. For example, moving up, down, left, or right in the grid world.
- A transition function **T(s, a, s')** that specifies the probability of reaching state **s'** from state **s** by taking action **a**. For example, the probability of moving to the right cell from the current cell by taking the right action.
- A reward function **R(s, a, s')** that specifies the immediate reward received by the agent for taking action **a** in state **s** and reaching state **s'**. For example, the reward for reaching the goal cell in the grid world.

The goal of the agent is to find a policy **π(s)** that specifies the best action to take in each state **s** to maximize the expected return, which is the discounted sum of future rewards . For example, the policy that tells the robot to move towards the goal cell in the grid world.

There are two main methods for finding the optimal policy in an MDP :

- Dynamic programming: This method assumes that the agent knows the transition and reward functions of the MDP, and uses iterative algorithms such as value iteration or policy iteration to compute the optimal value function and policy.
- Reinforcement learning: This method assumes that the agent does not know the transition and reward functions of the MDP, and learns from its own experience by interacting with the environment and receiving feedback. There are various algorithms for reinforcement learning, such as Q-learning, SARSA, or actor-critic.

MDPs are widely used to model and solve many RL problems, such as navigation, robotics, games, or control . They provide a formal and general framework for describing and analyzing the trade-off between exploration and exploitation, uncertainty and risk, and short-term and long-term rewards.