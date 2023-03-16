### Searching with Partial Observations

- In a partially observable environment, an agent cannot directly perceive the complete state of the world, but only some aspects of it.
- For example, a vacuum agent may only have a position sensor and a local dirt sensor, but not a global dirt sensor for the entire floor.
- To cope with partial observability, an agent needs to maintain a belief state, which is a set of possible states that are consistent with the agent's observations and actions.
- A belief state can be represented as a probability distribution over the possible states, or as a logical formula that captures the constraints on the states.
- Searching with partial observations requires expanding belief states rather than single states, and applying actions to belief states rather than single states.
- The result of applying an action to a belief state is a new belief state that incorporates the effects of the action and the new observation.
- The goal of searching with partial observations is to find a sequence of actions that leads to a belief state that satisfies the goal condition, or that maximizes the expected utility of the agent.
- Searching with partial observations is more complex than searching with full observability, because the size of the belief state can grow exponentially with the number of actions and observations, and because the agent may need to explore different branches of the search tree to gather more information.
- Some techniques for searching with partial observations are:

  - AND-OR search: a search tree that alternates between AND nodes, which represent belief states, and OR nodes, which represent actions. The agent chooses an action at an OR node, and then considers all possible outcomes at the next AND node. The search is complete when an AND node contains only goal states, or when the expected utility of the belief state is maximized.
  - Kripke structures: a graph-based representation of the possible states and transitions of a partially observable environment, where each node is a possible state, and each edge is labeled with an action and an observation. The agent can use model checking techniques to verify whether a formula is true in a Kripke structure, or to find a path that satisfies a formula.
  - POMDPs: a mathematical framework for modeling partially observable environments, where each state has a reward and a transition function, and each action has an observation function. The agent can use value iteration or policy iteration techniques to find an optimal policy that maps belief states to actions, or to approximate the optimal policy using point-based methods or Monte Carlo methods.