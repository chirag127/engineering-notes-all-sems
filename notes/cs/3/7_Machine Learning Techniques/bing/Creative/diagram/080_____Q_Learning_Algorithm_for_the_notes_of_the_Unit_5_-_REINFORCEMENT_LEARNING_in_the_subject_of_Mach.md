### Q Learning Algorithm

Q learning is a **model-free**, **value-based**, **off-policy** reinforcement learning algorithm that learns the **value of an action** in a particular state. It does not require a model of the environment, and it can handle problems with stochastic transitions and rewards. The goal of Q learning is to find the **optimal action-selection policy** that maximizes the expected **cumulative reward** over time.

The main components of Q learning are:

- A set of **states** S, which represent the possible situations that the agent can encounter.
- A set of **actions** A, which represent the possible choices that the agent can make in each state.
- A **reward function** R, which assigns a scalar value to each state-action pair, indicating the immediate feedback that the agent receives after taking an action in a state.
- A **discount factor** γ, which determines how much the agent values future rewards over immediate ones. It is a number between 0 and 1, where 0 means the agent only cares about the current reward, and 1 means the agent cares equally about all rewards.
- A **Q table** Q, which is a matrix that stores the estimated value of each state-action pair. It is initialized randomly or with zeros, and updated iteratively using the Q learning algorithm. The Q table helps the agent to find the best action for each state, by selecting the action that has the highest Q value.

The Q learning algorithm works as follows:

- The agent starts in an initial state s0.
- The agent chooses an action a0 using an **exploration-exploitation strategy**, such as **epsilon-greedy**. This means the agent selects a random action with a small probability epsilon, and selects the action with the highest Q value with a probability of 1-epsilon. This allows the agent to balance between exploring new actions and exploiting the known ones.
- The agent executes the action a0 and observes the next state s1 and the reward r0.
- The agent updates the Q table using the **Bellman equation**, which is:

Q(s0, a0) = Q(s0, a0) + alpha * (r0 + gamma * max Q(s1, a) - Q(s0, a0))

where alpha is the **learning rate**, which determines how much the agent updates the Q table based on new experiences. It is a number between 0 and 1, where 0 means the agent does not learn anything, and 1 means the agent overwrites the Q table with the new value.

The Bellman equation essentially updates the Q value of the current state-action pair by adding a fraction of the difference between the observed reward and the expected reward. The expected reward is the discounted maximum Q value for the next state, which represents the best possible future reward.

- The agent repeats steps 2-4 until the end of the episode, which can be a terminal state or a maximum number of steps.

The Q learning algorithm is guaranteed to converge to the optimal Q table, and hence the optimal policy, if the agent visits every state-action pair infinitely often and the learning rate is sufficiently small.

Some advantages of Q learning are:

- It is simple and easy to implement.
- It can learn from its own experience, without requiring a model of the environment.
- It can handle large and complex state spaces, by using function approximation techniques such as neural networks.

Some disadvantages of Q learning are:

- It can be slow to converge, especially for large state-action spaces.
- It can suffer from the **curse of dimensionality**, which means the Q table grows exponentially with the number of states and actions, making it impractical to store and update.
- It can be affected by the **exploration-exploitation dilemma**, which means the agent has to balance between trying new actions and exploiting the known ones, without knowing the optimal trade-off.