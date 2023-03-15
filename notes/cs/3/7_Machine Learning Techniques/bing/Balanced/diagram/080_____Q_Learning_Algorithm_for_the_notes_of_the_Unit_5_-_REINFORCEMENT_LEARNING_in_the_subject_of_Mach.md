### Q Learning Algorithm

Q learning is a model-free, value-based, off-policy reinforcement learning algorithm that learns the value of an action in a particular state. It does not require a model of the environment, and it can handle problems with stochastic transitions and rewards. The goal of Q learning is to find the optimal action-selection policy that maximizes the expected cumulative reward over time.

The main components of Q learning are:

- A set of states S, where the agent can be at any given time.
- A set of actions A, where the agent can choose to perform at each state.
- A reward function R, where the agent receives a scalar reward for each state-action pair.
- A discount factor γ, where the agent discounts future rewards by a factor of 0 ≤ γ ≤ 1.
- A Q table Q, where the agent stores the estimated value of each state-action pair.

The Q table is initialized randomly or with zeros, and then updated iteratively using the following formula:

Q(s, a) ← Q(s, a) + α [r + γ max Q(s', a') - Q(s, a)]

where:

- s is the current state
- a is the current action
- r is the immediate reward
- s' is the next state
- a' is the next action
- α is the learning rate, which controls how much the Q table is updated at each step

The Q learning algorithm follows these steps:

1. Initialize the Q table with random or zero values.
2. Observe the current state s.
3. Choose an action a based on an exploration-exploitation trade-off, such as epsilon-greedy, which selects a random action with probability ε and the best action with probability 1 - ε.
4. Execute the action a and observe the next state s' and the reward r.
5. Update the Q table using the formula above.
6. Set the current state to the next state: s ← s'.
7. Repeat steps 2 to 6 until the Q table converges or a termination condition is met.

Q learning is a simple and powerful algorithm that can learn optimal policies for many reinforcement learning problems. However, it also has some limitations, such as:

- It requires a large amount of memory and computation to store and update the Q table for large state and action spaces.
- It may not converge to the optimal policy if the learning rate or the exploration rate are not set properly.
- It may be affected by noisy or delayed rewards, which can make the Q table inaccurate or unstable.