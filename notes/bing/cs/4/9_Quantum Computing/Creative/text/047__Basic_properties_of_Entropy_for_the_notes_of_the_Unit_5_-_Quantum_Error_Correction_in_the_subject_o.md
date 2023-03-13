### Basic properties of Entropy for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Entropy is a measure of the uncertainty or disorder of a quantum system. It quantifies how much information is needed to describe the state of the system or how much information is gained by observing the system.
- The most common entropy measure in quantum information theory is the von Neumann entropy, defined as
$$
S(\rho) = -\mathrm{tr}(\rho \log \rho)
$$
where $\rho$ is the density matrix of the quantum system and $\log$ is the logarithm with base 2.
- The von Neumann entropy satisfies the following basic properties :
  - It is non-negative, i.e., $S(\rho) \geq 0$ for any $\rho$.
  - It is zero if and only if $\rho$ is a pure state, i.e., $\rho^2 = \rho$.
  - It is invariant under unitary transformations, i.e., $S(U\rho U^\dagger) = S(\rho)$ for any unitary operator $U$.
  - It is concave, i.e., $S(\sum_i p_i \rho_i) \geq \sum_i p_i S(\rho_i)$ for any probability distribution $\{p_i\}$ and density matrices $\{\rho_i\}$.
  - It is subadditive, i.e., $S(\rho_{AB}) \leq S(\rho_A) + S(\rho_B)$ for any bipartite system $\rho_{AB}$ and its reduced states $\rho_A$ and $\rho_B$.
  - It is upper bounded by the logarithm of the dimension of the Hilbert space, i.e., $S(\rho) \leq \log d$ for any $d$-dimensional system $\rho$.
  - It is equal to the Shannon entropy of the probability distribution of the eigenvalues of $\rho$, i.e., $S(\rho) = H(\lambda_1, \lambda_2, \dots, \lambda_d)$ where $\lambda_i$ are the eigenvalues of $\rho$ and $H$ is the Shannon entropy function.
- Another entropy measure that is useful in quantum information theory is the q-entropy, defined as
$$
S_q(\rho) = \frac{1}{q-1}(1 - \mathrm{tr}(\rho^q))
$$
where $q$ is a real parameter that determines the degree of nonlinearity of the entropy function. The q-entropy reduces to the von Neumann entropy when $q \to 1$.
- The q-entropy satisfies some of the properties of the von Neumann entropy, such as non-negativity, invariance under unitary transformations, and upper bound by the logarithm of the dimension. However, it does not satisfy concavity, subadditivity, or equality to the Shannon entropy of the eigenvalues.
- The q-entropy can be used to characterize the degree of entanglement of quantum states, as well as the efficiency of quantum data compression and quantum cryptography schemes.
- Entropy quantum computing is a novel approach to quantum computation that exploits the interaction of a quantum system with a carefully engineered environment, called the entropy, to drive the system to a desired solution state .
- Entropy quantum computing does not require error correction or isolation of the quantum system from the environment, as it uses the environment as a resource for computation. It also does not require gate operations or measurement, as the computation is performed by the relaxation of the quantum state .
- Entropy quantum computing is based on the principle of maximum entropy, which states that a quantum system will evolve to the state that maximizes its entropy, subject to the constraints imposed by the environment .
- Entropy quantum computing can be implemented using photonic systems, where the entropy is a specially designed optical cavity that couples to the quantum modes of the system. The cavity acts as a feedback mechanism that guides the system to the solution state .
- Entropy quantum computing can solve hard optimization problems, such as the traveling salesman problem, the knapsack problem, and the graph coloring problem, by encoding the problem constraints into the entropy and letting the system relax to the optimal state [^6^