### Basic properties of Entropy for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Entropy is a measure of the intrinsic dispersion, uncertainty, or lack of information of a quantum state.
- Entropy is also related to the amount of information that can be extracted from a quantum system, or the amount of compression that can be achieved for a quantum source.
- The most common entropy measure in quantum information theory is the von Neumann entropy, defined as:

$$
S(\rho) = -\mathrm{Tr}(\rho \log \rho)
$$

where $\rho$ is the density matrix of the quantum system, and $\log$ is the logarithm base 2.

- The von Neumann entropy satisfies some basic properties, such as:

  - Non-negativity: $S(\rho) \geq 0$ for any $\rho$, and $S(\rho) = 0$ if and only if $\rho$ is a pure state.
  - Subadditivity: $S(\rho_{AB}) \leq S(\rho_A) + S(\rho_B)$ for any bipartite system $AB$, where $\rho_{AB}$ is the joint state and $\rho_A$ and $\rho_B$ are the reduced states. This means that the entropy of the whole system is less than or equal to the sum of the entropies of the subsystems.
  - Strong subadditivity: $S(\rho_{ABC}) + S(\rho_B) \leq S(\rho_{AB}) + S(\rho_{BC})$ for any tripartite system $ABC$. This means that the entropy of a subsystem cannot increase by adding another subsystem that is correlated with it.
  - Concavity: $S(\sum_i p_i \rho_i) \geq \sum_i p_i S(\rho_i)$ for any convex combination of states $\rho_i$ with probabilities $p_i$. This means that the entropy of a mixture of states is greater than or equal to the average entropy of the states.
  - Continuity: $S(\rho)$ is a continuous function of $\rho$, meaning that small changes in $\rho$ lead to small changes in $S(\rho)$.

- The von Neumann entropy can be interpreted as the Shannon entropy of the eigenvalues of the density matrix, or the expected value of the self-information of a quantum measurement.
- The von Neumann entropy can also be used to define other entropy measures, such as the conditional entropy, the mutual information, the relative entropy, and the quantum entropy divergence .
- The conditional entropy $S(A|B)$ measures the amount of uncertainty about system $A$ given system $B$. It is defined as:

$$
S(A|B) = S(AB) - S(B)
$$

- The mutual information $I(A:B)$ measures the amount of information that system $A$ and system $B$ share. It is defined as:

$$
I(A:B) = S(A) + S(B) - S(AB)
$$

- The relative entropy $D(\rho \| \sigma)$ measures the distance between two quantum states $\rho$ and $\sigma$. It is defined as:

$$
D(\rho \| \sigma) = \mathrm{Tr}(\rho \log \rho) - \mathrm{Tr}(\rho \log \sigma)
$$

- The quantum entropy divergence $D_\alpha(\rho \| \sigma)$ is a generalization of the relative entropy that depends on a parameter $\alpha$. It is defined as:

$$
D_\alpha(\rho \| \sigma) = \frac{1}{\alpha - 1} \log \mathrm{Tr}(\rho^\alpha \sigma^{1-\alpha})
$$

- The quantum entropy divergence reduces to the relative entropy when $\alpha = 1$, and to the quantum Rényi entropy when $\sigma = \mathbb{I}$, where $\mathbb{I}$ is the identity matrix.

- The quantum Rényi entropy $S_\alpha(\rho)$ is another generalization of the von Neumann entropy that depends on a parameter $\alpha$. It is defined as:

$$
S_\alpha(\rho) = \frac{1}{1-\alpha} \log \mathrm{Tr}(\rho^\alpha)
$$

- The quantum Rényi entropy reduces to the von Neumann entropy when $\alpha = 1$, and to the min