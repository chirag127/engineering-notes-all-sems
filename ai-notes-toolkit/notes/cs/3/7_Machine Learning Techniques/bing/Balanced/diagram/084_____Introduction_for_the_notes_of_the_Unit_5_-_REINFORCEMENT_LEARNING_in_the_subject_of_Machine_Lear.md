### Introduction for the notes of the Unit 5 - REINFORCEMENT LEARNING in the subject of Machine Learning Techniques

- Reinforcement learning (RL) is a type of machine learning that learns from its own actions and rewards in an environment.
- RL is different from supervised learning, where the agent learns from labeled data, and unsupervised learning, where the agent learns from unlabeled data.
- RL is inspired by the way humans and animals learn from trial and error, and by the concepts of reward and punishment.
- RL can be applied to various domains, such as games, robotics, control, optimization, and decision making.
- RL can be formalized as a Markov decision process (MDP), which consists of four components: a set of states, a set of actions, a transition function, and a reward function.
- The goal of RL is to find an optimal policy, which is a function that maps each state to an action that maximizes the expected return, which is the cumulative discounted reward over time.
- RL can be classified into two categories: model-based and model-free. Model-based RL uses a model of the environment to plan ahead and choose actions, while model-free RL learns directly from experience without a model.
- RL can also be classified into two categories based on the type of feedback: on-policy and off-policy. On-policy RL learns from the actions that are actually taken by the agent, while off-policy RL learns from the actions that are not necessarily taken by the agent.
- RL algorithms can be divided into three groups: value-based, policy-based, and actor-critic. Value-based algorithms learn a value function that estimates the expected return for each state or state-action pair, and use it to derive a policy. Policy-based algorithms learn a policy function that directly outputs an action for each state. Actor-critic algorithms combine both value and policy functions, and use them to update each other.
- Some of the common RL algorithms are Q-learning, SARSA, Monte Carlo methods, temporal difference methods, policy gradient methods, and deep reinforcement learning methods.