### Markov Decision Process

A Markov decision process (MDP) is a mathematical framework for modeling decision-making problems where the outcomes are partly random and partly controllable by an agent. It is a framework that can address most reinforcement learning (RL) problems .

An MDP consists of four components :

- A set of states **S** that the agent can be in. For example, the location of a robot in a grid world.
- A set of actions **A** that the agent can take in each state. For example, moving up, down, left, or right in the grid world.
- A transition function **T(s, a, s')** that specifies the probability of reaching state **s'** from state **s** by taking action **a**. For example, the probability of moving to the right cell from the current cell by taking the right action.
- A reward function **R(s, a, s')** that specifies the immediate reward received by the agent for taking action **a** in state **s** and reaching state **s'**. For example, the reward for reaching the goal cell in the grid world.

The goal of the agent is to find a policy **π(s)** that specifies the best action to take in each state **s** to maximize the expected return, which is the discounted sum of future rewards . The return at time step **t** is defined as:

**G_t = R_t+1 + γR_t+2 + γ^2R_t+3 + ... = ∑_k=0^∞ γ^kR_t+k+1**

where **γ** is the discount factor that determines how much the agent values immediate rewards over future rewards. The discount factor is usually between 0 and 1 .

The value of a state **s** under a policy **π** is the expected return starting from state **s** and following policy **π** thereafter . It is denoted by **V_π(s)** and defined as:

**V_π(s) = E_π[G_t | S_t = s] = E_π[∑_k=0^∞ γ^kR_t+k+1 | S_t = s]**

The value of taking action **a** in state **s** under a policy **π** is the expected return starting from state **s**, taking action **a**, and following policy **π** thereafter . It is denoted by **Q_π(s, a)** and defined as:

**Q_π(s, a) = E_π[G_t | S_t = s, A_t = a] = E_π[∑_k=0^∞ γ^kR_t+k+1 | S_t = s, A_t = a]**

The optimal policy **π*** is the policy that maximizes the value for all states . It is defined as:

**π*(s) = argmax_a Q_π*(s, a)**

The optimal state-value function **V_π*(s)** is the value of a state **s** under the optimal policy . It is defined as:

**V_π*(s) = max_a Q_π*(s, a)**

The optimal action-value function **Q_π*(s, a)** is the value of taking action **a** in state **s** under the optimal policy . It is defined as:

**Q_π*(s, a) = E_π*[G_t | S_t = s, A_t = a]**

The Bellman equation expresses the relationship between the value of a state and the values of its successor states . It can be written as:

**V_π(s) = ∑_a π(a | s) ∑_s' T(s, a, s') [R(s, a, s') + γV_π(s')]**

The Bellman optimality equation expresses the relationship between the optimal value of a state and the optimal values of its successor states . It can be written as:

**V_π*(s) = max_a ∑_s' T(s, a