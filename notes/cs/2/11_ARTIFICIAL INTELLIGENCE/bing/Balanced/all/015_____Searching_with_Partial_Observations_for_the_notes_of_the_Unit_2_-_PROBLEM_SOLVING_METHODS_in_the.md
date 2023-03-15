# Searching with Partial Observations

- Searching with partial observations is a problem-solving method in artificial intelligence that deals with environments that are **partially observable**, meaning that the agent cannot access the complete state of the environment at any given time.
- Partial observability can arise due to **limited sensors**, **noise**, **uncertainty**, or **hidden variables** in the environment.
- A partial observation is a **subset** of the information that is available in the full state of the environment. For example, a vacuum agent may only have a position and a local dirt sensor, but not a dirt sensor for other squares.
- A partial observation can also be a **function** of the full state, such as a potential utility estimation or a load information of a neighbor agent.
- Searching with partial observations requires the agent to maintain a **belief state**, which is a set of possible states that are consistent with the agent's observations and actions.
- A belief state can be represented as a **probability distribution** over the full states, or as a **logical formula** that captures the constraints on the full states.
- A belief state can be updated using **Bayes' rule** or **logical inference** after each observation or action.
- Searching with partial observations can be done using **search trees**, where each node is a belief state, and each edge is an action or an observation.
- The goal of searching with partial observations is to find a **plan** or a **policy** that guides the agent to achieve its objective, such as reaching a goal state, maximizing a reward function, or minimizing a cost function.
- Searching with partial observations can be **challenging** due to the **exponential growth** of the belief state space, the **incompleteness** of the observations, and the **non-determinism** of the actions and the environment.
- Searching with partial observations can be **simplified** by using **heuristics**, **approximations**, **abstractions**, or **learning** techniques to reduce the complexity of the problem.