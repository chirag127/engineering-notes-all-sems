 Here is the content in markdown format without any emojis or external links and in a formal tone:

## Unit 5 - REINFORCEMENT LEARNING

1. Reinforcement Learning: Reinforcement learning is a type of machine learning algorithm that learns by interacting with its environment. The agent learns the behavior that maximizes the reward through trial-and-error using feedback from the environment.

2. Markove Decision Process (MDP): Reinforcement learning problems can be formulated as Markov Decision Processes (MDPs). An MDP is a tuple (S, A, P, R, gamma) where:

- S is a set of states
- A is a set of actions
- P(s'|s,a) is the transition probability of transitioning from state s to s' when action a is taken
- R(s,a) is the reward function
- gamma is the discount factor

3. Policy: A policy is a mapping from states (or state-action pairs) to probabilities of selecting each possible action. The goal of reinforcement learning is to find an optimal policy.

4. Value Function: The value function refers to the expected return when starting from a given state and following a given policy. The optimal value function is the maximum expected return achievable from a given state.

5. Q-Learning: Q-learning is a model-free reinforcement learning algorithm. It learns an action-value function that estimates the long-term reward for taking a given action in a given state. It does not require a model of the environment and can handle problems with discrete state/action spaces.

6. Deep Q-Network (DQN): DQN is a deep neural network agent that can learn complex control policies directly from high-dimensional sensory input using reinforcement learning. It is a deep reinforcement learning algorithm that combines Q-learning with a deep neural network to learn successful policies.