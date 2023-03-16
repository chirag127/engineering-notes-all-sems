# Strong Subadditivity for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Strong subadditivity (SSA) of quantum entropy is a fundamental property of quantum information theory that relates the von Neumann entropies of different subsystems of a larger quantum system .
- SSA states that for any tripartite quantum state $\rho_{ABC}$, the following inequality holds:

$$
S(\rho_{AB}) + S(\rho_{BC}) \leq S(\rho_{ABC}) + S(\rho_B)
$$

where $S(\rho) = -\text{Tr}(\rho \log \rho)$ is the von Neumann entropy of a quantum state $\rho$.

- SSA implies that the mutual information between two subsystems cannot increase by adding a third subsystem, i.e.,

$$
I(A:B) \geq I(A:BC)
$$

where $I(A:B) = S(\rho_A) + S(\rho_B) - S(\rho_{AB})$ is the quantum mutual information between subsystems $A$ and $B$.

- SSA also implies that the conditional entropy of a quantum state cannot be negative, i.e.,

$$
S(A|B) \leq 0
$$

where $S(A|B) = S(\rho_{AB}) - S(\rho_B)$ is the quantum conditional entropy of subsystem $A$ given subsystem $B$.

- SSA has many applications in quantum information theory, such as proving the Holevo bound, the quantum Fano inequality, the quantum data processing inequality, the quantum strong converse theorem, and the quantum reverse Shannon theorem .
- SSA can be proved using various methods, such as the Petz recovery map, the monotonicity of relative entropy, the Lieb concavity theorem, and the operator convexity of the logarithm.