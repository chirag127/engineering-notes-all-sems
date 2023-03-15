# Learning Task for the notes of the Unit 5 - REINFORCEMENT LEARNING in the subject of Machine Learning Techniques

Reinforcement learning is a machine learning technique that learns how to optimize sequential decisions based on rewards and penalties. It is inspired by how humans and animals learn from their own experiences and actions.

## Basic Concepts of Reinforcement Learning

- **Agent**: The entity that interacts with the environment and learns from it. For example, a robot, a game player, or a stock trader.
- **Environment**: The system that the agent interacts with and receives feedback from. For example, a maze, a chess board, or a stock market.
- **State**: The representation of the situation that the agent is in at a given time. For example, the position of the robot, the configuration of the chess board, or the price of the stocks.
- **Action**: The choice that the agent makes in each state. For example, moving left, right, up, or down, making a chess move, or buying or selling a stock.
- **Reward**: The immediate feedback that the agent receives from the environment after taking an action. For example, a positive reward for reaching the goal, a negative reward for hitting a wall, or a profit or loss for a trade.
- **Policy**: The strategy that the agent follows to select actions in each state. For example, a rule-based policy, a random policy, or a learned policy.
- **Value function**: The estimation of the long-term expected return for each state or state-action pair. For example, the value of being in a certain position, or the value of taking a certain action in a certain position.
- **Model**: The representation of the dynamics of the environment, that is, how the environment transitions from one state to another after an action, and what reward is obtained. For example, a deterministic model, a probabilistic model, or a learned model.

## Types of Reinforcement Learning

- **Model-based reinforcement learning**: The agent has access to a model of the environment, and uses it to plan ahead and evaluate the consequences of its actions. For example, a chess player that can simulate the moves of the opponent and the resulting board states.
- **Model-free reinforcement learning**: The agent does not have access to a model of the environment, and relies on trial and error to learn from its own experiences. For example, a robot that learns to navigate a maze by exploring and remembering the rewards it obtains.
- **Value-based reinforcement learning**: The agent learns a value function that estimates the expected return for each state or state-action pair, and uses it to select the best action in each state. For example, a stock trader that learns the value of holding or selling a stock in different market conditions.
- **Policy-based reinforcement learning**: The agent learns a policy that directly maps states to actions, without using a value function. For example, a game player that learns to choose actions based on the features of the game state.
- **Actor-critic reinforcement learning**: The agent learns both a value function and a policy, and uses the value function to update the policy. For example, a robot that learns to balance a pole by adjusting its policy based on the value of its actions.

## Algorithms of Reinforcement Learning

- **Dynamic programming**: A model-based value-based method that uses the Bellman equation to iteratively compute the optimal value function and policy for a finite and fully observable environment. For example, value iteration and policy iteration.
- **Monte Carlo methods**: A model-free value-based method that uses sampling to estimate the value function and policy for an episodic and partially observable environment. For example, first-visit Monte Carlo and every-visit Monte Carlo.
- **Temporal difference learning**: A model-free value-based method that combines dynamic programming and Monte Carlo methods to update the value function and policy online, without waiting for the end of an episode. For example, SARSA and Q-learning.
- **Policy gradient methods**: A model-free policy-based method that uses gradient ascent to optimize the policy directly, without using a value function. For example, REINFORCE and actor-critic methods.
- **Deep reinforcement learning**: A model-free method that uses deep neural networks to represent the value function, the policy, or the model, and applies advanced optimization techniques to handle high-dimensional and complex environments. For example, deep Q-networks, deep deterministic policy gradients, and deep recurrent Q-networks.