### Searching with Partial Observations

- Searching with partial observations is a problem-solving method in artificial intelligence that deals with environments that are **partially observable**, meaning that the agent cannot fully perceive the state of the world at any given time .
- In such environments, an agent can be in one of several possible states, and an action can lead to one of several possible outcomes. Therefore, the agent needs to maintain a **belief state**, which is a set of possible states that are consistent with the agent's observations and actions.
- A belief state can be represented as a **contingency plan**, which is a tree of actions and observations that specifies what the agent should do in each possible situation. The goal of the agent is to find a contingency plan that reaches a goal state in every branch of the tree, or minimizes the expected cost of reaching a goal state.
- Searching for a contingency plan can be done using a **belief-state search** algorithm, which is similar to a standard search algorithm, except that it operates on belief states instead of single states. The algorithm starts with the initial belief state, which contains all possible states, and expands it by applying each possible action and generating a new belief state for each possible observation. The algorithm terminates when it finds a goal belief state, which contains only goal states, or when it exhausts the search space.
- Searching with partial observations can be challenging because the size of the belief state can grow exponentially with the number of actions and observations, and the search space can be infinite if the environment is non-deterministic. Therefore, some techniques to reduce the complexity of the problem are:

  - Using **heuristics** to guide the search and prune the search space.
  - Using **approximate representations** of belief states, such as sets of samples or probability distributions.
  - Using **learning algorithms** to infer the action models or the observation models of the environment from the data.
  - Using **distributed algorithms** to parallelize the search and exploit the dataflow graph-based programming model.