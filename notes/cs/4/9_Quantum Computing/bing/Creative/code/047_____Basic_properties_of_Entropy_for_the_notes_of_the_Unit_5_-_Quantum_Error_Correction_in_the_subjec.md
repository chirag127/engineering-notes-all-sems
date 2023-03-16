# Basic properties of Entropy for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Entropy is a measure of the intrinsic dispersion, uncertainty, or lack of information of a quantum state.
- Entropy is also related to the amount of chaos or disorder in a quantum system.
- Entropy is a measurable quantity, at least in equilibrium, and it has units of bits or nats.
- The most common entropy measure in quantum mechanics is the von Neumann entropy, which is defined as:

$$
S(\rho) = -\text{Tr}(\rho \log \rho)
$$

where $\rho$ is the density matrix of the quantum state, and $\log$ is the logarithm base 2 or $e$  .

- The von Neumann entropy satisfies some basic properties, such as:

  - Non-negativity: $S(\rho) \geq 0$ for any $\rho$, and $S(\rho) = 0$ if and only if $\rho$ is a pure state  .
  - Concavity: $S(\sum_i p_i \rho_i) \geq \sum_i p_i S(\rho_i)$ for any convex combination of density matrices $\rho_i$ and probabilities $p_i$  .
  - Subadditivity: $S(\rho_{AB}) \leq S(\rho_A) + S(\rho_B)$ for any bipartite system $AB$ and its reduced density matrices $\rho_A$ and $\rho_B$  .
  - Strong subadditivity: $S(\rho_{ABC}) + S(\rho_B) \leq S(\rho_{AB}) + S(\rho_{BC})$ for any tripartite system $ABC$ and its reduced density matrices  .

- The von Neumann entropy can be interpreted as the average amount of information needed to specify the quantum state, or the optimal compression rate of quantum data.
- The von Neumann entropy can also be related to the thermodynamic entropy of a quantum system, and it satisfies the second law of thermodynamics, which states that the entropy of a closed system cannot decrease over time.
- Another important entropy measure in quantum mechanics is the conditional entropy, which is defined as:

$$
S(A|B) = S(\rho_{AB}) - S(\rho_B)
$$

where $\rho_{AB}$ and $\rho_B$ are the density matrices of a bipartite system $AB$ and its subsystem $B$, respectively.

- The conditional entropy measures the amount of information about subsystem $A$ that is not contained in subsystem $B$.
- The conditional entropy can be negative, which indicates the presence of quantum correlations or entanglement between $A$ and $B$.
- The conditional entropy can be used to quantify the quantum discord, which is a measure of the quantumness of correlations in a mixed state.