### Entropy and information for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Entropy is a measure of the uncertainty and the information content in the state of a physical system.
- In classical information theory, entropy quantifies the amount of information that can be extracted from a random variable or a message source.
- The most common measure of entropy in classical information theory is the Shannon entropy, defined as:

$$
H(X) = -\sum_{x \in X} p(x) \log_2 p(x)
$$

where $X$ is a discrete random variable with probability distribution $p(x)$.
- Shannon entropy satisfies some desirable properties, such as:

  - Non-negativity: $H(X) \geq 0$ for any $X$.
  - Additivity: $H(X,Y) = H(X) + H(Y)$ if $X$ and $Y$ are independent.
  - Maximum entropy: $H(X) \leq \log_2 |X|$ where $|X|$ is the size of the alphabet of $X$, and the equality holds if and only if $X$ is uniformly distributed.
  - Data processing inequality: $H(X) \geq H(f(X))$ for any function $f$, meaning that no processing of the data can increase the information content.

- A mnemonic to remember the formula of Shannon entropy is: **H**ow much **information** is in a **random variable**? **Sum** up the **probabilities** of each **outcome** times the **log** of the **inverse probabilities**.
- In quantum information theory, entropy generalizes to the quantum realm, where the state of a physical system is described by a density matrix $\rho$.
- The most common measure of entropy in quantum information theory is the von Neumann entropy, defined as:

$$
S(\rho) = -\mathrm{Tr}(\rho \log_2 \rho)
$$

where $\mathrm{Tr}$ is the trace operator.
- Von Neumann entropy satisfies some properties similar to Shannon entropy, such as:

  - Non-negativity: $S(\rho) \geq 0$ for any $\rho$.
  - Additivity: $S(\rho \otimes \sigma) = S(\rho) + S(\sigma)$ if $\rho$ and $\sigma$ are density matrices of independent systems.
  - Maximum entropy: $S(\rho) \leq \log_2 d$ where $d$ is the dimension of the Hilbert space, and the equality holds if and only if $\rho$ is the maximally mixed state $\frac{1}{d} I$.
  - Data processing inequality: $S(\rho) \geq S(\mathcal{E}(\rho))$ for any quantum operation $\mathcal{E}$, meaning that no quantum processing of the state can increase the information content.

- A mnemonic to remember the formula of von Neumann entropy is: **S**how me the **information** in a **density matrix**. **Trace** out the **matrix** times the **log** of the **matrix**.
- Entropy and information play a crucial role in quantum error correction, which is the process of protecting quantum information from noise and decoherence.
- One of the main goals of quantum error correction is to encode quantum information in such a way that the entropy of the encoded state is minimized, while the information content is maximized.
- A useful concept for quantum error correction is the entanglement of formation, which measures the amount of entanglement that is needed to create a given quantum state.
- The entanglement of formation of a bipartite quantum state $\rho_{AB}$ is defined as:

$$
E_F(\rho_{AB}) = \min_{\{p_i, |\psi_i\rangle\}} \sum_i p_i S(\mathrm{Tr}_B |\psi_i\rangle\langle\psi_i|)
$$

where the minimum is taken over all possible decompositions of $\rho_{AB}$ as a convex combination of pure states $|\psi_i\rangle$.
- The entanglement of formation satisfies some properties, such as:

  - Non-negativity: $E_F(\rho_{AB}) \geq 0$ for any $\rho_{AB}$.
  - Symmetry: $