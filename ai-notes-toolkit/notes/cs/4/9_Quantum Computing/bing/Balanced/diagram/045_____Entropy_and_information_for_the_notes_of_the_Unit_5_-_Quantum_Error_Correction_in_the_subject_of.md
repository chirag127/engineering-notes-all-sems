### Entropy and information for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Entropy is a measure of the uncertainty and the information content in the state of a physical system.
- In classical information theory, entropy quantifies the amount of information that can be extracted from a random variable or a message source.
- The most common measure of entropy in classical information theory is the Shannon entropy, defined as

$$
H(X) = -\sum_{x \in X} p(x) \log_2 p(x)
$$

where $X$ is a discrete random variable with probability distribution $p(x)$.
- Shannon entropy satisfies some desirable properties, such as being non-negative, additive for independent variables, and maximal for uniform distributions.
- Shannon entropy also has an operational interpretation as the optimal compression rate of a message source, i.e., the minimum number of bits per symbol needed to encode the source without loss of information.
- In quantum information theory, entropy generalizes to the quantum realm, where the state of a physical system is described by a density matrix $\rho$.
- The most common measure of entropy in quantum information theory is the von Neumann entropy, defined as

$$
S(\rho) = -\mathrm{Tr}(\rho \log_2 \rho)
$$

where $\mathrm{Tr}$ denotes the trace operation.
- Von Neumann entropy satisfies some properties analogous to Shannon entropy, such as being non-negative, additive for uncorrelated systems, and maximal for maximally mixed states.
- Von Neumann entropy also has an operational interpretation as the optimal compression rate of a quantum source, i.e., the minimum number of qubits per quantum state needed to encode the source without loss of coherence.
- Von Neumann entropy plays a crucial role in quantum information theory, as it quantifies various aspects of quantum information processing, such as entanglement, quantum communication, quantum cryptography, and quantum thermodynamics.
- One important application of von Neumann entropy is the entanglement of formation, which measures the amount of entanglement that can be created from a given bipartite quantum state $\rho_{AB}$.
- The entanglement of formation is defined as

$$
E_F(\rho_{AB}) = \min_{\{p_i, |\psi_i\rangle\}} \sum_i p_i S(\rho_A^i)
$$

where the minimum is taken over all possible decompositions of $\rho_{AB}$ as a convex combination of pure states $|\psi_i\rangle$, and $\rho_A^i = \mathrm{Tr}_B(|\psi_i\rangle\langle\psi_i|)$ is the reduced state of system $A$.
- The entanglement of formation quantifies the minimum amount of pure entanglement needed to prepare $\rho_{AB}$ by local operations and classical communication (LOCC).
- The entanglement of formation is related to the quantum error correction, as it characterizes the trade-off between the amount of entanglement and the amount of noise that can be tolerated in a quantum channel.