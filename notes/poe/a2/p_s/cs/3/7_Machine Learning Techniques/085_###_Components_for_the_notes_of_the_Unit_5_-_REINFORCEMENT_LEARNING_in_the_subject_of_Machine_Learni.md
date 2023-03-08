 Here are the components I would include for notes on Reinforcement Learning in Machine Learning Techniques:

### Environment
- The environment is where the agent interacts and performs actions. It is typically represented as a Markov Decision Process(MDP).
- An MDP is characterized by a set of states, actions, transition probabilities between states given actions, and rewards.
- The goal of the agent is to learn a policy for selecting actions that maximizes the cumulative reward over time.

### Agent
- The agent is the learner or decision-maker. It is the entity that interacts with the environment by sensing the state of the environment and performing actions.
- The agent's goal is to learn the optimal policy for selecting actions that maximizes reward. It does so by learning from interaction with the environment.

### Reward
- The reward is the evaluation of the outcome of the agent's actions. It determines the goal of the agent.
- The agent's goal is to maximize the cumulative reward over time by learning to select the actions that yield the highest reward in a given state.

### Policy
- A policy is the agent's strategy for selecting actions given states. It is a mapping from states to probabilities of selecting each possible action.
- The optimal policy is the one that maximizes expected cumulative reward. The agent's goal is to learn the optimal policy through interaction with the environment.

### Learning Methods
- There are 3 main types of RL learning methods: Monte Carlo methods, Temporal Difference learning, and Policy Gradient methods.
- Monte Carlo methods estimate the value of a policy by simulating paths through the environment and averaging returns.
- Temporal Difference methods update estimates based on differences between consecutive estimates and actual rewards. Examples include SARSA and Q-Learning.
- Policy Gradient methods directly update the policy by moving in the direction of higher reward. Examples include REINFORCE and Proximal Policy Optimization.

[Detailed diagrams, examples, pros/cons, applications, etc. could be included here for the above points]