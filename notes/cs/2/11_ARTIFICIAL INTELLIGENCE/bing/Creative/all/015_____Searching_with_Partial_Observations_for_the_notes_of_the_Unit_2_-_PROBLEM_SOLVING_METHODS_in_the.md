# Searching with Partial Observations

- Searching with partial observations is a problem-solving method in artificial intelligence that deals with environments that are **partially observable**, meaning that the agent cannot access the complete state of the environment at any given time .
- In such environments, an agent can be in one of several possible states, and an action can lead to one of several possible outcomes. The agent has to rely on its **percepts**, which are the sensory inputs that provide partial information about the environment .
- A common approach to searching with partial observations is to use a **belief state**, which is a set of possible states that the agent considers consistent with its percepts and actions. The agent can then search for a sequence of actions that leads to a goal belief state, where the goal is known to be true in at least one of the possible states.
- Another approach is to use **learning** techniques to infer the underlying **action model** of the environment, which specifies how the actions affect the states and the percepts. The agent can then use the learned action model to plan its actions and update its beliefs.
- Searching with partial observations can be applied to various domains, such as robotics, games, planning, diagnosis, and multi-agent systems . Some examples of partially observable environments are:

  - A vacuum cleaner agent that has a position sensor and a local dirt sensor, but no dirt sensor for other squares.
  - An 8-puzzle agent that can see only the upper-left corner square of the board.
  - A multi-agent system where each agent has partial observations of its neighbors' states and utilities.