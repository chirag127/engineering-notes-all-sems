### Entropy and information for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Entropy is a measure of the uncertainty and the information content in the state of a physical system .
- In classical information theory, entropy quantifies the amount of information that can be extracted from a random variable or a message source .
- The most common measure of entropy in classical information theory is the Shannon entropy, defined as

$$
H(X) = -\sum_{x} p(x) \log p(x),
$$

where $X$ is a discrete random variable with probability distribution $p(x)$ .
- Shannon entropy satisfies some desirable properties, such as non-negativity, additivity, and subadditivity .
- Shannon entropy also has an operational interpretation as the optimal compression rate of a message source, i.e., the minimum number of bits per symbol needed to encode the source without loss of information .
- In quantum information theory, entropy generalizes to the quantum realm, where the state of a physical system is described by a density matrix $\rho$ .
- The most common measure of entropy in quantum information theory is the von Neumann entropy, defined as

$$
S(\rho) = -\mathrm{Tr}(\rho \log \rho),
$$

where $\mathrm{Tr}$ denotes the trace operation .
- Von Neumann entropy satisfies some properties similar to Shannon entropy, such as non-negativity, additivity for tensor product states, and subadditivity for composite systems .
- Von Neumann entropy also has an operational interpretation as the optimal compression rate of a quantum source, i.e., the minimum number of qubits per quantum state needed to encode the source without loss of quantum information .
- Von Neumann entropy plays a crucial role in quantum information processing, especially in the context of quantum error correction .
- Quantum error correction is a technique to protect quantum information from noise and decoherence by encoding it in a larger quantum system that can detect and correct errors .
- One of the main challenges in quantum error correction is to find efficient and robust codes that can correct a large number of errors with a small amount of redundancy .
- One of the main tools to analyze and design quantum error correction codes is the concept of entanglement, which is a quantum phenomenon that describes the non-local correlations between quantum systems .
- Entanglement can be quantified by various measures, such as entanglement entropy, entanglement of formation, entanglement distillation, and entanglement cost .
- Entanglement entropy is the von Neumann entropy of the reduced density matrix of a subsystem, i.e.,

$$
S(\rho_A) = -\mathrm{Tr}(\rho_A \log \rho_A),
$$

where $\rho_A = \mathrm{Tr}_B(\rho_{AB})$ is the partial trace over the subsystem $B$ of a bipartite system $AB$ .
- Entanglement entropy measures the amount of entanglement between the subsystems $A$ and $B$, and it satisfies some properties such as non-negativity, symmetry, and strong subadditivity .
- Entanglement of formation is the minimum amount of entanglement needed to create a given bipartite quantum state by local operations and classical communication (LOCC), i.e.,

$$
E_F(\rho_{AB}) = \min_{\{p_i, |\psi_i\rangle\}} \sum_i p_i S(\rho_A^i),
$$

where the minimum is taken over all possible ensembles $\{p_i, |\psi_i\rangle\}$ of pure states $|\psi_i\rangle$ that can produce the state $\rho_{AB}$ with probabilities $p_i$, and $\rho_A^i = \mathrm{Tr}_B(|\psi_i\rangle\langle\psi_i|)$ .
- Entanglement of formation measures the cost of creating entanglement, and it