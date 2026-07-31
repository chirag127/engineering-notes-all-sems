### Quantum Fourier transform

- The quantum Fourier transform (QFT) is the quantum implementation of the discrete Fourier transform (DFT) over the amplitudes of a wavefunction .
- The QFT is a part of many quantum algorithms, notably Shor's algorithm for factoring and computing the discrete logarithm, the quantum phase estimation algorithm for estimating the eigenvalues of a unitary operator, and algorithms for the hidden subgroup problem.
- The QFT acts on a quantum state vector (a quantum register), and the DFT acts on a vector. Both types of vectors can be written as lists of complex numbers.
- The QFT maps the state vector |x> = (x0, x1, ..., xN-1) to the state vector |y> = (y0, y1, ..., yN-1), where

  - yk = (1/sqrt(N)) * sum(j=0 to N-1) xj * exp(2*pi*i*j*k/N) for k = 0, 1, ..., N-1 .
  - i is the imaginary unit, sqrt(N) is the square root of N, and exp(z) is the exponential function of z.
  - The QFT is a unitary transformation, meaning that it preserves the norm of the state vector, i.e., sum(k=0 to N-1) |yk|^2 = sum(j=0 to N-1) |xj|^2 = 1.

- The QFT can be implemented by a quantum circuit consisting of Hadamard gates and controlled phase shift gates. The circuit can be decomposed into smaller subcircuits that act on subsets of qubits.
- The QFT can be used to perform various operations on quantum states, such as:

  - Finding the period of a periodic function.
  - Estimating the phase of a unitary operator.
  - Solving linear systems of equations.
  - Computing the discrete logarithm of a number.
  - Factoring large numbers.

- The QFT has some advantages over the classical DFT, such as:

  - The QFT can be performed in O(log^2 N) quantum gates, while the classical DFT requires O(N log N) operations.
  - The QFT can exploit quantum parallelism and interference to achieve exponential speedup for some problems.
  - The QFT can be used to create superposition states that encode more information than classical states.