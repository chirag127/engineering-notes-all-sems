### Searching with Partial Observations

- In some problems, the agent does not have complete information about the state of the world, and can only observe some aspects of it.
- This is called **partial observability**, and it makes the search problem more challenging, as the agent has to deal with uncertainty and ambiguity.
- Partial observability can arise from various sources, such as noisy sensors, hidden variables, or limited vision.
- To cope with partial observability, the agent has to maintain a **belief state**, which is a set of possible states that are consistent with the agent's observations and actions.
- The agent's goal is to find a sequence of actions that leads to a goal state in any of the possible states in the belief state.
- A **belief state space** is a graph where the nodes are belief states and the edges are actions that change the belief state.
- A **solution** to a partially observable search problem is a path from the initial belief state to a goal belief state in the belief state space.
- There are different methods for searching with partial observations, such as:
  - **AND-OR search**: A tree-based search that alternates between AND nodes, which represent belief states, and OR nodes, which represent actions. The agent has to find a subtree that covers all possible states in the initial belief state and reaches a goal state in each branch.
  - **Sensorless search**: A graph-based search that ignores the observations and assumes that the agent knows the initial state. The agent has to find a sequence of actions that reaches a goal state in any possible state that can result from applying the actions.
  - **Conformant search**: A graph-based search that takes into account the observations and updates the belief state accordingly. The agent has to find a sequence of actions that reaches a goal state in any possible state that is consistent with the observations.
  - **Contingent search**: A tree-based search that plans for different contingencies based on the observations. The agent has to find a conditional plan that specifies what action to take for each possible observation, and reaches a goal state in any possible state that follows the plan.