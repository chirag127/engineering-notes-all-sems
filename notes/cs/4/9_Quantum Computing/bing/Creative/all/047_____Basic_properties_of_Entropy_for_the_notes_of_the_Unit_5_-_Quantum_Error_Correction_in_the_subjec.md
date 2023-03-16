# Basic properties of Entropy for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Entropy is a measure of the uncertainty or disorder of a quantum system. It quantifies how much information is missing or hidden in a quantum state.
- The most common entropy measure in quantum information theory is the von Neumann entropy, which is defined as:

$$
S(\rho) = -\text{Tr}(\rho \log \rho)
$$

where $\rho$ is the density matrix of the quantum system, and $\text{Tr}$ denotes the trace operation. The von Neumann entropy is a generalization of the Shannon entropy for classical probability distributions.
- The von Neumann entropy satisfies some basic properties, such as:

  - Non-negativity: $S(\rho) \geq 0$ for any $\rho$, and $S(\rho) = 0$ if and only if $\rho$ is a pure state.
  - Subadditivity: $S(\rho_{AB}) \leq S(\rho_A) + S(\rho_B)$ for any bipartite system $AB$, where $\rho_{AB}$ is the joint state and $\rho_A$ and $\rho_B$ are the reduced states. This means that the entropy of the whole system is less than or equal to the sum of the entropies of the subsystems.
  - Strong subadditivity: $S(\rho_{ABC}) + S(\rho_B) \leq S(\rho_{AB}) + S(\rho_{BC})$ for any tripartite system $ABC$. This means that the entropy of a subsystem cannot increase by adding another subsystem that is correlated with it.
  - Concavity: $S(\sum_i p_i \rho_i) \geq \sum_i p_i S(\rho_i)$ for any convex combination of states $\rho_i$ with probabilities $p_i$. This means that the entropy of a mixture of states is greater than or equal to the average entropy of the states.
  - Continuity: $S(\rho)$ is a continuous function of $\rho$ in the trace norm. This means that small changes in the state lead to small changes in the entropy.

- The von Neumann entropy can be used to quantify various aspects of quantum information, such as:

  - Quantum data compression: The von Neumann entropy gives the optimal rate at which quantum information can be compressed without losing information. The quantum source coding theorem states that $n$ copies of a quantum state $\rho$ can be compressed to $nS(\rho)$ qubits asymptotically.
  - Quantum entanglement: The von Neumann entropy can be used to measure the amount of entanglement between two quantum systems. The entanglement entropy is defined as the entropy of one subsystem after tracing out the other subsystem. For pure states, the entanglement entropy is equal to the entropy of either subsystem, and it is zero for separable states. For mixed states, the entanglement entropy is not unique, and there are other measures of entanglement, such as the relative entropy of entanglement, the entanglement of formation, and the entanglement of distillation.
  - Quantum thermodynamics: The von Neumann entropy can be used to describe the thermodynamic properties of quantum systems, such as the internal energy, the free energy, and the heat capacity. The second law of thermodynamics states that the entropy of a closed system cannot decrease, and the entropy of the universe tends to increase. This implies that quantum systems tend to evolve towards equilibrium states that maximize the entropy.
  - Quantum correlations: The von Neumann entropy can be used to quantify the amount of correlation or dependence between two quantum systems. The mutual information is defined as the difference between the entropy of the joint system and the sum of the entropies of the subsystems. The mutual information is zero for uncorrelated systems, and it is positive for correlated systems. The mutual information can be further decomposed into the classical and quantum parts, which measure the amount of correlation that can be accessed by local measurements and the amount of correlation that is purely quantum, respectively.