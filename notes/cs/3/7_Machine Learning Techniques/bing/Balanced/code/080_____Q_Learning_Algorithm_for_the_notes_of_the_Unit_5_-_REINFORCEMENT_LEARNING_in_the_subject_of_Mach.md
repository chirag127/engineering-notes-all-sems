### Q Learning Algorithm

Q learning is a model-free reinforcement learning algorithm that learns the value of an action in a particular state. It does not require a model of the environment, and it can handle problems with stochastic transitions and rewards without requiring adaptations.

Some key points about Q learning are:

- Q learning is a value-based reinforcement learning algorithm, which means it tries to find the optimal action-selection policy by learning a function that maps state-action pairs to expected rewards.
- Q learning uses a Q table, which is a matrix that stores the Q values for each state-action pair. The Q value represents the expected future reward of taking an action in a state.
- Q learning follows the Bellman equation, which states that the Q value of a state-action pair is equal to the immediate reward plus the discounted future reward of the next state-action pair.
- Q learning updates the Q table iteratively using the following formula:

  Q(state, action) = Q(state, action) + alpha * (reward + gamma * max Q(next state, all actions) - Q(state, action))

  where alpha is the learning rate, gamma is the discount factor, and max Q(next state, all actions) is the maximum Q value for the next state over all possible actions.
- Q learning is an off-policy algorithm, which means it learns from the actions that are not necessarily part of the current policy. It uses an exploration-exploitation trade-off to balance between exploring new actions and exploiting the best known actions.
- Q learning can converge to the optimal policy if the Q table is updated infinitely and the exploration rate is decayed appropriately.