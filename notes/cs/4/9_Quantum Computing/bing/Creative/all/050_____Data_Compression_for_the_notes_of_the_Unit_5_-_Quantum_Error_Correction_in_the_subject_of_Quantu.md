# Data Compression for Quantum Computing

Data compression is the process of reducing the amount of information needed to store or transmit data. Data compression can be useful for saving storage space, bandwidth, and computational resources. Data compression can also be applied to quantum information, which is encoded in quantum bits (qubits) that can exist in superpositions of two states.

## Quantum Data Compression

Quantum data compression is the quantum analogue of classical data compression. It aims to reduce the number of qubits needed to store or transmit quantum information, while preserving the fidelity of the information. Quantum data compression can be achieved by exploiting the quantum correlations or entanglement among the qubits, or by using quantum error correction codes.

Quantum data compression can be divided into two types: lossless and lossy. Lossless quantum data compression preserves the exact quantum state of the original data, while lossy quantum data compression allows some distortion or degradation of the quantum state. Lossless quantum data compression is also known as quantum source coding or quantum Schumacher compression, while lossy quantum data compression is also known as quantum rate distortion coding or quantum Lloyd-Max compression.

## Quantum Source Coding

Quantum source coding is the lossless quantum data compression of a quantum source, which is a device that produces a stream of identical or independent and identically distributed (i.i.d.) quantum states. Quantum source coding aims to find the optimal quantum code that can compress the quantum source into the minimum number of qubits, while allowing perfect reconstruction of the original quantum states.

The optimal quantum code for quantum source coding is given by the quantum Shannon-Fano coding theorem, which states that the minimum number of qubits per quantum state is equal to the von Neumann entropy of the quantum source. The von Neumann entropy is a measure of the quantum uncertainty or randomness of a quantum state, and is defined as

$$
S(\rho) = -\mathrm{Tr}(\rho \log \rho)
$$

where $\rho$ is the density matrix of the quantum state, and $\mathrm{Tr}$ is the trace operator. The von Neumann entropy is analogous to the Shannon entropy of a classical source, which measures the classical information content of a classical state.

The quantum Shannon-Fano coding theorem can be proved by using the quantum noiseless coding theorem, which states that the quantum source can be compressed into a subspace of the Hilbert space spanned by the qubits, such that the compression is reversible and noiseless. The quantum noiseless coding theorem can be derived by using the quantum singular value decomposition (SVD) and the quantum Schmidt decomposition.

An example of quantum source coding is the quantum compression of three qubits into two qubits, which was demonstrated experimentally for the first time in 2019. The quantum source was a device that produced three identical qubits in the state

$$
|\psi\rangle = \alpha |0\rangle + \beta |1\rangle
$$

where $\alpha$ and $\beta$ are complex coefficients such that $|\alpha|^2 + |\beta|^2 = 1$. The quantum code was a quantum circuit that applied a unitary transformation to the three qubits, such that the quantum state was compressed into two qubits, while the third qubit was discarded. The unitary transformation was designed to preserve the fidelity of the quantum state, which is the overlap between the original and the compressed state. The fidelity was measured by using quantum state tomography, which is a technique to reconstruct the quantum state from a set of measurements.

The quantum compression of three qubits into two qubits can be seen as a special case of the quantum compression of $n$ qubits into $m$ qubits, where $n > m$. The general quantum compression of $n$ qubits into $m$ qubits can be achieved by using quantum error correction codes, which are quantum codes that can protect quantum information from errors or noise.

## Quantum Error Correction

Quantum error correction is the process of encoding quantum information into a larger number of qubits, such that the quantum information can be recovered from errors or noise that affect the qubits. Quantum error correction can be seen as a form of quantum data compression, where the quantum information is compressed into a smaller number of logical qubits, which are encoded into a larger number of physical qubits.

Quantum error correction can be performed by using quantum error correction codes, which are quantum codes that can detect and correct errors or noise that affect the qubits. Quantum error correction codes can be classified into two types: passive and active. Passive quantum error correction codes rely on the quantum correlations or ent