### Introduction to Deep Q Learning

- Deep Q Learning is a variant of Q Learning, which is a model-free reinforcement learning algorithm that learns the value of an action in a given state .
- Deep Q Learning uses a deep neural network to approximate the Q function, which represents the expected cumulative reward of taking a certain action in a certain state and following a certain policy .
- Deep Q Learning can handle environments with a large number of states and actions, as well as high-dimensional inputs such as images or sensor data .
- Deep Q Learning was developed by DeepMind in 2015 and was able to solve a wide range of Atari games by combining reinforcement learning and deep neural networks at scale.
- Deep Q Learning consists of the following steps :
  - Initialize the Q network with random weights and create a target network with the same weights.
  - Observe the current state and choose an action based on an exploration-exploitation trade-off (e.g. epsilon-greedy).
  - Execute the action and observe the next state and the reward.
  - Store the transition (state, action, reward, next state) in a replay buffer.
  - Sample a batch of transitions from the replay buffer and use the Q network to predict the Q values for the current states and actions.
  - Use the target network to predict the Q values for the next states and actions, and apply the Bellman equation to compute the target Q values.
  - Update the Q network weights by minimizing the mean squared error between the predicted Q values and the target Q values.
  - Periodically update the target network weights by copying the Q network weights.
  - Repeat until convergence or termination.