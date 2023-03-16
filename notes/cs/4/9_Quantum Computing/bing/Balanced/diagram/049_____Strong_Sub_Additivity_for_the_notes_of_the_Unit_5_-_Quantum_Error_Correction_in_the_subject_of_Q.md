### Strong Subadditivity

- Strong subadditivity (SSA) is a fundamental property of quantum entropy that relates the von Neumann entropies of different subsystems of a tripartite quantum state .
- SSA states that for any tripartite quantum state $\rho_{ABC}$, the following inequality holds:

$$
S(\rho_{AB}) + S(\rho_{BC}) \leq S(\rho_{ABC}) + S(\rho_B)
$$

where $S(\rho) = -\mathrm{Tr}(\rho \log \rho)$ is the von Neumann entropy of a quantum state $\rho$.

- SSA implies that the mutual information between two subsystems cannot increase by adding a third subsystem . That is,

$$
I(A:B) \geq I(A:BC)
$$

where $I(A:B) = S(\rho_A) + S(\rho_B) - S(\rho_{AB})$ is the mutual information between subsystems $A$ and $B$.

- SSA has many applications in quantum information theory, such as quantum error correction, quantum cryptography, quantum entanglement, quantum thermodynamics, and quantum complexity theory  .
- SSA can be proved using various methods, such as the Petz recovery map, the monotonicity of relative entropy, the quantum data processing inequality, and the quantum conditional mutual information .