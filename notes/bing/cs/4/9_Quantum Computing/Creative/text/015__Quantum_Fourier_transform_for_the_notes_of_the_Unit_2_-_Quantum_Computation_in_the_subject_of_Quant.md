### Quantum Fourier transform

- The quantum Fourier transform (QFT) is the quantum implementation of the discrete Fourier transform (DFT) over the amplitudes of a quantum state  .
- The DFT acts on a vector of N complex numbers (x0, x1, ..., xN-1) and maps it to another vector of N complex numbers (y0, y1, ..., yN-1) by the formula :

  `y_k = (1/sqrt(N)) * sum_{j=0}^{N-1} x_j * exp(2*pi*i*j*k/N)`

  where i is the imaginary unit and exp is the exponential function.
- The inverse DFT is given by:

  `x_j = (1/sqrt(N)) * sum_{k=0}^{N-1} y_k * exp(-2*pi*i*j*k/N)`

- The QFT is defined as a unitary transformation on a quantum state of n qubits, where N = 2^n, that maps the basis state |j> to the superposition state  :

  `|j> -> (1/sqrt(N)) * sum_{k=0}^{N-1} exp(2*pi*i*j*k/N) |k>`

  where |j> and |k> are binary representations of the integers j and k, respectively.
- The inverse QFT is given by :

  `|k> -> (1/sqrt(N)) * sum_{j=0}^{N-1} exp(-2*pi*i*j*k/N) |j>`

- The QFT can be implemented efficiently on a quantum computer using a circuit of O(n^2) gates, where n is the number of qubits .
- The QFT is a part of many quantum algorithms, notably Shor's algorithm for factoring and computing the discrete logarithm, the quantum phase estimation algorithm for estimating the eigenvalues of a unitary operator, and algorithms for the hidden subgroup problem .