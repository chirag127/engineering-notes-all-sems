### Q Learning function for the notes of the Unit 5 - REINFORCEMENT LEARNING in the subject of Machine Learning Techniques

- Q-learning is a **model-free, off-policy** reinforcement learning algorithm that seeks to find the **best action** to take given the **current state**  .
- It does not require a **model of the environment**, and it can handle problems with **stochastic transitions and rewards** without requiring adaptations.
- The objective of Q-learning is to **maximize the value function Q**, which represents the **expected future reward** for taking an action in a state .
- The Q-learning function is defined as:

$$Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma \max_{a'} Q(s', a') - Q(s, a)]$$

where:

  - $s$ is the **current state**
  - $a$ is the **action** taken in the current state
  - $s'$ is the **next state** after taking the action
  - $a'$ is the **best action** in the next state
  - $r$ is the **reward** received for taking the action
  - $\alpha$ is the **learning rate**, which controls how much the Q-value is updated
  - $\gamma$ is the **discount factor**, which controls how much the future rewards are considered

- The Q-learning function updates the Q-value by adding a fraction of the **temporal difference** (TD) error, which is the difference between the **observed reward** and the **expected reward** .
- The Q-learning algorithm works as follows :

  - Initialize the Q-table with arbitrary values (usually zeros)
  - Repeat for each episode:
    - Initialize the state
    - Repeat for each step of the episode:
      - Choose an action using an exploration-exploitation strategy (e.g., epsilon-greedy)
      - Execute the action and observe the next state and reward
      - Update the Q-value using the Q-learning function
      - Update the state
    - Until the end of the episode

- Q-learning can be implemented using **tabular methods** or **function approximation methods**  .
- Tabular methods store the Q-values in a **table**, where each row corresponds to a state and each column corresponds to an action. The table is updated iteratively using the Q-learning function .
- Function approximation methods use a **function** (e.g., a neural network) to approximate the Q-values for any state-action pair. The function is trained using **gradient descent** to minimize the TD error.
- Q-learning is a **value-based** reinforcement learning algorithm, which means it learns the **value** of each state-action pair, rather than the **policy** that maps states to actions  .
- Q-learning is **guaranteed to converge** to the optimal Q-values under certain conditions, such as infinite exploration, constant learning rate, and Markovian environment .