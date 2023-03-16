# Entropy and Information for the Notes of the Unit 5 - Quantum Error Correction in the Subject of Quantum Computing

- Entropy is a measure of the uncertainty and the information content in the state of a physical system.
- In classical information theory, entropy quantifies the amount of information that can be extracted from a random variable or a message source.
- The most common measure of entropy in classical information theory is the Shannon entropy, defined as:

$$
H(X) = -\sum_{x \in X} p(x) \log_2 p(x)
$$

where $X$ is a discrete random variable with probability distribution $p(x)$.
- The Shannon entropy satisfies the following properties:
  - $H(X) \geq 0$ and $H(X) = 0$ if and only if $X$ is a constant.
  - $H(X) \leq \log_2 |X|$ where $|X|$ is the size of the alphabet of $X$. The equality holds if and only if $X$ is uniformly distributed.
  - $H(X,Y) = H(X) + H(Y|X) = H(Y) + H(X|Y)$ where $H(Y|X)$ is the conditional entropy of $Y$ given $X$.
  - $H(X,Y) \leq H(X) + H(Y)$ with equality if and only if $X$ and $Y$ are independent.
  - $H(X_1, X_2, \dots, X_n) \leq \sum_{i=1}^n H(X_i)$ with equality if and only if the $X_i$ are independent.
- The Shannon entropy is related to the compressibility of a message source. The source coding theorem states that the optimal compression rate of a message source is equal to its entropy.
- In quantum information theory, entropy generalizes to the quantum realm, where the state of a physical system is described by a density matrix $\rho$.
- The most common measure of entropy in quantum information theory is the von Neumann entropy, defined as:

$$
S(\rho) = -\text{Tr}(\rho \log_2 \rho)
$$

where $\text{Tr}$ denotes the trace operation.
- The von Neumann entropy satisfies the following properties:
  - $S(\rho) \geq 0$ and $S(\rho) = 0$ if and only if $\rho$ is a pure state.
  - $S(\rho) \leq \log_2 d$ where $d$ is the dimension of the Hilbert space of $\rho$. The equality holds if and only if $\rho$ is maximally mixed.
  - $S(\rho_{AB}) = S(\rho_A) + S(\rho_B|\rho_A) = S(\rho_B) + S(\rho_A|\rho_B)$ where $\rho_{AB}$ is a bipartite state and $\rho_A$, $\rho_B$ are the reduced states of the subsystems $A$ and $B$. $S(\rho_B|\rho_A)$ is the conditional entropy of $B$ given $A$.
  - $S(\rho_{AB}) \leq S(\rho_A) + S(\rho_B)$ with equality if and only if $\rho_{AB}$ is separable.
  - $S(\rho_{A_1 A_2 \dots A_n}) \leq \sum_{i=1}^n S(\rho_{A_i})$ with equality if and only if $\rho_{A_1 A_2 \dots A_n}$ is separable.
- The von Neumann entropy is related to the compressibility of a quantum state. The quantum source coding theorem states that the optimal compression rate of a quantum state is equal to its entropy.
- The von Neumann entropy is also related to the entanglement of a quantum state. The entanglement of formation is a measure of the amount of entanglement required to create a given quantum state. For pure bipartite states, the entanglement of formation is equal to the entropy of either subsystem. For mixed bipartite states, the entanglement of formation is defined as the minimum average entropy of the subsystems over all possible pure state decompositions of the mixed state.