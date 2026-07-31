# Markov Decision Process

Markov Decision Process (MDP) is a mathematical framework used for modeling decision making in situations where outcomes are partly random and partly under the control of a decision maker. MDPs are widely used in reinforcement learning, a type of machine learning technique, to solve problems that involve making a sequence of decisions.

An MDP is defined by the following components:
- A set of states, S
- A set of actions, A
- A transition function, T(s, a, s') that specifies the probability of transitioning from state s to state s' when action a is taken
- A reward function, R(s, a, s') that specifies the immediate reward received when transitioning from state s to state s' by taking action a
- A discount factor, γ, that determines the present value of future rewards

The goal of an MDP is to find a policy, π, that specifies the action to take in each state to maximize the expected cumulative reward over time. This can be achieved through various algorithms such as value iteration, policy iteration, and Q-learning.

In summary, Markov Decision Process is a powerful tool for modeling decision making in uncertain environments and is widely used in reinforcement learning to solve complex problems. It provides a structured approach to finding the optimal policy for maximizing the expected cumulative reward over time.