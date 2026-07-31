### Strong Subadditivity

- Strong subadditivity (SSA) is a fundamental property of the von Neumann entropy of quantum systems .
- SSA states that for any tripartite quantum state $\rho_{ABC}$, the following inequality holds:

$$
S(\rho_{ABC}) + S(\rho_B) \leq S(\rho_{AB}) + S(\rho_{BC})
$$

- Here, $S(\rho) = -\mathrm{Tr}(\rho \log \rho)$ is the von Neumann entropy of a quantum state $\rho$, and $\rho_{XY}$ denotes the reduced state of $\rho_{ABC}$ on the subsystems $X$ and $Y$.
- SSA implies that the mutual information $I(A:B) = S(\rho_A) + S(\rho_B) - S(\rho_{AB})$ is non-negative and monotonically non-increasing under local operations and classical communication (LOCC) .
- SSA also implies that the conditional entropy $S(A|B) = S(\rho_{AB}) - S(\rho_B)$ can be negative, indicating the presence of quantum correlations or entanglement .
- SSA has many applications in quantum information theory, such as quantum error correction, quantum cryptography, quantum thermodynamics, quantum channel capacity, and quantum entanglement theory .
- SSA can be proved using various methods, such as the monotonicity of the relative entropy, the Petz recovery map, the operator logarithmic Sobolev inequality, and the quantum de Finetti theorem .