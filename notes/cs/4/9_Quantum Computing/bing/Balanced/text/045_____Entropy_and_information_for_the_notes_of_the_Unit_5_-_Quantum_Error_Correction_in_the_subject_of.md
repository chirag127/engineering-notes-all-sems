### Entropy and information for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Entropy is a measure of the uncertainty and the information content in the state of a physical system .
- In classical information theory, entropy quantifies the average amount of information that can be extracted from a random variable or a message source.
- The most common measure of entropy in classical information theory is the Shannon entropy, defined as

$$
H(X) = -\sum_{x \in \mathcal{X}} p(x) \log_2 p(x)
$$

where $X$ is a discrete random variable with alphabet $\mathcal{X}$ and probability distribution $p(x)$.
- Shannon entropy satisfies some desirable properties, such as non-negativity, additivity, and subadditivity.
- Shannon entropy also has an operational interpretation as the optimal compression rate of a message source, i.e., the minimum number of bits per symbol needed to encode the source without loss of information.
- In quantum information theory, entropy generalizes to the quantum realm, where the state of a physical system is described by a density matrix $\rho$ .
- The most common measure of entropy in quantum information theory is the von Neumann entropy, defined as

$$
S(\rho) = -\mathrm{Tr}(\rho \log_2 \rho)
$$

where $\mathrm{Tr}$ denotes the trace operation and $\log_2$ is the matrix logarithm .
- Von Neumann entropy satisfies some properties similar to Shannon entropy, such as non-negativity, additivity for tensor product states, and subadditivity for composite systems .
- Von Neumann entropy also has an operational interpretation as the optimal compression rate of a quantum source, i.e., the minimum number of qubits per symbol needed to encode the source without loss of quantum information .
- Von Neumann entropy also plays a crucial role in quantifying quantum entanglement, which is a form of quantum correlation that cannot be explained by classical physics  .
- One way to measure the amount of entanglement in a bipartite quantum state $\rho_{AB}$ is the entanglement of formation, defined as

$$
E_F(\rho_{AB}) = \min_{\{p_i, |\psi_i\rangle\}} \sum_i p_i S(\rho_A^i)
$$

where the minimum is taken over all possible pure state decompositions of $\rho_{AB} = \sum_i p_i |\psi_i\rangle \langle \psi_i|$, and $\rho_A^i = \mathrm{Tr}_B(|\psi_i\rangle \langle \psi_i|)$ is the reduced density matrix of subsystem $A$ .
- Entanglement of formation quantifies the minimum amount of entanglement needed to create a given mixed state $\rho_{AB}$ from a product state using local operations and classical communication (LOCC) .
- Entropy and information are important concepts for quantum error correction, which is a technique to protect quantum information from noise and decoherence .
- Quantum error correction relies on encoding quantum information in entangled states that span a larger Hilbert space than the original information, and using syndrome measurements and recovery operations to correct any errors that may occur .
- Entropy and information can be used to characterize the performance and limitations of quantum error correction codes, such as the quantum Hamming bound, the quantum Singleton bound, and the quantum Gilbert-Varshamov bound .
- Entropy and information can also be used to study the trade-off between the rate and the fidelity of quantum error correction codes, and to design optimal codes for different noise models and applications .