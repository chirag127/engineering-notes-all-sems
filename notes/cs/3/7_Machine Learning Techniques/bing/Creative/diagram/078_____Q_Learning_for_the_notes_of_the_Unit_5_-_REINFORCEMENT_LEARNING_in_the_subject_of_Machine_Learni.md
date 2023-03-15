### Q Learning

Q learning is a model-free, off-policy reinforcement learning algorithm that will find the best course of action, given the current state of the agent. Depending on where the agent is in the environment, it will decide the next action to be taken. The objective of the model is to find the best course of action given its current state.

Some key points about Q learning are:

- Q learning is based on a Q table, which is a matrix that stores the value of taking an action in a state.
- Q learning does not require a model of the environment, and it can handle problems with stochastic transitions and rewards without requiring adaptations.
- Q learning is considered off-policy because the Q function learns from actions that are outside the current policy, like taking random actions, and therefore a policy is not needed.
- Q learning uses a learning rate and a discount factor to update the Q table based on the observed rewards and the expected future rewards.
- Q learning converges to the optimal Q function under certain conditions, such as infinite exploration and a sufficiently small learning rate.

A general algorithm for Q learning is:

- Initialize the Q table with arbitrary values, and set the learning rate and the discount factor.
- Repeat until convergence or termination:
  - Observe the current state s and choose an action a based on an exploration strategy (e.g., epsilon-greedy).
  - Execute the action a and observe the next state s' and the reward r.
  - Update the Q table using the formula: Q(s, a) = Q(s, a) + alpha * (r + gamma * max Q(s', a') - Q(s, a)), where alpha is the learning rate and gamma is the discount factor.
  - Set the current state to the next state: s = s'.