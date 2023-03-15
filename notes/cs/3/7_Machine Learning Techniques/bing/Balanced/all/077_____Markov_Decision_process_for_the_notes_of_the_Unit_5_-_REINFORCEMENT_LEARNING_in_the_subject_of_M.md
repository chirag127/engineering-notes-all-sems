# Markov Decision Process

A Markov decision process (MDP) is a mathematical framework for modeling decision-making problems where the outcomes are partly random and partly controllable by an agent. It is a framework that can address most reinforcement learning (RL) problems .

## Components of an MDP

An MDP is characterized by four components  :

- A set of states **S** that the agent can be in. A state is a complete description of the situation that the agent faces. For example, in a chess game, a state would be the configuration of the board and the turn of the player.
- A set of actions **A** that the agent can take in each state. An action is a choice that the agent makes to influence the outcome. For example, in a chess game, an action would be a move of a piece.
- A transition function **T** that specifies the probability of reaching a new state **s'** given the current state **s** and the action **a**. This function captures the dynamics of the environment and the uncertainty of the outcomes. For example, in a chess game, the transition function would depend on the rules of the game and the opponent's strategy.
- A reward function **R** that specifies the immediate reward that the agent receives after taking an action **a** in state **s** and reaching a new state **s'**. This function captures the goal of the agent and the feedback from the environment. For example, in a chess game, the reward function could be +1 for winning, -1 for losing, and 0 for other outcomes.

## Objective of an MDP

The objective of an MDP is to find a policy **π** that specifies the best action to take in each state to maximize the expected return  . The return is the total discounted reward that the agent accumulates over time, where the discount factor **γ** is a number between 0 and 1 that determines how much the agent values future rewards compared to immediate rewards. For example, in a chess game, the return would be the sum of the rewards from each move, discounted by a factor that reflects how much the agent cares about winning sooner rather than later.

## Solution methods for an MDP

There are two main classes of algorithms for computing optimal policies for an MDP: dynamic programming and reinforcement learning   .

- Dynamic programming algorithms assume that the agent knows the transition and reward functions of the MDP, and use them to iteratively update the value function and the policy until they converge to the optimal ones. The value function is a function that assigns a value to each state, representing the expected return from following the policy from that state. For example, the value iteration algorithm updates the value function by applying the Bellman optimality equation, which states that the value of a state is equal to the maximum expected value of taking an action and transitioning to a new state, plus the reward from doing so.
- Reinforcement learning algorithms do not assume that the agent knows the transition and reward functions of the MDP, and instead learn them from experience by interacting with the environment and observing the outcomes. The agent uses a trial-and-error approach to improve its policy based on the feedback from the environment. For example, the Q-learning algorithm updates the Q-function, which is a function that assigns a value to each state-action pair, representing the expected return from taking that action in that state and following the policy thereafter. The Q-function is updated by applying the temporal difference learning rule, which states that the Q-value of a state-action pair is updated by the difference between the observed reward and the next Q-value, multiplied by a learning rate.