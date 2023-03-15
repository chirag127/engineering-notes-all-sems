### Q Learning Function

- Q learning is a **model-free reinforcement learning algorithm** that seeks to find the best action to take given the current state .
- The Q in Q learning represents **quality**, the algorithm seeks to know how useful a particular action is to be able to rake in maximum future reward .
- The Q function is defined as **Q(s, a)**, where **s** is the state and **a** is the action. It returns the expected future reward for taking action **a** in state **s** .
- The Q function is updated using the **Bellman equation**, which expresses the optimal value of a state-action pair as the sum of the immediate reward and the discounted value of the next state-action pair .
- The Bellman equation for Q learning is:

```math
Q(s, a) \leftarrow Q(s, a) + \alpha [r + \gamma \max_{a'} Q(s', a') - Q(s, a)]
```

where:

  - $\alpha$ is the **learning rate**, which controls how much the Q function is updated at each step.
  - $r$ is the **reward** received for taking action **a** in state **s**.
  - $\gamma$ is the **discount factor**, which controls how much the future rewards are valued compared to the immediate ones.
  - $\max_{a'} Q(s', a')$ is the **maximum Q value** for the next state **s'**, which represents the best possible action to take from that state.

- Q learning is an **off-policy** algorithm, because it learns from actions that are outside the current policy, like taking random actions, and therefore a policy is not needed  .
- Q learning can **identify an optimal action-selection policy** for any given finite Markov decision process (FMDP), given infinite exploration time and a partly-random policy.
- Q learning can handle problems with **stochastic transitions and rewards** without requiring adaptations.