# Stochastic Games

- Stochastic games are a generalization of Markov decision processes (MDPs) to the case where there are multiple agents in a common environment .
- The agents perform a joint action that defines both the reward obtained by the agents and the new state of the environment .
- The agents may have different objectives and preferences, and may act cooperatively or competitively .
- Stochastic games can model many artificial intelligence applications, such as playing chess and Go, autonomous driving, and robotics .
- Stochastic games are also known as Markov games or matrix games .

## Formal Definition of Stochastic Games

- A stochastic game is defined by a tuple <S, A, T, R, γ>, where :
  - S is a finite set of states.
  - A is a finite set of actions, which can be decomposed into A = A1 x A2 x ... x An, where Ai is the set of actions available to agent i.
  - T is a transition function, which maps S x A x S to [0, 1], and specifies the probability of reaching state s' from state s by taking action a, i.e., T(s, a, s') = P(s'|s, a).
  - R is a reward function, which maps S x A to R^n, and specifies the reward received by each agent for taking action a in state s, i.e., R(s, a) = (r1(s, a), r2(s, a), ..., rn(s, a)).
  - γ is a discount factor, which is a real number in [0, 1], and represents the relative importance of future rewards versus immediate rewards.

## Solution Concepts for Stochastic Games

- A solution concept for a stochastic game is a way of defining what constitutes an optimal or rational behavior for each agent in the game .
- There are different solution concepts depending on the assumptions and goals of the agents, such as:
  - Nash equilibrium: a joint strategy where no agent can improve its expected payoff by deviating unilaterally, assuming the other agents keep their strategies fixed .
  - Pareto optimality: a joint strategy where no agent can improve its expected payoff without making another agent worse off .
  - Social welfare: a joint strategy that maximizes the sum of the expected payoffs of all agents .
  - Cooperative game theory: a framework that allows agents to form coalitions and share the rewards according to some rules or agreements .

## Algorithms for Stochastic Games

- There are various algorithms for finding or approximating the solution concepts for stochastic games, such as  :
  - Value iteration: a dynamic programming algorithm that iteratively updates the value function for each state and action until convergence .
  - Policy iteration: a dynamic programming algorithm that iteratively evaluates and improves a policy for each agent until convergence .
  - Linear programming: a mathematical optimization technique that solves a system of linear equations and inequalities to find the optimal value function or policy .
  - Reinforcement learning: a learning technique that allows agents to learn from their own experience and feedback, without requiring a model of the environment or the reward function .
  - Descent framework: a learning and planning technique that combines Monte Carlo tree search and deep neural networks to learn and improve a policy for each agent in stochastic games.