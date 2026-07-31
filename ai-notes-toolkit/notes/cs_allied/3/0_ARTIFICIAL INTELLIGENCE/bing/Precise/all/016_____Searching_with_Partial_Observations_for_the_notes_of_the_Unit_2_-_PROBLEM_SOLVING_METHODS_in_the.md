# Searching with Partial Observations

- When an environment is partially observable, an agent can be in one of several possible states. An action leads to one of several possible outcomes.
- To solve these problems, an agent maintains a belief state that represents the agent's current belief about the possible physical state it might be in.
- The environment generates percepts, for example, a vacuum agent has a position and a local dirt sensor but no dirt sensor for other squares.
- Many problems cannot be solved without sensing. For example, the sensorless 8-puzzle is impossible. On the other hand, a little bit of sensing can go a long way: we can solve 8-puzzles if we can see just the upper-left corner square.
- Suppose an agent can sense the environment: it can tell whether a room is dirty or not (but only the room where it is, not the next one). Percept(s) returns a percept for the given state, for example [A,Dirty] (if s is the state when the agent is in room A and it is dirty). Transitions are now 3-step.
