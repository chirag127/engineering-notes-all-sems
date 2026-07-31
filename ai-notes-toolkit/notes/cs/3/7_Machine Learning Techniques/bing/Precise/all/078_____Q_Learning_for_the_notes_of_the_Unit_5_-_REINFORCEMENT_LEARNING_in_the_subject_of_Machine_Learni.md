# Q Learning

Q Learning is a model-free reinforcement learning algorithm that is used to find the optimal action-selection policy for a Markov Decision Process (MDP). It is an off-policy algorithm, meaning that it learns the optimal policy even when actions are chosen according to a more exploratory or different policy.

Some key points to remember about Q Learning are:

1. Q Learning is a type of Temporal Difference (TD) learning, which means that it updates its Q values using the Bellman equation.
2. The Q values represent the expected future reward for taking a particular action in a given state.
3. The Q values are updated iteratively using the Q Learning update rule, which is based on the Bellman equation.
4. The Q Learning algorithm involves exploring the environment and updating the Q values based on the observed rewards and the estimated future rewards.
5. The exploration-exploitation trade-off is an important aspect of Q Learning, where the agent must balance the need to explore new states and actions with the need to exploit the knowledge it has already gained.
6. The learning rate and the discount factor are important hyperparameters of the Q Learning algorithm that determine how quickly the Q values are updated and how much future rewards are taken into account.
