## Unit 5 - REINFORCEMENT LEARNING

Reinforcement learning is a machine learning paradigm that is based on learning from the consequences of actions. It is inspired by behaviorist psychology, where an agent learns to perform a task by trial and error, receiving rewards or punishments for its actions  .

Some key concepts of reinforcement learning are:

- **Agent**: The entity that interacts with the environment and learns from its feedback. The agent can be a robot, a software program, a game player, etc.
- **Environment**: The world that the agent operates in and receives observations and rewards from. The environment can be physical, virtual, simulated, etc.
- **Action**: The choice that the agent makes at each time step. The action can be discrete (e.g., move left or right) or continuous (e.g., apply a certain force or angle).
- **State**: The representation of the situation that the agent is in. The state can be fully observable (e.g., the position and velocity of a car) or partially observable (e.g., the hidden cards in a poker game).
- **Reward**: The numerical feedback that the agent receives from the environment after taking an action. The reward can be positive (e.g., reaching a goal) or negative (e.g., hitting an obstacle).
- **Policy**: The strategy that the agent follows to select actions. The policy can be deterministic (e.g., always take the action that maximizes the expected reward) or stochastic (e.g., take actions according to a probability distribution).
- **Value function**: The function that estimates the long-term value of a state or an action. The value function can be state-value (e.g., the expected total reward from a given state) or action-value (e.g., the expected total reward from taking a given action in a given state).
- **Model**: The function that predicts the next state and reward given the current state and action. The model can be known (e.g., the rules of a chess game) or unknown (e.g., the dynamics of a complex system).

The goal of reinforcement learning is to find the optimal policy that maximizes the expected cumulative reward over time. There are different types of reinforcement learning algorithms, such as:

- **Model-based**: These algorithms use a model of the environment to plan ahead and evaluate the consequences of actions. They can be more efficient and accurate, but they require a reliable and complete model, which may not be available or feasible in some cases.
- **Model-free**: These algorithms do not use a model of the environment, but rely on direct experience and learning from trial and error. They can be more flexible and adaptable, but they may require more data and exploration, and may suffer from high variance and bias.
- **Value-based**: These algorithms learn a value function that estimates the value of states or actions, and use it to derive a policy. They can be more stable and consistent, but they may not handle multiple optimal actions well, and may be affected by the curse of dimensionality.
- **Policy-based**: These algorithms learn a policy directly, without using a value function. They can handle multiple optimal actions well, and can deal with high-dimensional and continuous action spaces, but they may be less stable and more sensitive to initial conditions and hyperparameters.
- **Actor-critic**: These algorithms combine the advantages of value-based and policy-based methods, by using both a value function and a policy. The value function (critic) evaluates the policy (actor) and provides a learning signal to improve it. They can be more efficient and robust, but they may also inherit the drawbacks of both methods.