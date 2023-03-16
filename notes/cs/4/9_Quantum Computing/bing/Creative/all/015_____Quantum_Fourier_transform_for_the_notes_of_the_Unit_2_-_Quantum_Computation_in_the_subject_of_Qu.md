# Quantum Fourier Transform

The quantum Fourier transform (QFT) is the quantum implementation of the discrete Fourier transform (DFT) over the amplitudes of a wavefunction. It is part of many quantum algorithms, most notably Shor's factoring algorithm and quantum phase estimation.

The DFT acts on a vector $(x_0,..., x_{N-1})$ and maps it to the vector $(y_0,..., y_{N-1})$ by the formula:

$$
y_k = \frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} x_j e^{2\pi ijk/N}
$$

The QFT acts on a quantum statevector (a quantum register), which can be written as a linear combination of basis states, or eigenstates, with complex coefficients. The basis states are labeled by binary strings of length $n$, where $N = 2^n$. For example, a quantum statevector of three qubits can be written as:

$$
|\psi\rangle = \sum_{j=0}^{7} x_j |j\rangle = x_0 |000\rangle + x_1 |001\rangle + ... + x_7 |111\rangle
$$

The QFT maps this statevector to another statevector by the formula:

$$
|\psi\rangle \xrightarrow{QFT} |\phi\rangle = \sum_{k=0}^{7} y_k |k\rangle = y_0 |000\rangle + y_1 |001\rangle + ... + y_7 |111\rangle
$$

where the coefficients $y_k$ are given by the same formula as the DFT:

$$
y_k = \frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} x_j e^{2\pi ijk/N}
$$

The QFT can be implemented as a single unitary transformation, which can be decomposed into a sequence of simpler quantum gates, such as Hadamard gates and controlled phase gates. The circuit diagram for the QFT on three qubits is shown below:

![QFT circuit](https://qiskit.org/textbook/ch-algorithms/images/qft_3.png)

The QFT has several important properties and applications in quantum computing, such as:

- It is reversible, meaning that it can be inverted by applying the inverse QFT, which is the same as the QFT with the opposite sign in the exponent.
- It is efficient, meaning that it can be implemented with a polynomial number of quantum gates, unlike the classical DFT which requires a superpolynomial number of operations.
- It can be used to perform quantum phase estimation, which is a technique to estimate the eigenvalues of a unitary operator by applying the QFT to the eigenstates of the operator.
- It can be used to perform Shor's algorithm, which is a quantum algorithm to factor large numbers by reducing the problem to finding the period of a function using the QFT.
- It can be used to solve the hidden subgroup problem, which is a generalization of the period-finding problem and has applications in cryptography and coding theory.