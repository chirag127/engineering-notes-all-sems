# Entropy and Information for the Notes of the Unit 5 - Quantum Error Correction in the Subject of Quantum Computing

- Entropy is a measure of the uncertainty and the information content in the state of a physical system.
- In classical information theory, entropy quantifies the amount of information that can be extracted from a random variable or a message source.
- The most common measure of entropy in classical information theory is the Shannon entropy, defined as:

$$
H(X) = -\sum_{x \in X} p(x) \log_2 p(x)
$$

where $X$ is a discrete random variable with probability distribution $p(x)$.
- The Shannon entropy satisfies some important properties, such as:

  - $H(X) \geq 0$ and $H(X) = 0$ if and only if $X$ is a constant.
  - $H(X) \leq \log_2 |X|$ and $H(X) = \log_2 |X|$ if and only if $X$ is uniformly distributed.
  - $H(X,Y) = H(X) + H(Y)$ if and only if $X$ and $Y$ are independent.
  - $H(X|Y) = H(X,Y) - H(Y)$ is the conditional entropy of $X$ given $Y$, which measures the remaining uncertainty of $X$ after observing $Y$.
  - $H(X|Y) \leq H(X)$ and $H(X|Y) = 0$ if and only if $X$ is a function of $Y$.
  - $I(X;Y) = H(X) - H(X|Y) = H(Y) - H(Y|X)$ is the mutual information between $X$ and $Y$, which measures the reduction of uncertainty of $X$ due to $Y$ or vice versa.
  - $I(X;Y) \geq 0$ and $I(X;Y) = 0$ if and only if $X$ and $Y$ are independent.

- In quantum information theory, entropy generalizes to measure the uncertainty and the information content in the state of a quantum system.
- The most common measure of entropy in quantum information theory is the von Neumann entropy, defined as:

$$
S(\rho) = -\mathrm{Tr}(\rho \log_2 \rho)
$$

where $\rho$ is a density matrix of a quantum system.
- The von Neumann entropy satisfies some important properties, such as:

  - $S(\rho) \geq 0$ and $S(\rho) = 0$ if and only if $\rho$ is a pure state.
  - $S(\rho) \leq \log_2 d$ and $S(\rho) = \log_2 d$ if and only if $\rho$ is the maximally mixed state of dimension $d$.
  - $S(\rho_A \otimes \rho_B) = S(\rho_A) + S(\rho_B)$ for any two quantum systems $A$ and $B$.
  - $S(\rho_{AB}) \geq S(\rho_A)$ and $S(\rho_{AB}) \geq S(\rho_B)$ for any bipartite quantum system $AB$.
  - $S(\rho_A) = S(\rho_B)$ for any pure bipartite quantum state $\rho_{AB}$, which is also called the entanglement entropy of $\rho_{AB}$.
  - $S(\rho_A|\rho_B) = S(\rho_{AB}) - S(\rho_B)$ is the conditional entropy of $A$ given $B$, which measures the remaining uncertainty of $A$ after observing $B$.
  - $S(\rho_A|\rho_B) \leq S(\rho_A)$ and $S(\rho_A|\rho_B) = 0$ if and only if $\rho_{AB}$ is a product state.
  - $I(\rho_{AB}) = S(\rho_A) - S(\rho_A|\rho_B) = S(\rho_B) - S(\rho_B|\rho_A)$ is the quantum mutual information between $A$ and $B$, which measures the total correlation (classical and quantum) between $A$ and $B$.
  - $I(\rho_{AB}) \geq 0$ and $I(\rho_{AB})