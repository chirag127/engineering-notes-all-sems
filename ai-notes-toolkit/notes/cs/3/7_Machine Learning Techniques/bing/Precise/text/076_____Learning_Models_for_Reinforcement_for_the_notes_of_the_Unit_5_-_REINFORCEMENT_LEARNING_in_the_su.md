### Learning Models for Reinforcement

Reinforcement learning is a type of machine learning technique that enables an agent to learn in an interactive environment by trial and error using feedback from its own actions and experiences. Here are some of the learning models used in reinforcement learning:

1. **Q-Learning**: Q-Learning is an off-policy reinforcement learning algorithm that seeks to find the best action to take given the current state. It's considered off-policy because the Q-learning function learns from actions that are outside the current policy, like taking random actions, and therefore a policy isn't needed.

2. **SARSA**: SARSA is an on-policy reinforcement learning algorithm, which means that it learns the Q-values based on the actions the current policy dictates. It stands for State-Action-Reward-State-Action.

3. **Deep Q-Networks (DQN)**: DQN is a model-free, online, off-policy reinforcement learning method. It combines Q-Learning with deep neural networks at scale.

4. **Monte Carlo Methods**: Monte Carlo methods are a class of algorithms that rely on repeated random sampling to obtain numerical results. In reinforcement learning, Monte Carlo methods can be used to estimate the value function of a given policy.

5. **Temporal Difference (TD) Learning**: TD learning is a combination of Monte Carlo ideas and dynamic programming (DP) ideas. Like Monte Carlo methods, TD methods can learn directly from raw experience without a model of the environment's dynamics. Like DP, TD methods update estimates based in part on other learned estimates, without waiting for a final outcome.

These are some of the learning models used in reinforcement learning. Each model has its own advantages and disadvantages and can be used in different scenarios depending on the problem at hand. It is important to understand the underlying concepts and principles of each model in order to effectively apply them in reinforcement learning.