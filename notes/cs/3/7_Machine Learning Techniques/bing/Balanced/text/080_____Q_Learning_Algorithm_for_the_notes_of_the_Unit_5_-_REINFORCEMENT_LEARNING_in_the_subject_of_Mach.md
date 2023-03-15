### Q Learning Algorithm

Q learning is a model-free reinforcement learning algorithm that learns the value of an action in a particular state. It does not require a model of the environment, and it can handle problems with stochastic transitions and rewards without requiring adaptations.

Some key points about Q learning are:

- Q learning is a value-based reinforcement learning algorithm, which means it tries to find the optimal action-selection policy by learning a function that maps state-action pairs to expected rewards.
- Q learning uses a table, called the Q table, to store the values of each state-action pair. The Q table is initialized randomly and updated iteratively using the Bellman equation.
- Q learning follows an off-policy learning approach, which means it can learn from the actions that are not part of the current policy. It uses an exploration-exploitation trade-off to balance between exploring new actions and exploiting the known ones.
- Q learning is guaranteed to converge to the optimal policy if the learning rate and the discount factor are chosen appropriately, and if each state-action pair is visited infinitely often.