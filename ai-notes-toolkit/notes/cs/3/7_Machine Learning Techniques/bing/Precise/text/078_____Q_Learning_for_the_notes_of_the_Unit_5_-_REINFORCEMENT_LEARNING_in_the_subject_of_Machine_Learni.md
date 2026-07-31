### Q Learning

Q-learning is a model-free reinforcement learning algorithm. The goal of Q-learning is to learn a policy, which tells an agent what action to take under what circumstances. It does not require a model of the environment and can handle problems with stochastic transitions and rewards, without requiring adaptations.

Here are some key points to remember about Q-learning:

1. Q-learning is a form of temporal difference learning, which means it updates its Q-values using the Bellman equation.
2. The Q-value for a given state-action pair is the expected future reward for taking that action in that state and following the optimal policy thereafter.
3. The Q-learning algorithm iteratively updates the Q-values for each state-action pair using the Bellman equation until the Q-values converge.
4. The learning rate and discount factor are two important hyperparameters that control the speed of learning and the importance of future rewards, respectively.
5. Q-learning can be used with both discrete and continuous state and action spaces, but it may require the use of function approximation techniques for large or continuous spaces.
6. Q-learning has been successfully applied to a wide range of problems, including game playing, control, and navigation.
