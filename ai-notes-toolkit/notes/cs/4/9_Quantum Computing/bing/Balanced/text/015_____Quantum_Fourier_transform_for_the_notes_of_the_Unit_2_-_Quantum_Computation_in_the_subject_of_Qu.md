### Quantum Fourier transform

- The quantum Fourier transform (QFT) is the quantum implementation of the discrete Fourier transform (DFT) over the amplitudes of a wavefunction .
- The QFT is a part of many quantum algorithms, notably Shor's algorithm for factoring and computing the discrete logarithm, the quantum phase estimation algorithm for estimating the eigenvalues of a unitary operator, and algorithms for the hidden subgroup problem.
- The QFT acts on a quantum state vector (a quantum register), and the DFT acts on a vector. Both types of vectors can be written as lists of complex numbers.
- In the quantum case, the vector is a sequence of probability amplitudes for all the possible outcomes upon measurement (called basis states, or eigenstates).
- The QFT can be defined as follows:

  - Let $|x\rangle$ be an $n$-qubit state, where $x$ is an $n$-bit integer. Then the QFT maps $|x\rangle$ to $|y\rangle$, where $y$ is another $n$-bit integer, such that:

    $$|y\rangle = \frac{1}{\sqrt{2^n}}\sum_{x=0}^{2^n-1}e^{2\pi ixy/2^n}|x\rangle$$

  - Equivalently, the QFT can be written in terms of the computational basis states $|0\rangle$ and $|1\rangle$ as:

    $$\text{QFT}|x_1x_2...x_n\rangle = \frac{1}{\sqrt{2^n}}\sum_{k_1,k_2,...,k_n=0}^1 e^{2\pi i(x_1k_1/2+x_2k_2/4+...+x_nk_n/2^n)}|k_1k_2...k_n\rangle$$

  - The QFT can be implemented as a single unitary transformation, which can be decomposed into a product of simpler unitary operations, such as Hadamard gates and controlled phase shift gates .
- The QFT has several properties that make it useful for quantum algorithms:

  - The QFT is reversible, meaning that it can be inverted by applying the inverse QFT, which is the same as the QFT with a negative sign in the exponent.
  - The QFT is periodic, meaning that it maps periodic functions to periodic functions, and preserves the period of the function.
  - The QFT is linear, meaning that it preserves superpositions of quantum states, and can be applied to any linear combination of basis states.
  - The QFT is symmetric, meaning that it does not depend on the order of the qubits in the quantum register, and can be applied to any permutation of the basis states.