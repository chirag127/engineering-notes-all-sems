### Markov chains for the notes of the Unit 3 - Pseudo-Random Numbers in the subject of MATHEMATICAL FOUNDATION AI , ML AND DATA SCIENCE

- A Markov chain is a type of Markov process that has either a discrete state space or a discrete index set (often representing time), but the precise definition of a Markov chain varies.
- A Markov chain is a mathematical system that experiences transitions from one state to another according to certain probabilistic rules.
- The defining characteristic of a Markov chain is that no matter how the process arrived at its present state, the possible future states are fixed. This property is called the **Markov property** or **memorylessness**.
- A Markov chain can be represented by a **transition matrix** that specifies the probability of moving from one state to another . The transition matrix is usually denoted by **P** and has the following properties:
  - The entries of P are non-negative, i.e., P[i][j] >= 0 for all i and j.
  - The sum of each row of P is 1, i.e., sum(P[i]) = 1 for all i. This means that the probabilities of all possible transitions from a given state must add up to 1.
  - The size of P is equal to the number of states in the Markov chain, i.e., P is a n x n matrix, where n is the number of states.
- A Markov chain can also be represented by a **directed graph** (as opposed to our usual directed acyclic graph), where the nodes are the states and the edges are labeled with the probabilities of going from one state to another.
- A Markov chain can be used to model various phenomena that involve random or stochastic processes, such as weather, genetics, text generation, finance, etc  .
- A Markov chain can have different types of states, such as **transient**, **recurrent**, **absorbing**, **ergodic**, etc., depending on the behavior of the transitions and the long-term probabilities of the states.
- A Markov chain can have different types of **stationary distributions**, which are the probability distributions of the states in the long run, i.e., as the number of transitions approaches infinity. A stationary distribution is also called a **steady-state distribution** or an **equilibrium distribution**.
- A Markov chain can have different types of **convergence properties**, which describe how the probability distribution of the states changes over time, i.e., as the number of transitions increases. For example, a Markov chain can be **irreducible**, **aperiodic**, **positive recurrent**, **reversible**, etc., which imply different types of convergence to a unique stationary distribution.