### Introduction to Deep Q Learning

Deep Q Learning is a reinforcement learning algorithm that combines Q Learning and deep neural networks to learn how to act optimally in complex environments. 

Some key points about Deep Q Learning are:

- Q Learning is a model-free algorithm that learns the value of taking an action in a state, denoted by Q(s, a). The Q value represents the expected cumulative reward of following a certain policy from that state-action pair.
- Deep Q Learning uses a deep neural network to approximate the Q function, rather than a table of values. This allows the algorithm to handle large state and action spaces, as well as high-dimensional inputs such as images or sensor data.
- Deep Q Learning trains the neural network by minimizing the mean squared error between the predicted Q value and the target Q value, which is computed using the Bellman equation and a discount factor.
- Deep Q Learning introduces two techniques to improve the stability and performance of the algorithm: experience replay and target network. Experience replay stores the agent's experiences in a buffer and samples mini-batches of transitions to train the network. Target network is a copy of the main network that is updated periodically and used to compute the target Q values.
- Deep Q Learning was able to achieve superhuman performance on many Atari games by using a convolutional neural network to process the raw pixel inputs and output the Q values for each possible action.