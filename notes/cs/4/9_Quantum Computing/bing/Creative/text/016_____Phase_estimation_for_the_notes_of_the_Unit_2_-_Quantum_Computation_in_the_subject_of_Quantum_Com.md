### Phase estimation

- Phase estimation is a quantum algorithm to estimate the phase (or eigenvalue) of an eigenvector of a unitary operator.
- The objective of the algorithm is to find θ in U|ψ> = e<sup>2πiθ</sup>|ψ>, where U is a unitary operator and |ψ> is an eigenvector of U with eigenvalue e<sup>2πiθ</sup>.
- The algorithm uses two quantum registers: one for the input state |ψ> and one for the output state |0><sup>n</sup>, where n is the number of qubits used to store the estimate of θ.
- The algorithm consists of the following steps:
  - Apply a Hadamard gate to each qubit in the output register, creating an equal superposition of all possible states.
  - Apply a controlled-U<sup>2<sup>k</sup></sup> gate to the k-th qubit in the output register and the input register, where U<sup>2<sup>k</sup></sup> is the unitary operator U repeated 2<sup>k</sup> times. This creates a phase shift of 2<sup>k</sup>θ on the k-th qubit in the output register.
  - Apply an inverse quantum Fourier transform (QFT<sup>†</sup>) to the output register, transforming the phase shifts into a binary representation of θ.
  - Measure the output register, obtaining an n-bit approximation of θ.
- The algorithm has a success probability of at least 4/π<sup>2</sup> ≈ 40.5% for any choice of n. The accuracy of the estimate can be improved by increasing n or repeating the algorithm multiple times.
- Phase estimation is a central building block for many quantum algorithms, such as Shor's algorithm, quantum counting, quantum amplitude amplification, and quantum simulation . It can also be used to implement a measurement for essentially any Hermitian operator.