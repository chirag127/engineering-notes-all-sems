### Entropy and information for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Entropy is a measure of the uncertainty and the information content in the state of a physical system .
- In classical information theory, entropy quantifies the amount of information that can be extracted from a random variable or a message source.
- The most common measure of entropy in classical information theory is the Shannon entropy, defined as

$$
H(X) = -\sum_{x} p(x) \log p(x)
$$

where $X$ is a discrete random variable with probability distribution $p(x)$.
- Shannon entropy satisfies some desirable properties, such as being non-negative, being maximal for a uniform distribution, being additive for independent variables, and being invariant under permutations.
- Shannon entropy also has an operational interpretation as the optimal compression rate of a message source, i.e., the minimum number of bits per symbol needed to encode the source without loss of information.
- In quantum information theory, entropy generalizes to the quantum realm, where the state of a physical system is described by a density matrix $\rho$ .
- The most common measure of entropy in quantum information theory is the von Neumann entropy, defined as

$$
S(\rho) = -\text{Tr}(\rho \log \rho)
$$

where $\text{Tr}$ denotes the trace operation .
- Von Neumann entropy satisfies some properties analogous to Shannon entropy, such as being non-negative, being maximal for a maximally mixed state, being additive for uncorrelated systems, and being invariant under unitary transformations .
- Von Neumann entropy also has an operational interpretation as the optimal compression rate of a quantum source, i.e., the minimum number of qubits per quantum state needed to encode the source without loss of quantum information .
- However, von Neumann entropy also has some features that are distinct from Shannon entropy, such as being subadditive for correlated systems, being non-increasing under quantum operations, and being related to the entanglement of quantum states .
- Entanglement is a quantum phenomenon that allows two or more systems to share quantum correlations that cannot be explained by classical physics .
- Entanglement is a valuable resource for quantum information processing, such as quantum cryptography, quantum teleportation, and quantum computation .
- A measure of entanglement for pure bipartite quantum states is the entanglement entropy, defined as the von Neumann entropy of the reduced density matrix of either subsystem, i.e.,

$$
E(\rho_{AB}) = S(\rho_A) = S(\rho_B)
$$

where $\rho_{AB}$ is the pure state of the composite system $AB$, and $\rho_A$ and $\rho_B$ are the reduced states of the subsystems $A$ and $B$, obtained by tracing out the other subsystem .
- Entanglement entropy quantifies the amount of information that is inaccessible to local measurements on either subsystem, and that can only be revealed by global measurements on the composite system .
- A measure of entanglement for mixed bipartite quantum states is the entanglement of formation, defined as the minimum average entanglement entropy of a pure state decomposition of the mixed state, i.e.,

$$
E_F(\rho_{AB}) = \min_{\{p_i, \psi_i\}} \sum_i p_i E(\psi_i)
$$

where $\rho_{AB} = \sum_i p_i |\psi_i\rangle\langle\psi_i|$ is an ensemble of pure states $|\psi_i\rangle$ with probabilities $p_i$ .
- Entanglement of formation quantifies the amount of entanglement that is needed to create the mixed state from a product state by local operations and classical communication .
- Entropy and entanglement are important concepts for quantum error correction, which is the process of protecting quantum information from noise and decoherence .
- Quantum error correction relies on encoding quantum information in entangled states that span a larger Hilbert space, and using redundancy and syndrome