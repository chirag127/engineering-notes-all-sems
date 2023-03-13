### Strong Subadditivity for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Strong subadditivity (SSA) is a fundamental property of quantum entropy that relates the von Neumann entropies of different subsystems of a larger quantum system .
- SSA states that for any tripartite quantum state $\rho_{ABC}$, the following inequality holds:

$$
S(\rho_{AB}) + S(\rho_{BC}) \geq S(\rho_{B}) + S(\rho_{ABC})
$$

where $S(\rho) = -\text{Tr}(\rho \log \rho)$ is the von Neumann entropy of a quantum state $\rho$.

- SSA can be interpreted as saying that the entropy of a subsystem $B$ cannot increase by adding or removing another subsystem $A$ or $C$.
- SSA can also be written in terms of the conditional entropy $S(A|B) = S(AB) - S(B)$ and the mutual information $I(A:B) = S(A) + S(B) - S(AB)$ as follows:

$$
S(A|BC) \leq S(A|B)
$$

$$
I(A:B|C) \geq 0
$$

- SSA has many applications in quantum information theory, such as proving the Holevo bound, the quantum Fano inequality, the quantum data processing inequality, the quantum strong converse, the quantum state merging protocol, the quantum reverse Shannon theorem, and the quantum conditional mutual information inequality.
- A simple mnemonic to remember SSA is to think of the entropy as a measure of uncertainty or ignorance. SSA then says that adding or removing information (subsystems) cannot increase the uncertainty or ignorance of another subsystem.
- A simple proof of SSA is based on the operator monotonicity of the logarithm function and the joint convexity of the von Neumann entropy. The proof goes as follows:

  - Let $P$ be the projector onto the support of $\rho_{ABC}$ and let $Q = I - P$ be the orthogonal complement. Then we have:

  $$
  \rho_{ABC} = P \rho_{ABC} P + Q \rho_{ABC} Q
  $$

  - Define $\sigma_{ABC} = P \rho_{ABC} P / \text{Tr}(P \rho_{ABC} P)$ and $\tau_{ABC} = Q \rho_{ABC} Q / \text{Tr}(Q \rho_{ABC} Q)$. Then we have:

  $$
  \rho_{ABC} = p \sigma_{ABC} + (1-p) \tau_{ABC}
  $$

  where $p = \text{Tr}(P \rho_{ABC} P)$ and $1-p = \text{Tr}(Q \rho_{ABC} Q)$.

  - By the joint convexity of the von Neumann entropy, we have:

  $$
  S(\rho_{ABC}) \leq p S(\sigma_{ABC}) + (1-p) S(\tau_{ABC})
  $$

  - Note that $\sigma_{ABC}$ and $\tau_{ABC}$ are both full-rank states, so their supports are the whole Hilbert space. Therefore, we can write:

  $$
  \sigma_{ABC} = \sigma_{AB} \otimes \sigma_{C}
  $$

  $$
  \tau_{ABC} = \tau_{AB} \otimes \tau_{C}
  $$

  where $\sigma_{AB} = \text{Tr}_C(\sigma_{ABC})$, $\sigma_{C} = \text{Tr}_{AB}(\sigma_{ABC})$, and similarly for $\tau_{AB}$ and $\tau_{C}$.

  - By the operator monotonicity of the logarithm function, we have:

  $$
  \log \sigma_{ABC} \leq \log \sigma_{AB} + \log \sigma_{C}
  $$

  $$
  \log \tau_{ABC} \leq \log \tau_{AB} + \log \tau_{C}
  $$

  - Taking the trace of both sides and multiplying by $-p$ and $-(1-p)$ respectively, we get:

  $$
  -p S(\sigma_{ABC}) \geq -p S(\sigma_{AB}) - p S(\sigma_{C})