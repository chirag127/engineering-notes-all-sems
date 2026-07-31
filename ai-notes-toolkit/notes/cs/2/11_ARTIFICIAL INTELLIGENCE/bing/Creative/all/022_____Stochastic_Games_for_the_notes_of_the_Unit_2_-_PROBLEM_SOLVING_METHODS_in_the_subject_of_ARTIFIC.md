# Stochastic Games

- Stochastic games are a generalization of Markov decision processes (MDPs) to the case where there are multiple agents in a common environment .
- The agents perform a joint action that defines both the reward obtained by the agents and the new state of the environment .
- The agents may have different objectives and preferences, and may act cooperatively or competitively .
- Stochastic games can model many artificial intelligence applications, such as playing chess and Go games, autonomous driving, and robotics .
- Stochastic games are also known as Markov games or matrix games .

## Formal Definition of Stochastic Games

- A stochastic game is defined by a tuple <S, A, T, R, γ>, where :
  - S is a finite set of states.
  - A is a finite set of actions, where A = A<sub>1</sub> x A<sub>2</sub> x ... x A<sub>n</sub>, and A<sub>i</sub> is the set of actions available to agent i.
  - T is a transition function, where T(s, a, s') is the probability of reaching state s' from state s after performing action a.
  - R is a reward function, where R<sub>i</sub>(s, a) is the immediate reward received by agent i in state s after performing action a.
  - γ is a discount factor, where 0 ≤ γ < 1.

## Types of Stochastic Games

- Depending on the information available to the agents and the nature of the game, stochastic games can be classified into different types :
  - Perfect-information vs. imperfect-information: In perfect-information games, the agents know the current state and the actions of the other agents. In imperfect-information games, the agents have only partial or noisy observations of the state and the actions of the other agents.
  - Zero-sum vs. non-zero-sum: In zero-sum games, the sum of the rewards of all the agents is zero, meaning that one agent's gain is another agent's loss. In non-zero-sum games, the sum of the rewards of all the agents can be positive or negative, meaning that the agents can have common or conflicting interests.
  - Cooperative vs. non-cooperative: In cooperative games, the agents can communicate and coordinate their actions to achieve a common goal. In non-cooperative games, the agents act independently and selfishly to maximize their own rewards.

## Solution Concepts for Stochastic Games

- A solution concept for a stochastic game is a way of defining the optimal behavior of the agents in the game .
- Some of the common solution concepts for stochastic games are:
  - Nash equilibrium: A Nash equilibrium is a joint strategy where no agent can improve its expected reward by deviating from its strategy, given that the other agents do not change their strategies .
  - Pareto optimality: A Pareto optimal outcome is a joint strategy where no agent can improve its expected reward without making another agent worse off .
  - Correlated equilibrium: A correlated equilibrium is a joint strategy where the agents follow a randomization device that assigns probabilities to each possible action, and no agent can improve its expected reward by deviating from the device, given that the other agents follow the device .

## Algorithms for Stochastic Games

- There are various algorithms for finding solutions for stochastic games, depending on the type and the size of the game .
- Some of the common algorithms for stochastic games are:
  - Value iteration: Value iteration is an iterative algorithm that computes the optimal value function and the optimal policy for each agent, by updating the value function based on the Bellman equation until convergence .
  - Policy iteration: Policy iteration is an iterative algorithm that computes the optimal value function and the optimal policy for each agent, by alternating between policy evaluation and policy improvement steps until convergence .
  - Linear programming: Linear programming is a mathematical technique that solves a system of linear inequalities to find the optimal value function and the optimal policy for each agent, by maximizing or minimizing a linear objective function subject to linear constraints [^5