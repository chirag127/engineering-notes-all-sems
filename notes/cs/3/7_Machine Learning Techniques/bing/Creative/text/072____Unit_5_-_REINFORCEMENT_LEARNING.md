## Unit 5 - REINFORCEMENT LEARNING

- Reinforcement learning is a machine learning training method based on rewarding desired behaviors and/or punishing undesired ones.
- Reinforcement learning is about learning the optimal behavior in an environment to obtain maximum reward.
- Reinforcement learning can be used to optimize sequential decisions, which are decisions that are taken recurrently across time steps, for example, daily stock replenishment decisions taken in inventory control.
- Reinforcement learning mimics how we, as humans, learn through interactions with the environment and observations of how it responds, similar to children exploring the world around them and learning the actions that lead to positive outcomes.
- Reinforcement learning elements are as follows:
  - Policy: A policy defines the learning agent's way of behaving at a given time. It is a mapping from the state of the environment to the action to be taken by the agent.
  - Reward function: A reward function defines the goal of the learning agent. It is a scalar feedback signal that indicates how well the agent is doing at a given time step. The agent's objective is to maximize the total reward it receives over time.
  - Value function: A value function specifies what is good in the long run. It is the expected total reward that can be obtained from a given state or action. It helps the agent to select the best action that leads to the highest future reward.
  - Model of the environment: A model of the environment predicts how the environment will change in response to the agent's actions. It can be used to plan ahead and evaluate the consequences of different actions. A model is optional, and some reinforcement learning methods can learn without a model.