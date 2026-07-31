# Markov Chains

- A Markov chain is a type of Markov process that has either a discrete state space or a discrete index set (often representing time), but the precise definition of a Markov chain varies.
- A Markov chain is a mathematical system that experiences transitions from one state to another according to certain probabilistic rules.
- The defining characteristic of a Markov chain is that no matter how the process arrived at its present state, the possible future states are fixed. This property is called the **Markov property** or **memorylessness**.
- A Markov chain can be represented by a **transition matrix** that specifies the probability of moving from one state to another . The transition matrix is usually denoted by **P** and has the following properties:
  - The entries of P are non-negative, i.e., P[i][j] >= 0 for all i and j.
  - The sum of each row of P is 1, i.e., sum(P[i]) = 1 for all i. This means that the probabilities of all possible transitions from a given state must add up to 1.
- A Markov chain can also be represented by a **directed graph** where the nodes are the states and the edges are labeled with the transition probabilities. The graph is called a **state diagram** or a **Markov diagram**.
- A Markov chain can be used to model various stochastic processes, such as weather patterns, text generation, finance modeling, cruise control systems, etc  .
- A Markov chain can have different types of states, such as **absorbing states**, **recurrent states**, **transient states**, **ergodic states**, etc., depending on the behavior of the transitions .
- A Markov chain can have different types of properties, such as **stationarity**, **periodicity**, **irreducibility**, **reversibility**, etc., depending on the structure of the transition matrix .
- A Markov chain can be analyzed using various methods, such as **matrix algebra**, **Markov chain Monte Carlo**, **Perron-Frobenius theorem**, **Chapman-Kolmogorov equation**, etc .