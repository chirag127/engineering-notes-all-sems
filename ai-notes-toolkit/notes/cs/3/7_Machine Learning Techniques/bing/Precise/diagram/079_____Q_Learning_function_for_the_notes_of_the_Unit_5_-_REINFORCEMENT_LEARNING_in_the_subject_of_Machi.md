### Q Learning function for the notes of the Unit 5 - REINFORCEMENT LEARNING in the subject of Machine Learning Techniques

Q-learning is a model-free reinforcement learning algorithm. The goal of Q-learning is to learn a policy, which tells an agent what action to take under what circumstances. It does not require a model of the environment and can handle problems with stochastic transitions and rewards, without requiring adaptations.

The Q-learning algorithm is as follows:
1. Initialize the Q-values table, Q(s, a), arbitrarily.
2. Observe the current state, s.
3. Choose an action, a, for the current state based on the current Q-value estimates. This can be done using an exploration strategy, such as ε-greedy.
4. Take the chosen action, observe the resulting reward, r, and the new state, s'.
5. Update the Q-value for the state-action pair using the observed reward and the maximum Q-value for the new state: Q(s, a) = Q(s, a) + α[r + γ max Q(s', a') - Q(s, a)], where α is the learning rate and γ is the discount factor.
6. Set the current state to the new state: s = s'.
7. Repeat steps 3-6 until the goal state is reached or a maximum number of steps is reached.

The Q-learning algorithm can be used to find an optimal action-selection policy for any given finite Markov decision process (MDP). It works by learning an action-value function that ultimately gives the expected utility of taking a given action in a given state and following the optimal policy thereafter. The Q-learning algorithm has been proven to converge to the optimal action-values with probability 1 so long as all actions are repeatedly sampled in all states and the learning rate is appropriately balanced with the tendency to explore new actions.