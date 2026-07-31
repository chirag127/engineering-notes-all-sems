# Entropy and information for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Entropy is a measure of the uncertainty and the information content in the state of a physical system.
- In classical information theory, entropy quantifies the amount of information that can be extracted from a random variable or a message source.
- The most common measure of entropy in classical information theory is the Shannon entropy, defined as:

$$H(X) = -\sum_{x \in X} p(x) \log_2 p(x)$$

where $X$ is a discrete random variable with probability distribution $p(x)$.
- The Shannon entropy satisfies some important properties, such as:

  - Non-negativity: $H(X) \geq 0$ for any $X$.
  - Additivity: $H(X,Y) = H(X) + H(Y)$ if $X$ and $Y$ are independent.
  - Subadditivity: $H(X,Y) \leq H(X) + H(Y)$ for any $X$ and $Y$.
  - Conditional entropy: $H(X|Y) = H(X,Y) - H(Y)$, which measures the uncertainty of $X$ given $Y$.
  - Chain rule: $H(X_1, X_2, \dots, X_n) = H(X_1) + H(X_2|X_1) + \dots + H(X_n|X_1, \dots, X_{n-1})$.
  - Data processing inequality: $H(X) \geq H(f(X))$ for any function $f$, which means that processing data cannot increase its information content.

- In quantum information theory, entropy generalizes to measure the uncertainty and the information content in the state of a quantum system.
- The most common measure of entropy in quantum information theory is the von Neumann entropy, defined as:

$$S(\rho) = -\text{Tr}(\rho \log_2 \rho)$$

where $\rho$ is a density matrix of a quantum system.
- The von Neumann entropy satisfies some important properties, such as:

  - Non-negativity: $S(\rho) \geq 0$ for any $\rho$.
  - Additivity: $S(\rho \otimes \sigma) = S(\rho) + S(\sigma)$ if $\rho$ and $\sigma$ are density matrices of independent quantum systems.
  - Subadditivity: $S(\rho_{AB}) \leq S(\rho_A) + S(\rho_B)$ for any bipartite quantum system $\rho_{AB}$ with reduced density matrices $\rho_A$ and $\rho_B$.
  - Conditional entropy: $S(\rho_A|\rho_B) = S(\rho_{AB}) - S(\rho_B)$, which measures the uncertainty of $\rho_A$ given $\rho_B$.
  - Chain rule: $S(\rho_{A_1 A_2 \dots A_n}) = S(\rho_{A_1}) + S(\rho_{A_2}|\rho_{A_1}) + \dots + S(\rho_{A_n}|\rho_{A_1} \dots \rho_{A_{n-1}})$.
  - Data processing inequality: $S(\rho) \geq S(\mathcal{E}(\rho))$ for any quantum operation $\mathcal{E}$, which means that processing quantum data cannot increase its information content.

- The von Neumann entropy is related to the compressibility of a quantum state, which is the minimum number of qubits needed to store the state with negligible error.
- The von Neumann entropy is also related to the entanglement of a quantum state, which is the amount of quantum correlations between the subsystems of a bipartite quantum system.
- The entanglement of formation of a pure bipartite quantum state $\rho_{AB}$ is equal to the von Neumann entropy of either of its reduced density matrices, i.e., $E_F(\rho_{AB}) = S(\rho_A) = S(\rho_B)$.
- The entanglement of formation of a mixed bipartite quantum state $\rho_{AB}$ is defined as the minimum average entanglement of formation over all possible pure state decompositions of $\rho_{AB}$, i