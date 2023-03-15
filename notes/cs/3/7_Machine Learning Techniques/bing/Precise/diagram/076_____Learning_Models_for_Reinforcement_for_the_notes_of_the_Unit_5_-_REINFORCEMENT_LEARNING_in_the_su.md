### Learning Models for Reinforcement

Reinforcement learning is a type of machine learning technique that enables an agent to learn in an interactive environment by trial and error using feedback from its own actions and experiences. Here are some of the learning models for reinforcement learning:

1. **Q-Learning**: Q-learning is a model-free reinforcement learning algorithm. The goal of Q-learning is to learn a policy, which tells an agent what action to take under what circumstances. It does not require a model of the environment and can handle problems with stochastic transitions and rewards, without requiring adaptations.

2. **SARSA**: SARSA is an on-policy reinforcement learning algorithm. It is similar to Q-learning, but the main difference is that the maximum reward for the next state is not necessarily used for updating the Q-values. Instead, the Q-value of the next state and the next action that the current policy would choose is used.

3. **Deep Q-Networks (DQN)**: Deep Q-Networks (DQN) is a model-free, online, off-policy reinforcement learning method. It combines Q-Learning with deep neural networks at scale. DQN was able to handle high-dimensional sensory inputs and was the first to successfully learn control policies directly from high-dimensional sensory input using reinforcement learning.

4. **Monte Carlo Methods**: Monte Carlo methods are a class of reinforcement learning algorithms that learn directly from episodes of experience without any prior knowledge of the environment's dynamics. Monte Carlo methods are based on averaging sample returns, with the key idea being to learn by averaging over many random samples of an agent's experience.

5. **Temporal Difference (TD) Learning**: Temporal Difference (TD) learning is a combination of Monte Carlo ideas and dynamic programming (DP) ideas. Like Monte Carlo methods, TD methods can learn directly from raw experience without a model of the environment's dynamics. Like DP, TD methods update estimates based in part on other learned estimates, without waiting for a final outcome.

These are some of the learning models used in reinforcement learning. Each model has its own advantages and disadvantages and can be used in different scenarios depending on the problem at hand.