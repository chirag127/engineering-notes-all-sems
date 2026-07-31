### Phase estimation

- Phase estimation is a quantum algorithm to estimate the phase (or eigenvalue) of an eigenvector of a unitary operator.
- The objective of the algorithm is to find θ in U|ψ> = e<sup>2πiθ</sup>|ψ>, where U is a unitary operator and |ψ> is an eigenvector of U with eigenvalue e<sup>2πiθ</sup>.
- The algorithm uses two quantum registers: a counting register of n qubits initialized to |0>, and an eigenstate register of m qubits initialized to |ψ>.
- The algorithm consists of the following steps :
  - Apply a Hadamard gate to each qubit in the counting register, creating an equal superposition of all possible states.
  - Apply a controlled-U<sup>2<sup>k</sup></sup> gate to the k-th qubit in the counting register and the eigenstate register, where U<sup>2<sup>k</sup></sup> is the unitary operator U repeated 2<sup>k</sup> times. This creates a phase kickback on the counting register, such that the state becomes:

  |Ψ> = 1/√2<sup>n</sup> Σ<sub>k=0</sub><sup>2<sup>n</sup>-1</sup> e<sup>2πi2<sup>k</sup>θ</sup>|k>|ψ>

  - Apply an inverse quantum Fourier transform (QFT<sup>-1</sup>) to the counting register, which transforms the state to:

  |Ψ> = 1/2<sup>n</sup> Σ<sub>k=0</sub><sup>2<sup>n</sup>-1</sup> Σ<sub>j=0</sub><sup>2<sup>n</sup>-1</sup> e<sup>-2πijk/2<sup>n</sup></sup> e<sup>2πi2<sup>k</sup>θ</sup>|j>|ψ>

  - Measure the counting register in the computational basis, which gives a value j with probability:

  p(j) = 1/2<sup>2n</sup> |Σ<sub>k=0</sub><sup>2<sup>n</sup>-1</sup> e<sup>2πi(2<sup>k</sup>θ-j/2<sup>n</sup>)</sup>|<sup>2</sup>

  - The measured value j is an approximation of 2<sup>n</sup>θ, which can be used to estimate θ by dividing j by 2<sup>n</sup>.
- The algorithm can achieve an accuracy of O(2<sup>-n</sup>) with high probability, which means that the number of qubits in the counting register determines the precision of the estimation.
- Phase estimation is a central building block for many quantum algorithms, such as Shor's algorithm, quantum counting, quantum amplitude amplification, and quantum simulation.