### Q Learning Function

- Q learning is a model-free reinforcement learning algorithm that seeks to find the best action to take given the current state.
- Q learning does not require a model of the environment, and it can handle problems with stochastic transitions and rewards without requiring adaptations.
- Q learning can identify an optimal action-selection policy for any given finite Markov decision process (FMDP), given infinite exploration time and a partly-random policy.
- Q learning is based on the Q function, which represents the expected future rewards for taking an action in a given state .
- The Q function is defined as:

    Q(s, a) = E[r + γ max Q(s', a') | s, a]

    where s is the current state, a is the action, r is the immediate reward, γ is the discount factor, s' is the next state, and a' is the next action .

- The Q function is updated iteratively using the following rule:

    Q(s, a) ← Q(s, a) + α [r + γ max Q(s', a') - Q(s, a)]

    where α is the learning rate .

- The Q function can be implemented using a table, a neural network, or other function approximators .
- The Q function can be used to select the best action in each state by choosing the action that maximizes the Q value .
- The Q function can also be used to evaluate the performance of a policy by computing the expected return for following the policy from a given state .
- Q learning is an off-policy algorithm, because it learns from actions that are outside the current policy, like taking random actions, and therefore a policy is not needed .
- Q learning is based on the Bellman equation, which expresses the optimal value function as a recursive function of the immediate reward and the expected future value.