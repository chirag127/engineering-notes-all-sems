### Q Learning Algorithm

Q learning is a **model-free**, **value-based**, **off-policy** reinforcement learning algorithm that learns the **value of an action** in a particular state. It does not require a model of the environment, and it can handle problems with stochastic transitions and rewards. The goal of Q learning is to find the **optimal action-selection policy** that maximizes the expected **cumulative reward** over time.

The main components of Q learning are:

- A set of **states** S that the agent can observe.
- A set of **actions** A that the agent can perform in each state.
- A **reward function** R that gives the immediate reward for each state-action pair.
- A **discount factor** γ that determines how much the agent values future rewards over immediate ones.
- A **Q table** Q that stores the estimated value of each state-action pair.

The Q table is initialized randomly or with some prior knowledge, and then updated iteratively using the **Q learning update rule**:

Q(s, a) ← Q(s, a) + α [r + γ max Q(s', a') - Q(s, a)]

where:

- s is the current state
- a is the action taken in s
- r is the reward received after taking a in s
- s' is the next state
- a' is the action with the highest Q value in s'
- α is the learning rate that controls how much the Q value is updated

The Q learning update rule is based on the **Bellman equation**, which states that the optimal Q value for a state-action pair is equal to the expected reward plus the discounted optimal Q value for the next state-action pair.

The agent learns by **exploring** the environment and **exploiting** the Q table. A common exploration strategy is the **epsilon-greedy** method, which chooses a random action with probability ε and the greedy action (the one with the highest Q value) with probability 1 - ε. This balances the trade-off between exploration and exploitation, and ensures that the agent does not get stuck in a suboptimal policy.

Q learning is a simple and powerful algorithm that can learn to solve many complex problems, such as maze navigation, cart-pole balancing, and Atari games. However, it also has some limitations, such as:

- It requires a large Q table to store the value of every state-action pair, which can be impractical for large or continuous state and action spaces.
- It assumes that the environment is **Markovian**, meaning that the next state and reward depend only on the current state and action, and not on the previous ones.
- It can be slow to converge to the optimal policy, especially if the rewards are sparse or delayed.