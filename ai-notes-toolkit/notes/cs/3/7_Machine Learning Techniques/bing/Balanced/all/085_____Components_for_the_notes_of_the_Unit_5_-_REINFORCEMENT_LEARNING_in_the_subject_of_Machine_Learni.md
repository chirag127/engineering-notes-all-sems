# Components for the notes of the Unit 5 - REINFORCEMENT LEARNING in the subject of Machine Learning Techniques

- Reinforcement learning (RL) is a type of machine learning that learns from its own actions and rewards, without explicit supervision or labels.
- RL agents interact with an environment, which provides them with observations, actions, and rewards. The goal of RL is to learn a policy that maximizes the expected cumulative reward over time.
- The main components of RL are:
  - Agent: The entity that learns and acts in the environment.
  - Environment: The system that the agent interacts with, which can be deterministic or stochastic, fully or partially observable, discrete or continuous, etc.
  - State: The representation of the agent's current situation in the environment, which can be observed or hidden.
  - Action: The choice that the agent makes at each time step, which affects the state and the reward.
  - Reward: The immediate feedback that the agent receives from the environment after taking an action, which can be positive or negative, scalar or vector, etc.
  - Policy: The function that maps states to actions, which can be deterministic or stochastic, explicit or implicit, etc.
  - Value: The function that estimates the long-term desirability of states or actions, which can be state-value or action-value, model-based or model-free, etc.
  - Model: The function that predicts the next state and reward given the current state and action, which can be learned or given, accurate or approximate, etc.
- RL algorithms can be classified into three categories:
  - Model-based: These algorithms use a model of the environment to plan ahead and select the best actions, which can be optimal or suboptimal, exact or approximate, etc. Examples are value iteration, policy iteration, Monte Carlo tree search, etc.
  - Model-free: These algorithms do not use a model of the environment, but rely on trial-and-error learning to update the policy or value function, which can be on-policy or off-policy, temporal-difference or Monte Carlo, etc. Examples are Q-learning, SARSA, REINFORCE, etc.
  - Model-learning: These algorithms learn a model of the environment from the agent's experience, and use it to improve the policy or value function, which can be online or offline, supervised or unsupervised, etc. Examples are Dyna-Q, PILCO, MBMF, etc.
- RL applications can be found in various domains, such as robotics, games, control, optimization, recommendation, etc.