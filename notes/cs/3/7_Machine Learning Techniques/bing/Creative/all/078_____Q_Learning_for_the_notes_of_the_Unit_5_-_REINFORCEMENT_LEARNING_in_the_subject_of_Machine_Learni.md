# Q Learning

Q learning is a model-free, off-policy reinforcement learning algorithm that seeks to find the best action to take given the current state of the agent . It does not require a model of the environment, and it can handle problems with stochastic transitions and rewards. The objective of the algorithm is to learn a policy that maximizes the expected return for each state.

Some key concepts of Q learning are:

- Q function: A function that maps a state-action pair to a scalar value, representing the expected return from taking that action in that state. The Q function can be represented as a table, where each row corresponds to a state and each column corresponds to an action. The Q function is updated iteratively using the Bellman equation, which expresses the optimal value of a state-action pair as the sum of the immediate reward and the discounted value of the next state-action pair  .
- Exploration-exploitation trade-off: A dilemma faced by the agent, where it has to balance between taking actions that have high Q values (exploitation) and taking actions that have low Q values but may lead to new information and better Q values in the future (exploration). A common way to handle this trade-off is to use an epsilon-greedy policy, where the agent chooses a random action with a small probability epsilon, and chooses the action with the highest Q value with a probability of 1-epsilon .
- Learning rate: A parameter that controls how much the Q function is updated at each iteration. A high learning rate means that the Q function is updated more aggressively, while a low learning rate means that the Q function is updated more conservatively. The learning rate should be chosen carefully, as it affects the convergence and stability of the Q learning algorithm .
- Discount factor: A parameter that controls how much the agent values future rewards over immediate rewards. A high discount factor means that the agent is more far-sighted, while a low discount factor means that the agent is more short-sighted. The discount factor should be chosen carefully, as it affects the optimal policy and the convergence of the Q learning algorithm .

The pseudocode of the Q learning algorithm is as follows:

- Initialize the Q table with arbitrary values, and set the learning rate, discount factor, and epsilon
- Repeat for each episode:
  - Initialize the initial state
  - Repeat for each step of the episode:
    - Choose an action using the epsilon-greedy policy
    - Execute the action and observe the next state and reward
    - Update the Q table using the Bellman equation
    - Update the current state
  - Until the current state is terminal
- Return the Q table