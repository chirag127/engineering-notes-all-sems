### Quantum Fourier transform

- The quantum Fourier transform (QFT) is the quantum implementation of the discrete Fourier transform (DFT) over the amplitudes of a wavefunction .
- The QFT is a part of many quantum algorithms, notably Shor's algorithm for factoring and computing the discrete logarithm, the quantum phase estimation algorithm for estimating the eigenvalues of a unitary operator, and algorithms for the hidden subgroup problem.
- The QFT acts on a quantum state vector (a quantum register), and the DFT acts on a vector. Both types of vectors can be written as lists of complex numbers.
- In the quantum case, the vector is a sequence of probability amplitudes for all the possible outcomes upon measurement (called basis states, or eigenstates).
- The QFT can be defined as follows:

  - Let |x> be an n-qubit state, where x is an n-bit integer. Then the QFT maps |x> to |y>, where y is another n-bit integer, such that:

    - |y> = (1/sqrt(2^n)) * sum_{k=0}^{2^n-1} exp(2*pi*i*x*k/2^n) |k>

  - The QFT can be implemented as a single unitary transformation, which can be decomposed into a product of simpler gates, such as Hadamard gates and controlled phase shift gates .
  - The QFT can be inverted by applying the inverse of each gate in reverse order.
  - The QFT has a circuit complexity of O(n^2) gates, where n is the number of qubits.
  - The QFT can be used to perform efficient quantum algorithms for various problems, such as:

    - Period finding: Given a periodic function f(x) = f(x+r) for some unknown r, the QFT can be used to find r in O(n) steps, where n is the number of qubits needed to store x.
    - Phase estimation: Given a unitary operator U and an eigenstate |psi> of U, the QFT can be used to estimate the eigenvalue of U corresponding to |psi> with high precision in O(log(1/epsilon)) steps, where epsilon is the desired accuracy.
    - Order finding: Given a positive integer N and a positive integer a coprime to N, the QFT can be used to find the order of a modulo N, i.e., the smallest positive integer r such that a^r = 1 (mod N), in O((log N)^3) steps.
    - Factoring: Given a composite integer N, the QFT can be used to find its prime factors in O((log N)^3) steps, by using the order finding algorithm as a subroutine.
    - Discrete logarithm: Given a positive integer N, a primitive root g of N, and an integer h such that h = g^x (mod N) for some unknown x, the QFT can be used to find x in O((log N)^3) steps, by using the order finding algorithm as a subroutine.
    - Hidden subgroup: Given a finite group G, a subgroup H of G, and a function f: G -> S that is constant on each coset of H and distinct on different cosets, the QFT can be used to find a set of generators of H in O(log |G|) steps, by using the phase estimation algorithm as a subroutine.