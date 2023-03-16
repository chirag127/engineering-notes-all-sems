# Strong Subadditivity

- Strong subadditivity (SSA) is a fundamental property of quantum entropy that relates the von Neumann entropies of different subsystems of a tripartite quantum state .
- SSA states that for any tripartite quantum state $\rho_{ABC}$, the following inequality holds:

$$
S(\rho_{AB}) + S(\rho_{BC}) \leq S(\rho_{A}) + S(\rho_{ABC})
$$

where $S(\rho) = -\text{Tr}(\rho \log \rho)$ is the von Neumann entropy of a quantum state $\rho$.

- SSA implies that the mutual information between two subsystems cannot increase by adding a third subsystem, i.e.,

$$
I(A:B) \geq I(A:BC)
$$

where $I(A:B) = S(\rho_A) + S(\rho_B) - S(\rho_{AB})$ is the quantum mutual information between subsystems $A$ and $B$.

- SSA has many applications in quantum information theory, such as bounding the capacity of quantum channels, proving the Holevo bound on accessible information, and deriving the quantum Fannes-Audenaert inequality.