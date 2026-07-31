### Introduction to Deep Q Learning

Deep Q Learning is a type of Reinforcement Learning algorithm that combines the Q-Learning algorithm with Deep Neural Networks. It is used to solve complex problems where the state and action spaces are large or continuous.

Some key points to remember about Deep Q Learning are:

1. Deep Q Learning is an off-policy algorithm, meaning that it learns from past experiences rather than the current policy.
2. The algorithm uses a Deep Neural Network to approximate the Q-function, which estimates the expected future rewards for taking an action in a given state.
3. The network is trained using a variant of the Q-Learning algorithm, where the target Q-values are computed using the current Q-network and the Bellman equation.
4. Experience replay is often used in Deep Q Learning to improve the stability of the learning process. This involves storing past experiences in a replay buffer and randomly sampling from it to update the network.
5. Deep Q Learning has been successfully applied to a wide range of problems, including playing Atari games and controlling robots.

This is a brief introduction to Deep Q Learning. It is a powerful algorithm that has shown great success in solving complex problems. It is an important topic to study in the field of Reinforcement Learning and Machine Learning Techniques.