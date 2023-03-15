## Unit 5 - REINFORCEMENT LEARNING

Reinforcement learning is a machine learning paradigm that aims to learn optimal actions in an environment based on rewards and penalties. It is inspired by behaviorist psychology and how humans and animals learn from trial and error. A reinforcement learning agent interacts with its environment and observes the consequences of its actions, such as receiving a positive or negative reward. The agent then adjusts its behavior to maximize the expected cumulative reward over time.

Some key concepts and components of reinforcement learning are:

- **Agent**: The entity that learns and acts in the environment. It can be a software program, a robot, a game player, etc.
- **Environment**: The external system that the agent interacts with. It can be a physical world, a simulated world, a board game, etc.
- **State**: The representation of the agent's current situation in the environment. It can be a vector of features, an image, a board position, etc.
- **Action**: The choice that the agent makes in each state. It can be a discrete or continuous variable, such as moving left or right, selecting a card, applying a force, etc.
- **Reward**: The immediate feedback that the agent receives from the environment after taking an action. It can be a scalar value, such as a score, a penalty, a profit, etc.
- **Policy**: The strategy that the agent follows to select actions in each state. It can be a deterministic or stochastic function, such as a lookup table, a neural network, a probability distribution, etc.
- **Value function**: The estimation of the expected cumulative reward that the agent can obtain from each state or state-action pair. It can be a scalar or vector function, such as a linear approximation, a neural network, a tree, etc.
- **Model**: The prediction of the next state and reward that the agent will encounter after taking an action. It can be a deterministic or stochastic function, such as a transition matrix, a neural network, a probability distribution, etc.

Reinforcement learning can be classified into different types based on the availability and use of the reward, value function, and model. Some common types are:

- **Model-based vs. model-free**: Model-based methods use a model of the environment to plan ahead and select actions, while model-free methods learn directly from experience and do not rely on a model.
- **Value-based vs. policy-based**: Value-based methods learn a value function and derive a policy from it, while policy-based methods learn a policy directly and do not use a value function.
- **Monte Carlo vs. temporal difference**: Monte Carlo methods learn from complete episodes and use the average return as the value estimate, while temporal difference methods learn from incomplete episodes and use the difference between successive value estimates as the learning signal.
- **On-policy vs. off-policy**: On-policy methods learn the value or policy of the behavior that they follow, while off-policy methods learn the value or policy of a different behavior than the one they follow.
- **Exploration vs. exploitation**: Exploration is the act of trying new actions to discover their effects and improve the agent's knowledge, while exploitation is the act of choosing the best known action to maximize the reward. A trade-off between exploration and exploitation is essential for effective reinforcement learning.