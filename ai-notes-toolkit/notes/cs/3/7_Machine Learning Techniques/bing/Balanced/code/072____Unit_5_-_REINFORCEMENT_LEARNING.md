## Unit 5 - REINFORCEMENT LEARNING

Reinforcement learning is a machine learning technique that learns how to optimize sequential decisions based on rewards and penalties. It is inspired by how humans and animals learn from their own experiences and actions.

Some key concepts and elements of reinforcement learning are:

- **Agent**: The entity that interacts with the environment and learns from it. The agent can be a robot, a computer program, a game player, etc.
- **Environment**: The system or situation that the agent operates in. The environment can be physical, virtual, or simulated. It provides feedback to the agent in the form of rewards and penalties.
- **Action**: The choice that the agent makes at each time step. The action can be discrete or continuous, deterministic or stochastic, etc.
- **State**: The representation of the environment at a given time. The state can be fully or partially observable, static or dynamic, etc.
- **Reward**: The numerical feedback that the environment gives to the agent after each action. The reward can be positive or negative, immediate or delayed, etc. The goal of the agent is to maximize the total reward over time.
- **Policy**: The strategy or rule that the agent follows to select actions. The policy can be deterministic or stochastic, explicit or implicit, etc.
- **Value function**: The estimation of the expected future reward for each state or state-action pair. The value function can be used to evaluate the quality of a policy or to guide the agent's action selection.
- **Model**: The approximation of the environment's dynamics and behavior. The model can be used to predict the next state and reward given the current state and action. The model can be known, unknown, or learned by the agent.

There are different types of reinforcement learning algorithms, such as:

- **Model-based**: The agent uses a model of the environment to plan ahead and select the best action. For example, dynamic programming, Monte Carlo tree search, etc.
- **Model-free**: The agent does not use a model of the environment, but learns directly from its own experience. For example, temporal difference learning, Q-learning, policy gradient, etc.
- **On-policy**: The agent learns the value function or the policy based on the actions it actually takes. For example, SARSA, REINFORCE, etc.
- **Off-policy**: The agent learns the value function or the policy based on the actions it would take under a different policy. For example, Q-learning, actor-critic, etc.
- **Exploration**: The agent tries new or uncertain actions to gain more information and improve its learning. For example, epsilon-greedy, softmax, etc.
- **Exploitation**: The agent exploits its current knowledge and selects the best action according to its value function or policy. For example, greedy, optimistic, etc.