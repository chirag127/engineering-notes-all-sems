 Here is the content in markdown format with formal tone and without emojis:

### Q Learning Algorithm

1. Q Learning is a model-free reinforcement learning algorithm.
2. It learns an action-value function (Q function) that gives the expected reward for taking an action in a given state & following the optimal policy thereafter.
3. The goal is to learn the optimal action-selection policy that maximizes the expected reward over the long run.
4. The Q function is updated using the Bellman equation - Q(s,a) = r + gamma*max[Q(s',a')]. Here, r is the immediate reward, gamma is the discount factor and s' is the next state.
5. The Q-table (table of Q values) is initialized with random values and the agent interacts with the environment, observing rewards and updating Q values based on the rewards.
6. With each interaction, the algorithm converges to the optimal Q-function and optimal policy.
7. The key steps in Q Learning are:
    1. Initialize Q(s,a) arbitrarily
    2. Repeat:
        1. Take action a in state s and observe reward r and next state s'
        2. Compute Q(s,a) = r + gamma * max[Q(s',a')]
        3. Update Q(s,a) = Q(s,a) + alpha * [Q(s,a) - Q(s,a)]
        4. s <- s'
8. Q Learning is a simple yet powerful algorithm that has been applied to a variety of problems. However, it does not scale well to problems with large state-action spaces due to the creation and storage of the Q-table.