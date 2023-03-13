The following is a detailed ascii diagram for basic properties of entropy for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing.

### Basic properties of Entropy

Entropy is a measure of uncertainty or disorder in a system. In quantum information theory, there are different types of entropy that can be used to quantify various aspects of quantum states, such as purity, correlations, information content, etc.

One of the most fundamental and widely used entropy measures is the von Neumann entropy, which is defined as:

```
S(rho) = -Tr(rho log rho)
```

where rho is a density matrix of a quantum system, Tr is the trace operator, and log is the logarithm base 2. The von Neumann entropy is a generalization of the classical Shannon entropy, which is defined as:

```
H(X) = -sum_x p(x) log p(x)
```

where X is a discrete random variable, and p(x) is the probability of observing x. The Shannon entropy measures the average amount of information needed to specify the outcome of X.

The von Neumann entropy has some basic properties that are similar to the Shannon entropy, such as:

- Non-negativity: S(rho) >= 0 for any rho, and S(rho) = 0 if and only if rho is a pure state (i.e., rho = |psi><psi| for some |psi>).
- Subadditivity: S(rho_AB) <= S(rho_A) + S(rho_B) for any bipartite system AB, where rho_AB is the joint state of A and B, and rho_A and rho_B are the reduced states of A and B, respectively. This means that the entropy of the whole system is less than or equal to the sum of the entropies of the subsystems.
- Strong subadditivity: S(rho_ABC) + S(rho_B) <= S(rho_AB) + S(rho_BC) for any tripartite system ABC, where rho_ABC is the joint state of A, B, and C, and rho_AB, rho_BC, and rho_B are the reduced states of AB, BC, and B, respectively. This means that the entropy of a subsystem cannot increase by adding another subsystem that is correlated with it.
- Concavity: S(sum_i p_i rho_i) >= sum_i p_i S(rho_i) for any convex combination of states rho_i with probabilities p_i. This means that the entropy of a mixture of states is greater than or equal to the weighted average of the entropies of the states.

The following diagram illustrates the basic properties of von Neumann entropy for a bipartite system AB:

```
  +-----------------+-----------------+
  |                 |                 |
  |                 |                 |
  |                 |                 |
  |       A         |        B        |
  |                 |                 |
  |                 |                 |
  |                 |                 |
  +-----------------+-----------------+
  |                 |                 |
  |                 |                 |
  |                 |                 |
  |       AB        |                 |
  |                 |                 |
  |                 |                 |
  |                 |                 |
  +-----------------+-----------------+

  S(rho_A) + S(rho_B) >= S(rho_AB)   (subadditivity)
```