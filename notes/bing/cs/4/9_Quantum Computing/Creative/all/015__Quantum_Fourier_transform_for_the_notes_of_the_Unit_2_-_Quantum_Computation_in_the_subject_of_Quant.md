### Quantum Fourier transform for the notes of the Unit 2 - Quantum Computation in the subject of Quantum Computing

- The quantum Fourier transform (QFT) is the quantum implementation of the discrete Fourier transform (DFT) over the amplitudes of a quantum state  .
- The DFT acts on a vector of N complex numbers (x0, x1, ..., xN-1) and maps it to another vector of N complex numbers (y0, y1, ..., yN-1) by the formula :

  yk = (1/sqrt(N)) * sum(j=0 to N-1) of xj * exp(2*pi*i*j*k/N)

  where i is the imaginary unit and exp is the exponential function.

- The QFT acts on a quantum state of n qubits, which can be written as a superposition of 2^n basis states :

  |psi> = sum(j=0 to 2^n-1) of aj * |j>

  where aj are complex amplitudes and |j> are binary strings of length n.

- The QFT maps this state to another state of n qubits, which can be written as a superposition of 2^n basis states :

  |phi> = sum(k=0 to 2^n-1) of bk * |k>

  where bk are complex amplitudes and |k> are binary strings of length n.

- The QFT can be expressed as a unitary matrix of size 2^n x 2^n, which can be decomposed into a product of simpler unitary matrices, such as Hadamard gates and controlled phase gates .
- The QFT can be implemented as a quantum circuit with O(n^2) gates, where n is the number of qubits .
- The QFT is a part of many quantum algorithms, such as Shor's algorithm for factoring and computing the discrete logarithm, the quantum phase estimation algorithm for estimating the eigenvalues of a unitary operator, and algorithms for the hidden subgroup problem  .
- The QFT can be used to perform fast Fourier transforms on quantum data, which can be useful for signal processing, data compression, and frequency analysis.
- The QFT can also be used to create quantum states with periodic or symmetric properties, such as the W state or the GHZ state.

- A possible mnemonic for remembering the QFT formula is to think of the exponent as a dot product between the binary representations of j and k, where each bit is multiplied by pi/2^n. For example, if n = 3 and j = 5 (101 in binary) and k = 6 (110 in binary), then the exponent is:

  2*pi*i*j*k/N = 2*pi*i*(1*1 + 0*1 + 1*0)/8 = pi*i/2

- A possible learning trick for understanding the QFT circuit is to use the swap test to compare the input and output states of the QFT. The swap test is a quantum circuit that can measure the overlap between two quantum states using an ancilla qubit. The swap test can be used to verify that the QFT preserves the norm of the state, and that the QFT is its own inverse (up to a global phase).