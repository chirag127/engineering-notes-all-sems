### Shannon Entropy for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Shannon entropy is a measure of the uncertainty or information content of a random variable or a probability distribution.
- In classical information theory, Shannon entropy quantifies the average number of bits needed to encode a message drawn from a given source.
- In quantum information theory, Shannon entropy can be generalized to quantum systems, where the random variable is replaced by a quantum state and the probability distribution is replaced by the density matrix.
- The quantum analogue of Shannon entropy is the von Neumann entropy, which is defined as

$$
S(\rho) = -\text{Tr}(\rho \log \rho),
$$

where $\rho$ is the density matrix of the quantum system and $\text{Tr}$ denotes the trace operation.
- The von Neumann entropy satisfies some of the same properties as the Shannon entropy, such as non-negativity, concavity, subadditivity, and the chain rule.
- The von Neumann entropy also has some quantum-specific properties, such as being invariant under unitary transformations, being zero for pure states, and being bounded by the logarithm of the dimension of the Hilbert space.
- The von Neumann entropy can be used to measure the compressibility of a quantum state, the amount of quantum information in a quantum system, and the degree of entanglement between quantum subsystems .
- One application of the von Neumann entropy is the quantum Shannon theory, which studies the transmission and processing of quantum information through noisy quantum channels.
- Quantum Shannon theory generalizes and extends the classical Shannon theory to the quantum domain, and establishes fundamental limits and optimal protocols for quantum communication and computation.
- Some of the main topics in quantum Shannon theory are quantum data compression, quantum channel capacity, quantum error correction, quantum cryptography, and quantum entanglement distillation.
- A useful mnemonic to remember the definition of the von Neumann entropy is to think of it as the quantum version of the Gibbs entropy, which is defined as

$$
S_G(p) = -k_B \sum_i p_i \log p_i,
$$

where $p_i$ are the probabilities of the classical states and $k_B$ is the Boltzmann constant.
- The von Neumann entropy replaces the classical probabilities with the quantum density matrix, and the Boltzmann constant with the natural logarithm base.
- Another useful mnemonic to remember the properties of the von Neumann entropy is to use the acronym NICSUB, which stands for Non-negativity, Invariance, Concavity, Subadditivity, and Upper Bound.
- A simple example of calculating the von Neumann entropy is to consider a qubit in a mixed state

$$
\rho = p |0\rangle \langle 0| + (1-p) |1\rangle \langle 1|,
$$

where $0 \leq p \leq 1$.
- The von Neumann entropy of this state is

$$
S(\rho) = -p \log p - (1-p) \log (1-p),
$$

which is the same as the Shannon entropy of a binary source with probability $p$.
- The von Neumann entropy of this state is zero when $p=0$ or $p=1$, which corresponds to a pure state, and is maximal when $p=1/2$, which corresponds to a maximally mixed state.