### Strong Subadditivity

- Strong subadditivity (SSA) is a fundamental theorem in quantum information theory that relates the von Neumann entropies of different quantum subsystems of a larger quantum system.
- SSA states that for any tripartite quantum system ABC with density matrix $\rho_{ABC}$, the following inequality holds:

$$
S(\rho_{ABC}) + S(\rho_B) \leq S(\rho_{AB}) + S(\rho_{BC})
$$

where $S(\rho) = -\text{Tr}(\rho \log \rho)$ is the von Neumann entropy of a density matrix $\rho$, and $\rho_X$ denotes the reduced density matrix of subsystem X obtained by tracing out the other subsystems.

- SSA implies that the conditional mutual information $I(A:C|B) = S(\rho_{AB}) + S(\rho_{BC}) - S(\rho_{ABC}) - S(\rho_B)$ is always non-negative, which means that the correlations between A and C cannot increase by conditioning on B.
- SSA also implies the weak subadditivity (WSA) of quantum entropy, which states that for any bipartite quantum system AB with density matrix $\rho_{AB}$, the following inequality holds:

$$
S(\rho_{AB}) \leq S(\rho_A) + S(\rho_B)
$$

where $\rho_A$ and $\rho_B$ are the reduced density matrices of subsystems A and B, respectively. WSA implies that the mutual information $I(A:B) = S(\rho_A) + S(\rho_B) - S(\rho_{AB})$ is always non-negative, which means that the total correlations between A and B are bounded by the individual entropies of A and B.

- SSA has many applications in quantum information theory, such as quantum data processing, quantum channel capacity, quantum entanglement, quantum error correction, and quantum cryptography. SSA is also related to other important inequalities in quantum information theory, such as the Wigner-Yanase-Dyson conjecture, the monotonicity of quantum relative entropy, and the joint convexity of quantum relative entropy.
- SSA was conjectured by Robinson and Ruelle in 1966 and Lanford and Robinson in 1968, and proved by Lieb and Ruskai in 1973 using the concavity of the Wigner-Yanase-Dyson skew information. There are also other proofs of SSA based on different techniques, such as the Petz recovery map, the operator monotone functions, and the quantum de Finetti theorem.