### Genetic Programming

Genetic Programming (GP) is a type of Evolutionary Algorithm (EA), a subset of machine learning. EAs are used to discover solutions to problems humans do not know how to solve, directly.

In the context of Reinforcement Learning (RL), GP can be used for feature discovery. A population of individuals, each representing a set of features, is evolved, and individuals are evaluated by their average performance on short reinforcement learning trials.

GP can also be used to find the values of parameters used in Deep Deterministic Policy Gradient (DDPG) combined with Hindsight Experience Replay (HER), to help speed up the learning agent. Experimental evaluation shows that this method leads to better performance, faster than the original algorithm.