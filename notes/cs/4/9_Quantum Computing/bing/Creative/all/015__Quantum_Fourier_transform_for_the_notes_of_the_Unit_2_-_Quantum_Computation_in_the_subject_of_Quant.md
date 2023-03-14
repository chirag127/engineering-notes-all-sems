### Quantum Fourier transform for the notes of the Unit 2 - Quantum Computation in the subject of Quantum Computing

- The quantum Fourier transform (QFT) is the quantum analogue of the discrete Fourier transform (DFT), which maps a vector of complex numbers to another vector of complex numbers according to a specific formula.
- The QFT acts on a quantum state vector (a quantum register) and transforms the amplitudes of the basis states according to the same formula as the DFT.
- The QFT is a linear and unitary transformation, meaning that it preserves the inner product and the norm of the quantum state vector.
- The QFT is a part of many quantum algorithms, such as Shor's algorithm for factoring and discrete logarithm, quantum phase estimation for finding the eigenvalues of a unitary operator, and algorithms for the hidden subgroup problem.
- The QFT can be implemented efficiently on a quantum computer using a quantum circuit consisting of Hadamard gates and controlled phase shift gates. The circuit has a complexity of O(n^2) gates, where n is the number of qubits. 
- The QFT can be approximated by truncating some of the phase shift gates, resulting in a circuit with O(n log n) gates and a small error.
- The QFT can be understood intuitively as a transformation between two bases: the computational basis and the Fourier basis. The computational basis consists of the binary states |0>, |1>, |00>, |01>, ..., while the Fourier basis consists of the superposition states |+>, |->, |++>, |+->, ..., where |+> = (|0> + |1>)/sqrt(2) and |-> = (|0> - |1>)/sqrt(2).
- The QFT can be seen as a generalization of the Hadamard gate, which is the single-qubit QFT. The Hadamard gate transforms between the Z-basis states |0> and |1> and the X-basis states |+> and |->. Similarly, the QFT transforms between the n-qubit computational basis states and the n-qubit Fourier basis states.
- The QFT can be expressed mathematically as follows: 

  - Given a quantum state |x> = sum_{j=0}^{N-1} x_j |j>, where N = 2^n and x_j are complex amplitudes, the QFT maps |x> to |y> = sum_{k=0}^{N-1} y_k |k>, where y_k are complex amplitudes given by: y_k = (1/sqrt(N)) sum_{j=0}^{N-1} x_j omega_N^{jk}, where omega_N = e^{2 pi i / N} is an N-th root of unity.
  - Alternatively, the QFT can be written as: |j> -> (1/sqrt(N)) sum_{k=0}^{N-1} omega_N^{jk} |k>, for each basis state |j>.
  - In matrix form, the QFT can be represented by a unitary matrix U_QFT = (1/sqrt(N)) sum_{j=0}^{N-1} sum_{k=0}^{N-1} omega_N^{jk} |k><j|.

- The QFT can be implemented using a quantum circuit as follows:

  - The circuit consists of n qubits, labeled from 0 to n-1, where qubit 0 is the least significant bit and qubit n-1 is the most significant bit.
  - The circuit has n layers, each consisting of a Hadamard gate on one qubit and some controlled phase shift gates on the other qubits.
  - The Hadamard gate on the i-th layer is applied to the i-th qubit, and the controlled phase shift gates are applied to the qubits with lower indices, with the control on the i-th qubit and the target on the j-th qubit, where j < i.
  - The phase shift angle for the gate on the i-th layer and the j-th qubit is 2 pi / 2^(i-j+1).
  - After applying all the layers, the qubits are reversed, so that the output state is in the