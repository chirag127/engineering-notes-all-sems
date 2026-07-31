### Searching with Partial Observations

- Searching with partial observations is a problem-solving method in artificial intelligence that deals with environments that are **partially observable**, meaning that the agent cannot access the complete state of the environment at any given time.
- In such environments, the agent has to rely on **percepts**, which are pieces of information that the agent receives from its sensors, such as vision, sound, touch, etc.
- Percepts may be **incomplete**, meaning that they do not cover all the aspects of the environment, or **noisy**, meaning that they may contain errors or uncertainties.
- The agent has to use its **memory** and **inference** abilities to construct a **belief state**, which is a representation of the agent's knowledge and uncertainty about the environment.
- A belief state may be a **set** of possible states that the agent considers plausible, a **probability distribution** over the possible states, or a **logical formula** that captures the agent's beliefs and constraints.
- The agent has to choose an **action** that maximizes its expected utility, taking into account the possible outcomes of the action and the possible future percepts.
- The agent has to update its belief state based on the **feedback** from the environment, which may include the **effect** of the action and the **new percept**.
- Searching with partial observations is a **challenging** task, as the agent has to deal with **exponential** growth of the belief state, **uncertainty** and **inconsistency** of the percepts, and **non-determinism** and **unpredictability** of the environment.
- Some examples of searching with partial observations are:
  - **Vacuum agent**: an agent that cleans a grid of squares, but can only sense its position and the dirtiness of the current square.
  - **8-puzzle**: a sliding puzzle with 8 tiles and one blank space, but the agent can only see the upper-left corner square.
  - **Robot navigation**: a robot that moves in an unknown environment, but can only sense the distance and direction of nearby obstacles.
  - **Action model learning**: an agent that learns the effects of its actions on the environment, but can only observe partial and noisy feedback.
  - **Universal search**: an agent that searches for a goal state in any computable environment, but can only observe the output of a Turing machine.