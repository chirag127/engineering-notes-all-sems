# Q Learning Algorithm

- Q learning is a **model-free** reinforcement learning algorithm that learns the **value** of an action in a particular state .
- It does not require a model of the environment, and it can handle problems with **stochastic** transitions and rewards.
- The goal of Q learning is to find the **optimal** action-selection policy that maximizes the **expected** reward .
- Q learning uses a **Q table** to store the value of each state-action pair. The Q table is initialized randomly and updated iteratively using the **Bellman equation** .
- The Bellman equation expresses the **recursive** relationship between the value of a state and the value of its successor states.
- Q learning follows an **exploration-exploitation** trade-off strategy to balance between **exploring** new actions and **exploiting** the known values .
- Q learning is an **off-policy** algorithm, meaning that it learns from the actions that are **not** necessarily following the current policy.
- Q learning can converge to the optimal policy if all state-action pairs are visited **infinitely** often and the learning rate is **properly** set .