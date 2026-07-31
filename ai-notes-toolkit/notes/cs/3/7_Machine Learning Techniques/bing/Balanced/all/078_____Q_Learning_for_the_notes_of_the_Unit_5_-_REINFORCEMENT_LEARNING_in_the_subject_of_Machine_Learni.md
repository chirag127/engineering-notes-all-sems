# Q Learning

Q learning is a model-free, off-policy reinforcement learning algorithm that will find the best course of action, given the current state of the agent . Depending on where the agent is in the environment, it will decide the next action to be taken. The objective of the model is to find the best course of action given its current state.

- Q learning does not require a model of the environment (hence "model-free"), and it can handle problems with stochastic transitions and rewards without requiring adaptations.
- Q learning is considered off-policy because the Q function learns from actions that are outside the current policy, like taking random actions, and therefore a policy is not needed.
- Q learning uses a Q table to store the value of an action in a particular state. The Q table helps us to find the best action for each state. It helps to maximize the expected reward by selecting the best of all possible actions.
- Q learning updates the Q table using the Bellman equation, which expresses the optimal value of a state-action pair as the sum of the immediate reward and the discounted future reward  .
- Q learning is an iterative algorithm that converges to the optimal Q function when the Q table is updated sufficiently  .