
### Markov Decision Process

Markov Decision Process (MDP) is a fundamental tool used in Reinforcement Learning (RL). It is a mathematical framework for modeling decision-making in a situation where outcomes are partly random and partly under the control of a decision-maker.

MDPs are used to solve a wide variety of problems, from robotics to finance. In RL, MDPs provide a way to define the environment in which an agent is operating, and to determine the optimal policy for the agent to follow.

MDPs consist of five components:

1. A set of **states**: These are the different states that the environment can be in.
2. A set of **actions**: These are the different actions that the agent can take in each state.
3. A **transition function**: This is a function that defines the probability of transitioning from one state to another, given an action.
4. A **reward function**: This is a function that defines the rewards that the agent receives for taking a particular action in a particular state.
5. A **discount factor**: This is a parameter that determines how much the agent values future rewards relative to immediate rewards.

The goal of an MDP is to find the optimal policy, which is the sequence of actions that maximizes the expected reward over time. To do this, the agent needs to use a reinforcement learning algorithm to learn the optimal policy.