# Quantum Fourier Transform

- The quantum Fourier transform (QFT) is the quantum implementation of the discrete Fourier transform (DFT) over the amplitudes of a wavefunction .
- The QFT is a part of many quantum algorithms, notably Shor's algorithm for factoring and computing the discrete logarithm, the quantum phase estimation algorithm for estimating the eigenvalues of a unitary operator, and algorithms for the hidden subgroup problem.
- The QFT acts on a quantum state vector (a quantum register), and the DFT acts on a vector. Both types of vectors can be written as lists of complex numbers.
- In the quantum case, the vector is a sequence of probability amplitudes for all the possible outcomes upon measurement (called basis states, or eigenstates).
- The QFT is defined as follows :

  - Let $|x\rangle$ be an $n$-qubit state, where $x$ is an $n$-bit integer. Then the QFT maps $|x\rangle$ to $|y\rangle$, where $y$ is another $n$-bit integer, as follows:

    $$\text{QFT}|x\rangle = \frac{1}{\sqrt{2^n}}\sum_{y=0}^{2^n-1}e^{2\pi ixy/2^n}|y\rangle$$

  - Equivalently, the QFT can be written in terms of the binary expansions of $x$ and $y$ as follows:

    $$\text{QFT}|x_1x_2...x_n\rangle = \frac{1}{\sqrt{2^n}}\sum_{y_1=0}^1\sum_{y_2=0}^1...\sum_{y_n=0}^1e^{2\pi i(x_1y_1/2+x_2y_1/4+...+x_ny_1/2^n+x_1y_2/4+...+x_ny_2/2^{n+1}+...+x_1y_n/2^n+...+x_ny_n/2^{2n})}|y_1y_2...y_n\rangle$$

  - The QFT can also be expressed as a product of unitary matrices, each corresponding to a single-qubit or two-qubit gate, as follows:

    $$\text{QFT} = \prod_{k=1}^n\left(H_k\prod_{j=1}^{k-1}R_{jk}\right)$$

    where $H_k$ is the Hadamard gate applied to the $k$-th qubit, and $R_{jk}$ is the controlled phase shift gate applied to the $j$-th and $k$-th qubits, defined as:

    $$H_k = \frac{1}{\sqrt{2}}\begin{bmatrix}1 & 1\\ 1 & -1\end{bmatrix}$$

    $$R_{jk} = \begin{bmatrix}1 & 0\\ 0 & e^{2\pi i/2^{k-j}}\end{bmatrix}$$

- The QFT is reversible, meaning that it has an inverse operation, denoted by $\text{QFT}^{-1}$, that can undo the QFT and recover the original state .
- The inverse QFT is defined as follows :

  - Let $|y\rangle$ be an $n$-qubit state, where $y$ is an $n$-bit integer. Then the inverse QFT maps $|y\rangle$ to $|x\rangle$, where $x$ is another $n$-bit integer, as follows:

    $$\text{QFT}^{-1}|y\rangle = \frac{1}{\sqrt{2^n}}\sum_{x=0}^{2^n-1}e^{-2\pi ixy/2^n}|x\rangle$$

  - Equivalently, the inverse QFT can be written in terms of the binary expansions of $x$ and $y$ as follows:

    $$\text{QFT}^{-1}|y_1y_2...y_n\rangle =