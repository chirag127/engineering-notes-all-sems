### Searching with Partial Observations

- Searching with partial observations is a problem-solving method in artificial intelligence that deals with environments that are **partially observable**, meaning that the agent cannot access the complete state of the environment at any given time.
- In such environments, the agent has to rely on **percepts**, which are pieces of information that the agent receives from its sensors, such as vision, sound, touch, etc.
- Percepts may be **incomplete**, meaning that they do not cover all the aspects of the environment, or **uncertain**, meaning that they may be noisy, inaccurate, or ambiguous.
- The agent has to use its percepts to **infer** the possible states of the environment and choose the best action to achieve its goal.
- Searching with partial observations can be seen as a form of **belief-state search**, where the agent maintains a **belief state**, which is a set of possible states that are consistent with its percepts and actions.
- The agent updates its belief state after each action and percept, using a **transition model** that describes how the environment changes in response to actions, and an **observation model** that describes how the environment generates percepts.
- The agent's goal is to find a **plan**, which is a sequence of actions, that leads to a **goal state**, which is a state that satisfies some criteria.
- Searching with partial observations can be challenging because the agent has to deal with **exponential growth** of the belief state, **intractability** of finding optimal plans, and **incompleteness** of the models.
- Some examples of searching with partial observations are:
  - **Vacuum agent**: An agent that cleans a grid of squares, but can only sense its position and the dirtiness of the current square.
  - **8-puzzle**: A puzzle where the agent has to slide tiles to form a goal configuration, but can only see one corner of the board.
  - **Robot navigation**: A robot that has to move in an unknown environment, but can only sense the distance and direction of nearby obstacles.
  - **Action model learning**: An agent that has to learn the effects of its actions on the environment, but can only observe partial outcomes.
  - **Universal search**: A search algorithm that can solve any partially observable environment, but requires a lot of computation and memory.