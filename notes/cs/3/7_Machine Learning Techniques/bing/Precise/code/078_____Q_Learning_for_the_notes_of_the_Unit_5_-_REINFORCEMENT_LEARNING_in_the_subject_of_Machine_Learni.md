### Q Learning

Q-learning is a model-free reinforcement learning algorithm. The goal of Q-learning is to learn a policy, which tells an agent what action to take under what circumstances. It does not require a model of the environment and can handle problems with stochastic transitions and rewards, without requiring adaptations.

Here are some key points to remember about Q-learning:

1. Q-learning is an off-policy algorithm, meaning that it learns the optimal policy even when actions are chosen according to a more exploratory or even random policy.

2. The Q-learning algorithm iteratively updates the Q-values for each state-action pair using the Bellman equation.

3. The Q-values represent the expected future reward for taking a given action in a given state and following the optimal policy thereafter.

4. The learning rate determines how much new information is taken into account in each update of the Q-values.

5. The discount factor determines the importance of future rewards. A high discount factor means that future rewards are taken into account more strongly.

6. The exploration-exploitation trade-off is an important aspect of Q-learning. The agent needs to balance the exploration of new actions and states with the exploitation of known information to maximize its reward.

7. Q-learning can be used with a variety of function approximators to estimate the Q-values, including neural networks, decision trees, and linear regression.

8. Q-learning can be applied to a wide range of problems, including game playing, robotics, and resource management.
