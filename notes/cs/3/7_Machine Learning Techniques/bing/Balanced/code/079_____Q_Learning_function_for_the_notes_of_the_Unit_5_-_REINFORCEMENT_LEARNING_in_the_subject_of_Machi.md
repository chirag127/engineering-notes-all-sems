### Q Learning function for the notes of the Unit 5 - REINFORCEMENT LEARNING in the subject of Machine Learning Techniques

- Q-learning is a **model-free, off-policy** reinforcement learning algorithm that seeks to find the **best action** to take given the **current state** of the agent  .
- Q-learning does not require a **model** of the environment (hence "model-free"), and it can handle problems with **stochastic transitions and rewards** without requiring adaptations.
- Q-learning uses a **Q-table**, which is a matrix that stores the **value** of taking an action in a state. The Q-table is updated iteratively using the **Bellman equation**, which expresses the optimal value function as the sum of the immediate reward and the discounted future value  .
- The Q-learning algorithm is as follows  :
  - Initialize the Q-table with arbitrary values (usually zeros).
  - Observe the current state of the agent and the environment.
  - Choose an action using an **exploration-exploitation** strategy (such as **epsilon-greedy**), which balances between taking random actions to explore new states and taking the best known action to exploit the current knowledge.
  - Execute the action and observe the resulting state and reward.
  - Update the Q-table using the Bellman equation: `Q(state, action) = Q(state, action) + alpha * (reward + gamma * max Q(next state, all actions) - Q(state, action))`, where `alpha` is the **learning rate** and `gamma` is the **discount factor**.
  - Repeat until the Q-table converges to the optimal value function.
- Q-learning can be extended to handle large or continuous state and action spaces using **function approximation** techniques, such as **deep neural networks**. This is known as **deep Q-learning** or **deep Q-networks (DQN)**.