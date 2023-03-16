# Basic properties of Entropy for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Entropy is a measure of the intrinsic dispersion, uncertainty, or lack of information of a quantum state.
- Entropy is also a measurable quantity that is related to the thermodynamics and statistical mechanics of a quantum system.
- The most common entropy measure for quantum states is the von Neumann entropy, which is defined as:

$$
S(\rho) = -\text{Tr}(\rho \log \rho)
$$

where $\rho$ is the density matrix of the quantum state, and $\log$ is the logarithm base 2.

- The von Neumann entropy satisfies the following basic properties:

  - Non-negativity: $S(\rho) \geq 0$ for any $\rho$.
  - Additivity: $S(\rho \otimes \sigma) = S(\rho) + S(\sigma)$ for any $\rho$ and $\sigma$.
  - Subadditivity: $S(\rho_{AB}) \leq S(\rho_A) + S(\rho_B)$ for any $\rho_{AB}$ and its reduced states $\rho_A$ and $\rho_B$.
  - Strong subadditivity: $S(\rho_{ABC}) + S(\rho_B) \leq S(\rho_{AB}) + S(\rho_{BC})$ for any $\rho_{ABC}$ and its reduced states $\rho_B$, $\rho_{AB}$, and $\rho_{BC}$.
  - Concavity: $S(\sum_i p_i \rho_i) \geq \sum_i p_i S(\rho_i)$ for any $\rho_i$ and $p_i$.
  - Continuity: $S(\rho)$ is a continuous function of $\rho$.

- The von Neumann entropy can be interpreted as the optimal compression rate for quantum information, or the minimum number of qubits needed to store a quantum state asymptotically.
- The von Neumann entropy can also be used to quantify the entanglement of a quantum state, or the amount of quantum correlations between two or more subsystems.
- The von Neumann entropy is not the only entropy measure for quantum states. There are other entropies, such as the Renyi entropy, the Tsallis entropy, the min-entropy, the max-entropy, and the conditional entropy, that have different properties and applications .
- The conditional entropy of a quantum state is defined as:

$$
S(A|B) = S(\rho_{AB}) - S(\rho_B)
$$

where $\rho_{AB}$ is the joint state of subsystems $A$ and $B$, and $\rho_B$ is the reduced state of subsystem $B$.

- The conditional entropy can be negative, unlike the classical case, which reflects the presence of quantum entanglement.
- The conditional entropy can be used to quantify the quantum discord, the quantum mutual information, the quantum coherence, and the quantum conditional mutual information of a quantum state.
- The conditional entropy is a non-linear and non-convex function of the quantum state, which makes its computation and optimization challenging.