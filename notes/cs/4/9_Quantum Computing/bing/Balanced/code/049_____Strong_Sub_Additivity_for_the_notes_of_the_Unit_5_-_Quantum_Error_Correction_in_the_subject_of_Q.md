### Strong Subadditivity for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Strong subadditivity (SSA) of quantum entropy is a fundamental theorem in quantum information theory that relates the von Neumann entropies of different quantum subsystems of a larger quantum system .
- The von Neumann entropy of a quantum system is defined as $S(\rho) = -\text{Tr}(\rho \log \rho)$, where $\rho$ is the density matrix of the system and $\text{Tr}$ is the trace operator.
- SSA states that for any tripartite quantum system $\rho_{ABC}$, the following inequality holds:

$$
S(\rho_{AB}) + S(\rho_{BC}) \leq S(\rho_{ABC}) + S(\rho_B)
$$

- This inequality implies that the mutual information between two quantum systems cannot increase by adding a third system, or equivalently, that the conditional entropy of a quantum system given another system cannot be negative .
- SSA has many applications in quantum information theory, such as bounding the capacity of quantum channels, proving the security of quantum cryptography, and characterizing the entanglement properties of quantum states .
- SSA can be proved using various methods, such as the monotonicity of relative entropy, the operator convexity of the logarithm function, or the Petz recovery map.