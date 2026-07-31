# Searching with Partial Observations

- Searching with partial observations is a problem-solving method in artificial intelligence that deals with environments that are **partially observable**, meaning that the agent cannot fully perceive the state of the world at any given time.
- Partial observability can arise due to **limited sensors**, **noise**, **uncertainty**, or **hidden variables** that affect the environment.
- In such environments, the agent needs to maintain a **belief state**, which is a set of possible states that are consistent with the agent's observations and actions.
- The agent's goal is to find a **plan** or a **policy** that maximizes its expected utility or reward over the belief state, taking into account the possible outcomes of its actions and the possible observations it might receive.
- Searching with partial observations can be formulated as a **partially observable Markov decision process (POMDP)**, which is a generalization of a Markov decision process (MDP) that incorporates uncertainty in both the state transitions and the observations.
- A POMDP is defined by a tuple <S, A, T, R, O, Z>, where:
  - S is a finite set of states
  - A is a finite set of actions
  - T is a state transition function that maps S x A x S to the probability of reaching state s' after taking action a in state s
  - R is a reward function that maps S x A to the immediate reward of taking action a in state s
  - O is a finite set of observations
  - Z is an observation function that maps S x A x O to the probability of receiving observation o after taking action a in state s
- A solution to a POMDP is a **policy** that maps each belief state to an action that maximizes the expected value of the objective function, which can be the total reward, the discounted reward, or the average reward over an infinite horizon.
- Solving a POMDP exactly is **NP-hard**, so various approximation methods have been developed, such as **value iteration**, **point-based value iteration**, **Monte Carlo tree search**, **policy iteration**, **policy gradient**, and **reinforcement learning**.
- Some examples of applications of searching with partial observations are **robot navigation**, **speech recognition**, **dialogue systems**, **medical diagnosis**, and **poker**.