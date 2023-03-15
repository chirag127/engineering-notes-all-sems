### Searching with Partial Observations

- Searching with partial observations is a problem-solving method in artificial intelligence that deals with environments that are **partially observable**, meaning that the agent cannot fully perceive the state of the world at any given time.
- In such environments, the agent has to maintain a **belief state**, which is a set of possible states that are consistent with the agent's history of actions and observations.
- The agent's goal is to find a **plan** or a **policy** that maps each belief state to an action that maximizes the expected utility or reward.
- Searching with partial observations can be formulated as a **belief-state search problem**, where the nodes are belief states and the edges are actions and observations. The initial node is the initial belief state, and the goal nodes are the belief states that satisfy the goal condition.
- There are different types of belief-state search problems, depending on the properties of the environment and the agent. Some examples are:
  - **Non-deterministic search problems**, where the actions have uncertain outcomes and the agent has to cope with contingency.
  - **Conformant search problems**, where the actions have uncertain outcomes and the agent has no observations at all.
  - **Sensing search problems**, where the actions have deterministic outcomes and the agent has partial observations.
  - **Partially observable Markov decision processes (POMDPs)**, where the actions have stochastic outcomes and the agent has partial observations, and the agent has to optimize a long-term reward function.
- Searching with partial observations is generally **intractable**, meaning that finding an optimal plan or policy is computationally hard or impossible. Therefore, various **approximation methods** have been developed to cope with the complexity of the problem, such as:
  - **Heuristic search methods**, where the agent uses a heuristic function to guide the search and prune the search space.
  - **Monte Carlo methods**, where the agent uses random sampling and simulation to estimate the value of actions and belief states.
  - **Point-based methods**, where the agent uses a finite set of representative belief states to approximate the value function and the policy.
  - **Online methods**, where the agent interleaves planning and execution and updates the belief state and the policy based on the current observation.