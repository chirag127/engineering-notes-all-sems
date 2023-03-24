 Here is the content in markdown format without any emojis or external links, written in points and in a formal tone:

### Q Learning for the notes of the Unit 5 - REINFORCEMENT LEARNING in the subject of Machine Learning Techniques

1. Q Learning is a model-free reinforcement learning algorithm. It does not require a model of the environment and can handle problems with stochastic transitions and rewards.
2. The goal of Q Learning is to learn a policy which tells an agent what action to take under what circumstances. It does so by learning an action-value function (Q function) which evaluates the long-term reward for each action in each state.
3. The Q function is estimated based on the agent's interaction with the environment. The agent selects actions and observes rewards and next states. Based on this, it updates its Q estimates, thereby gradually learning to predict the long-term reward of state-action pairs and learning an optimal policy.
4. The Q update rule is:
Q(s, a) = Q(s, a) + alpha * (reward + gamma * max(Q(s', a')) - Q(s, a))
where alpha is the learning rate, gamma is the discount factor, s is the current state, a is the current action, s' is the next state and reward is the immediate reward received after taking action a in state s.
5. As the agent interacts with the environment, its Q estimates get more and more accurate, allowing it to determine better actions to take. An epsilon-greedy policy is commonly used to balance between exploration and exploitation. With probability epsilon, a random action is selected for exploration, otherwise the action with the highest Q value is selected for exploitation.