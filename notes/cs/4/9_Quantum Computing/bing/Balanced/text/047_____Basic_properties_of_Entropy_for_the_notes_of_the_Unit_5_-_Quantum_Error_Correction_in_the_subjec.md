### Basic properties of Entropy for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Entropy is a measure of the intrinsic dispersion, uncertainty, or lack of information of a quantum state.
- Entropy is also a measurable quantity that is related to the thermodynamic properties of a quantum system.
- The most common entropy measure for quantum states is the von Neumann entropy, which is defined as
$$
S(\rho) = -\mathrm{Tr}(\rho \log \rho)
$$
where $\rho$ is the density matrix of the quantum state and $\log$ is the logarithm base 2.
- The von Neumann entropy satisfies some basic properties, such as
  - Non-negativity: $S(\rho) \geq 0$ for any $\rho$.
  - Additivity: $S(\rho \otimes \sigma) = S(\rho) + S(\sigma)$ for any $\rho$ and $\sigma$.
  - Subadditivity: $S(\rho_{AB}) \leq S(\rho_A) + S(\rho_B)$ for any $\rho_{AB}$ and its reduced states $\rho_A$ and $\rho_B$.
  - Strong subadditivity: $S(\rho_{ABC}) + S(\rho_B) \leq S(\rho_{AB}) + S(\rho_{BC})$ for any $\rho_{ABC}$ and its reduced states $\rho_B$, $\rho_{AB}$ and $\rho_{BC}$.
- The von Neumann entropy can be used to quantify the quantum correlations and entanglement between subsystems of a quantum state.
- The von Neumann entropy can also be used to address the issue of redundancy and compression in quantum information theory.
- The von Neumann entropy is not the only entropy measure for quantum states. There are other entropies, such as the Renyi entropy, the Tsallis entropy, the min-entropy, and the max-entropy, that have different properties and applications.
- The entropy of a quantum state can depend on the algebra of observables that are accessible to the observer. Different algebras can lead to different density matrices and different entropies for the same state.
- The entropy of a quantum state can also depend on the interaction with the environment. Some quantum systems, such as the Entropy Quantum Computing (EQC) systems, use controlled feedback from the environment to drive the quantum information results.