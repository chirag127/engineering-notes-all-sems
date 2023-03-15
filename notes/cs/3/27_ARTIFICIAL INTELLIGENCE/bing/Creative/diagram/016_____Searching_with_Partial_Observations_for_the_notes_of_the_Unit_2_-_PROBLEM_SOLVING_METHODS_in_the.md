# Searching with Partial Observations

- Searching with partial observations is a problem-solving method in artificial intelligence that deals with environments that are **partially observable**, meaning that the agent cannot access the complete state of the environment at any given time.
- In such environments, the agent has to rely on **percepts**, which are pieces of information that the agent receives from its sensors, such as vision, sound, touch, etc.
- Percepts may be **incomplete**, meaning that they do not cover all the aspects of the environment, or **noisy**, meaning that they may contain errors or uncertainties.
- The agent has to use its percepts to **infer** the possible states of the environment and choose the best action to achieve its goal.
- Searching with partial observations can be modeled as a **contingency problem**, where the agent has to plan for different outcomes of its actions depending on the percepts it receives.
- A contingency problem can be represented as a **contingency tree**, where the nodes are states of the environment, the edges are actions, and the branches are percepts.
- The agent has to search the contingency tree for a **solution path**, which is a sequence of actions that leads to a goal state in any possible scenario.
- Searching the contingency tree can be done using **depth-first search**, **breadth-first search**, or **heuristic search** algorithms, depending on the size and complexity of the problem.
- Searching with partial observations can be applied to various domains, such as robotics, navigation, games, diagnosis, etc.