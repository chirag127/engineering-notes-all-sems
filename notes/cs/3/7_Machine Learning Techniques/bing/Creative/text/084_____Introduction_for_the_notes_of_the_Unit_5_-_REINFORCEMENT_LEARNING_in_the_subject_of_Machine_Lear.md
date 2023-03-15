### Introduction for the notes of the Unit 5 - REINFORCEMENT LEARNING in the subject of Machine Learning Techniques

- Reinforcement learning (RL) is a branch of machine learning that deals with learning from actions and rewards.
- RL is inspired by the way humans and animals learn from trial and error, and from positive and negative feedback.
- RL differs from supervised learning and unsupervised learning in that it does not require labeled data or predefined clusters, but rather learns from its own experience and interaction with the environment.
- RL agents are software or hardware systems that can perceive their state, take actions, and receive rewards or penalties from the environment.
- RL agents aim to maximize their cumulative reward over time by learning a policy, which is a function that maps states to actions.
- RL problems can be modeled as Markov decision processes (MDPs), which are mathematical frameworks that capture the dynamics of stochastic environments with discrete states and actions.
- MDPs are characterized by four components: a set of states, a set of actions, a transition function, and a reward function.
- The transition function specifies the probability of moving from one state to another given an action, and the reward function specifies the immediate reward or penalty received after taking an action in a state.
- The value function is a function that estimates the expected long-term reward of being in a state, and the Q-function is a function that estimates the expected long-term reward of taking an action in a state.
- RL algorithms can be classified into three categories: value-based, policy-based, and actor-critic methods.
- Value-based methods learn the value function or the Q-function, and derive the policy implicitly from them. Examples of value-based methods are temporal difference (TD) learning, Q-learning, and SARSA.
- Policy-based methods learn the policy directly, without using a value function or a Q-function. Examples of policy-based methods are policy iteration, policy gradient, and REINFORCE.
- Actor-critic methods combine value-based and policy-based methods, by using an actor that learns the policy and a critic that learns the value function or the Q-function. Examples of actor-critic methods are advantage actor-critic (A2C), deep deterministic policy gradient (DDPG), and proximal policy optimization (PPO).
- RL can be applied to various domains, such as robotics, games, control, optimization, and natural language processing. Some of the challenges and limitations of RL are exploration-exploitation trade-off, partial observability, high dimensionality, delayed rewards, and safety.