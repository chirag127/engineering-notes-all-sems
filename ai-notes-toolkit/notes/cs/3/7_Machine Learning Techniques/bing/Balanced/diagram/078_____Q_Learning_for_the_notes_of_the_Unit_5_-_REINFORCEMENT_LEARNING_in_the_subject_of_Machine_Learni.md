### Q Learning

Q learning is a model-free, off-policy reinforcement learning algorithm that will find the best course of action, given the current state of the agent . Depending on where the agent is in the environment, it will decide the next action to be taken. The objective of the model is to find the best course of action given its current state.

- Q learning uses a Q table, which is a matrix that stores the value of taking an action in a state. The Q table is initialized randomly and updated iteratively using the Bellman equation  .
- The Bellman equation is a recursive formula that expresses the optimal value of a state-action pair as the immediate reward plus the discounted future value of the next state-action pair  .
- The Q learning algorithm consists of the following steps :
  - Initialize the Q table randomly.
  - Observe the current state of the agent.
  - Choose an action using an exploration-exploitation trade-off strategy, such as epsilon-greedy .
  - Execute the action and observe the next state and the reward.
  - Update the Q table using the Bellman equation.
  - Repeat until the Q table converges or a termination condition is met.

- Q learning is an off-policy algorithm because it learns from actions that are outside the current policy, like taking random actions, and therefore a policy is not needed. However, Q learning can also be used to derive a policy by choosing the action that maximizes the Q value for each state .
- Q learning can handle problems with stochastic transitions and rewards without requiring adaptations. However, Q learning may suffer from the curse of dimensionality, which means that the Q table may become too large and impractical to store and update as the number of states and actions increases .
- Q learning is a simple and powerful reinforcement learning algorithm that can be applied to many problems, such as gridworld, maze, cart-pole, mountain car, etc . However, Q learning may also have some limitations, such as slow convergence, overestimation of Q values, and inability to generalize to unseen states. Therefore, Q learning may need to be combined with other techniques, such as function approximation, deep learning, or policy gradient, to overcome these challenges.