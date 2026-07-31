### Introduction to Deep Q Learning

Deep Q Learning is a reinforcement learning algorithm that combines Q Learning and deep neural networks to learn how to act optimally in complex environments. 

- Q Learning is a model-free algorithm that learns the value of taking an action in a state, called the Q-value, by exploring the environment and updating a table of Q-values based on the observed rewards.
- Deep neural networks are function approximators that can learn from high-dimensional inputs, such as images or sensor data, and output a vector of values, such as Q-values for all possible actions .
- Deep Q Learning uses a deep neural network to represent the Q-function, and trains it with a variant of stochastic gradient descent called experience replay, which samples transitions from a replay buffer of past experiences.
- Deep Q Learning can solve a wide range of problems, such as playing Atari games, controlling robots, or optimizing energy consumption, by learning from raw inputs and rewards, without requiring a model of the environment or prior knowledge of the domain .

: https://www.geeksforgeeks.org/deep-q-learning/
: https://www.turing.com/kb/how-are-neural-networks-used-in-deep-q-learning
: https://en.wikipedia.org/wiki/Q-learning
: https://www.tensorflow.org/agents/tutorials/0_intro_rl
: https://www.datacamp.com/tutorial/introduction-q-learning-beginner-tutorial