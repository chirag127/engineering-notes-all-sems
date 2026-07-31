### Phase estimation

Phase estimation is a quantum algorithm that estimates the phase (or eigenvalue) of an eigenvector of a unitary operator. It is a central building block for many quantum algorithms, such as Shor's algorithm, quantum Fourier transform, and quantum machine learning. It can also be used to implement a measurement for any Hermitian operator.

The main idea of the algorithm is to use a quantum register of n qubits, initialized in the state |0...0>, and apply a Hadamard gate to each qubit, creating a superposition of all possible states. Then, the unitary operator U is applied to the register, controlled by an ancilla qubit that is in the state |ψ>, which is an eigenvector of U with eigenvalue e<sup>2πiθ</sup>, where θ is the phase to be estimated. The result is a state of the form:

|ψ> ⊗ (|0...0> + e<sup>2πiθ</sup>|0...01> + e<sup>2πi2θ</sup>|0...010> + ... + e<sup>2πi2<sup>n-1</sup>θ</sup>|1...1>)/√2<sup>n</sup>

Then, a quantum Fourier transform is applied to the register, which transforms the state into:

|ψ> ⊗ (|0...0> + e<sup>-2πiθ</sup>|0...01> + e<sup>-2πi2θ</sup>|0...010> + ... + e<sup>-2πi2<sup>n-1</sup>θ</sup>|1...1>)/√2<sup>n</sup>

Finally, a measurement is performed on the register, which gives a binary number that is an approximation of θ in the form of 0.θ<sub>1</sub>θ<sub>2</sub>...θ<sub>n</sub>. The accuracy of the estimation depends on the number of qubits in the register and the value of θ. The algorithm succeeds with high probability if θ is a rational number with a small denominator, or if it is close to such a number.

The following is a schematic diagram of the phase estimation algorithm:

![Phase estimation algorithm](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Phase_Estimation_Algorithm.svg/800px-Phase_Estimation_Algorithm.svg.png)

Some key points to remember about phase estimation are:

- It requires a unitary operator U and an eigenvector |ψ> of U as inputs.
- It outputs an approximation of the phase (or eigenvalue) of |ψ> with respect to U.
- It uses a quantum register of n qubits and an ancilla qubit to perform the computation.
- It applies a Hadamard gate, a controlled-U gate, a quantum Fourier transform, and a measurement to the register.
- It has applications in many quantum algorithms and measurements.