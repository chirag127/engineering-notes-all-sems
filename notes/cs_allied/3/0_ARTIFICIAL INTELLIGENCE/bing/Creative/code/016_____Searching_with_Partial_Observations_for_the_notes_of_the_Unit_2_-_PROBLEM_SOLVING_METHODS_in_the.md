### Searching with Partial Observations

- When an environment is **partially observable**, an agent can be in one of **several possible states**    .
- An action leads to one of **several possible outcomes**   .
- To solve these problems, an agent maintains a **belief state** that represents the agent's current belief about the possible physical state it might be in   .
- A belief state is a **set of states** that are consistent with the agent's percepts and actions   .
- A percept is a **piece of information** that the agent receives from the environment .
- A percept can be **complete** or **partial**, depending on how much information it provides about the state  .
- A complete percept allows the agent to **determine** the state uniquely  .
- A partial percept leaves the agent with **uncertainty** about the state  .
- A search problem with partial observations can be defined as a **quintuple** (S, A, P, R, O)   , where:
  - S is a set of possible **states**   .
  - A is a set of possible **actions**   .
  - P is a **transition function** that maps a state and an action to a probability distribution over states   .
  - R is a **reward function** that maps a state and an action to a numerical reward   .
  - O is an **observation function** that maps a state and an action to a probability distribution over percepts   .
- A solution to a search problem with partial observations is a **policy** that maps a belief state to an action   .
- A policy can be **optimal** or **suboptimal**, depending on how well it maximizes the expected reward   .
- There are different **algorithms** for finding optimal or suboptimal policies, such as **belief state search**, **value iteration**, **policy iteration**, **Q-learning**, etc.   .
- Searching with partial observations is a **challenging** and **important** problem in artificial intelligence, as many real-world environments are partially observable   .