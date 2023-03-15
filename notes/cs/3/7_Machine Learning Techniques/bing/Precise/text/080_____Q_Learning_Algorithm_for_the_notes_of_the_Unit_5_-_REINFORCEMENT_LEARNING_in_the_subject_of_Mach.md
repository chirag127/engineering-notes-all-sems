### Q Learning Algorithm

Q-learning is a model-free reinforcement learning algorithm. It is used to find the optimal action-selection policy for any given finite Markov Decision Process (MDP). It works by learning an action-value function that ultimately gives the expected utility of taking a given action in a given state and following the optimal policy thereafter.

Here are some key points to remember about the Q-learning algorithm:

1. Q-learning is an off-policy algorithm, meaning that it learns the optimal policy even when actions are chosen according to a more exploratory or even random policy.
2. The Q-learning algorithm iteratively updates the Q-values for each state-action pair using the Bellman equation.
3. The learning rate and discount factor are two important hyperparameters that need to be set when using the Q-learning algorithm.
4. The Q-learning algorithm can be used with both discrete and continuous state and action spaces, but may require the use of function approximation techniques for the latter.
5. The Q-learning algorithm is guaranteed to converge to the optimal action-value function under certain conditions.
