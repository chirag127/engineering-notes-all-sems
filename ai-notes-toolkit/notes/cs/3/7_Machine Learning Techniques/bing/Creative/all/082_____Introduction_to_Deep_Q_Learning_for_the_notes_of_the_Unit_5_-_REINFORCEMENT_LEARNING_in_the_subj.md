# Introduction to Deep Q Learning

Deep Q Learning is a reinforcement learning algorithm that combines Q Learning and deep neural networks to learn how to act optimally in complex environments. 

Some key points about Deep Q Learning are:

- Q Learning is a model-free, value-based, off-policy algorithm that learns the value of taking an action in a state, denoted by Q(s, a). The Q value represents the expected cumulative reward of following a certain policy after taking an action in a state.
- Deep Q Learning uses a deep neural network to approximate the Q function, rather than a table of values. This allows the algorithm to handle large state and action spaces, as well as high-dimensional inputs such as images or sensor data.
- Deep Q Learning trains the neural network by minimizing the mean squared error between the predicted Q value and the target Q value, which is computed using the Bellman equation and a discount factor. The target Q value is updated periodically using a copy of the network, called the target network, to avoid instability and divergence.
- Deep Q Learning also uses a technique called experience replay, which stores the agent's experiences in a memory buffer and samples them randomly to train the network. This reduces the correlation and variance of the training data, and improves the efficiency and stability of the learning process.
- Deep Q Learning was developed by DeepMind in 2015 and demonstrated superhuman performance on a wide range of Atari games by learning from raw pixel inputs. It is one of the most influential and popular algorithms in reinforcement learning.