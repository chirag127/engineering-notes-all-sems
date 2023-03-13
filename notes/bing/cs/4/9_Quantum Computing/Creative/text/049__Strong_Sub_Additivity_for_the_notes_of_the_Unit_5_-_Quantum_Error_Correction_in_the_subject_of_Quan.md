### Strong Sub Additivity

- Strong sub additivity is a property of the von Neumann entropy that relates the entropy of a composite system to the entropy of its subsystems.
- Mathematically, it states that for any tripartite quantum state $\rho_{ABC}$, the following inequality holds:

$$
S(\rho_{ABC}) + S(\rho_B) \leq S(\rho_{AB}) + S(\rho_{BC})
$$

- Intuitively, this means that the entropy of a system cannot increase by adding a subsystem that is already correlated with it.
- Strong sub additivity is a useful tool for proving various results in quantum information theory, such as the Holevo bound, the quantum Fano inequality, and the quantum data processing inequality.
- Strong sub additivity can also be generalized to more than three subsystems, as follows:

$$
S(\rho_{A_1 \cdots A_n}) + S(\rho_{A_i}) \leq S(\rho_{A_1 \cdots A_{i-1}}) + S(\rho_{A_i \cdots A_n})
$$

- for any $i = 1, \ldots, n$ and any $n$-partite quantum state $\rho_{A_1 \cdots A_n}$.