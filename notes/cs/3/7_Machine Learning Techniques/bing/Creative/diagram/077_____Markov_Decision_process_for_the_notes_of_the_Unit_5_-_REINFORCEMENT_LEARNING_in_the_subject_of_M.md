### Markov Decision Process

A Markov decision process (MDP) is a mathematical model for sequential decision making under uncertainty. It consists of four components:

- A set of states, denoted by **S**, that describe the possible situations of the system. For example, in a chess game, a state could be the configuration of the board and the player to move.
- A set of actions, denoted by **A**, that the decision maker can choose from in each state. For example, in a chess game, an action could be a legal move of a piece.
- A transition function, denoted by **T**, that specifies the probability of moving from one state to another given an action. For example, in a chess game, the transition function could depend on the rules of the game and the opponent's strategy.
- A reward function, denoted by **R**, that assigns a numerical value to each state or state-action pair. For example, in a chess game, the reward function could be the score of the board or the outcome of the game.

The goal of an MDP is to find a policy, denoted by **π**, that maps each state to an action that maximizes the expected return, denoted by **G**, which is the sum of discounted rewards over time. For example, in a chess game, the goal is to find a policy that wins the game or minimizes the loss.

There are different methods to solve an MDP, such as value iteration, policy iteration, and Q-learning. These methods rely on the Bellman equation, which relates the value of a state or a state-action pair to the value of its successor states or state-action pairs. The Bellman equation can be written as:

- For state values: **V(s) = max_a R(s,a) + γ Σ_s' T(s,a,s') V(s')**, where **γ** is the discount factor that controls the importance of future rewards.
- For state-action values: **Q(s,a) = R(s,a) + γ Σ_s' T(s,a,s') max_a' Q(s',a')**, where **Q(s,a)** is the expected return of taking action **a** in state **s** and following the optimal policy thereafter.

An MDP is a general framework that can be applied to many reinforcement learning problems, where the agent learns from its own experience and interacts with the environment. Some examples of MDPs are:

- Gridworld: The agent moves in a grid of cells, where some cells have rewards or penalties, and the goal is to reach a terminal state with the highest reward.
- Blackjack: The agent plays a simplified version of blackjack against a dealer, where the state is the sum of the agent's cards and the dealer's showing card, and the actions are to hit or stand.
- Inventory control: The agent manages the inventory of a store, where the state is the current inventory level, the actions are to order or not order new items, and the rewards are the profits or losses from selling or storing items.