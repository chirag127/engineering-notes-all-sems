### Quantum Fourier transform

- The quantum Fourier transform (QFT) is the quantum implementation of the discrete Fourier transform (DFT) over the amplitudes of a wavefunction .
- The QFT is a part of many quantum algorithms, notably Shor's algorithm for factoring and computing the discrete logarithm, the quantum phase estimation algorithm for estimating the eigenvalues of a unitary operator, and algorithms for the hidden subgroup problem.
- The QFT acts on a quantum state vector (a quantum register), and the DFT acts on a vector. Both types of vectors can be written as lists of complex numbers.
- In the quantum case, the vector is a sequence of probability amplitudes for all the possible outcomes upon measurement (called basis states, or eigenstates).
- The QFT can be defined as follows:

  - Let $|x\rangle$ be an $n$-qubit state, where $x$ is an $n$-bit integer. Then the QFT maps $|x\rangle$ to $|y\rangle$, where $y$ is another $n$-bit integer, such that:

    $$|y\rangle = \frac{1}{\sqrt{2^n}}\sum_{x=0}^{2^n-1}e^{2\pi ixy/2^n}|x\rangle$$

  - The QFT can be implemented by a single unitary transformation, which can be decomposed into a product of simpler gates, such as Hadamard gates and controlled phase shift gates .
  - The QFT can be inverted by applying the inverse of the unitary transformation, which is the complex conjugate of the QFT matrix.
  - The QFT can be used to transform a quantum state from the computational basis to the Fourier basis, and vice versa.
  - The QFT can be used to perform efficient arithmetic operations, such as addition, multiplication, and modular exponentiation, on quantum states.
  - The QFT can be used to extract information about the periodicity or the phase of a quantum state, which is essential for many quantum algorithms.