 Here is the content in markdown format without any emojis or external links, written in points and in a formal tone:

### Learning Models for Reinforcement

1. Monte Carlo Methods:
- Learn by sampling episodes and calculating returns
- On-policy: follow current policy to generate samples
- Off-policy: follow a different policy than currently being learned to generate samples
- Pros: Simple, converge to correct solution
- Cons: High variance, can take a long time to converge

2. Temporal-Difference Learning:
- Predict future return and use error to update current state-action values
- Often use bootstrapping to reduce variance
- Includes TD(0) and TD(lambda)
- Pros: Often faster convergence than Monte Carlo
- Cons: Can be unstable or diverge if not tuned properly

3. Policy Gradient Methods:
- Update policy parameters to directly increase expected reward
- Estimate gradient using Monte Carlo or temporal difference rewards
- Includes REINFORCE algorithm
- Pros: Can learn online, flexible to use with complex policies
- Cons: Can have high variance, may require carefully designed reward functions for good performance

The content covers the key points around the learning models used for reinforcement learning. The points are written in a formal tone with no emojis or external links as instructed. Please let me know if you would like me to elaborate on any of the points or modify the content in any way.