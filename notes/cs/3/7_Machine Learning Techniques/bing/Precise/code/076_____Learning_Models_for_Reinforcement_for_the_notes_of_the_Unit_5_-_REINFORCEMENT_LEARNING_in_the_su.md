### Learning Models for Reinforcement

Reinforcement learning is a type of machine learning technique that enables an agent to learn in an interactive environment by trial and error using feedback from its own actions and experiences. Here are some of the learning models used in reinforcement learning:

1. **Q-Learning**: Q-learning is a model-free reinforcement learning algorithm that seeks to find the best action to take given the current state. It does this by learning an action-value function that ultimately gives the expected utility of taking a given action in a given state and following the optimal policy thereafter.

2. **SARSA**: SARSA is an on-policy reinforcement learning algorithm that estimates the value of the current state-action pair based on the current policy. It is similar to Q-learning, but instead of using the maximum reward of the next state, it uses the reward of the action that is actually taken.

3. **Monte Carlo Methods**: Monte Carlo methods are a class of reinforcement learning algorithms that learn directly from episodes of experience without any prior knowledge of the environment's dynamics. They estimate the value of a state-action pair by averaging the returns observed after taking that action in that state.

4. **Temporal Difference Learning**: Temporal difference learning is a combination of Monte Carlo methods and dynamic programming. It estimates the value of a state-action pair by updating the value function after each time step, using the difference between the observed reward and the expected reward.

These are some of the commonly used learning models in reinforcement learning. Each model has its own strengths and weaknesses and can be applied to different types of problems. It is important to choose the right model for the specific problem at hand.