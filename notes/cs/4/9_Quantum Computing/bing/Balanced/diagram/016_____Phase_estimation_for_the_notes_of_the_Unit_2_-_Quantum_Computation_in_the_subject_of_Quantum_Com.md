### Phase estimation

Phase estimation is a quantum algorithm that estimates the phase (or eigenvalue) of an eigenvector of a unitary operator. It is a central building block for many quantum algorithms, such as Shor's algorithm, quantum Fourier transform, and quantum machine learning . It also implements a measurement for essentially any Hermitian operator.

The objective of the algorithm is the following: Given a unitary operator U and an eigenvector |ψ⟩ of U, the algorithm estimates θ in U|ψ⟩ = e<sup>2πiθ</sup>|ψ⟩. Here, θ is a fraction in [0, 1) and e<sup>2πiθ</sup> is the corresponding eigenvalue of U.

The algorithm uses two quantum registers: a control register of n qubits, initialized to |0⟩<sup>⊗n</sup>, and a target register of m qubits, initialized to |ψ⟩. The algorithm consists of the following steps:

1. Apply a Hadamard gate to each qubit in the control register, creating an equal superposition of all possible states.
2. Apply a controlled-U<sup>2<sup>j</sup></sup> gate to the target register for each qubit in the control register, where j is the index of the control qubit. This creates a phase kickback to the control register, such that the state becomes:

    |Ψ⟩ = 1/√2<sup>n</sup> ∑<sub>k=0</sub><sup>2<sup>n</sup>-1</sup> e<sup>2πiθk</sup>|k⟩|ψ⟩

3. Apply an inverse quantum Fourier transform to the control register, which transforms the state to:

    |Ψ⟩ ≈ |2<sup>n</sup>θ⟩|ψ⟩

4. Measure the control register in the computational basis, which gives an n-bit approximation of 2<sup>n</sup>θ. Divide the measurement result by 2<sup>n</sup> to obtain an estimate of θ.

The accuracy of the algorithm depends on the number of qubits in the control register and the value of θ. The algorithm succeeds with high probability if 2<sup>n</sup>θ is close to an integer. The more qubits are used, the higher the precision of the estimate. However, the algorithm also requires more resources, such as the number of controlled-U gates and the complexity of the inverse quantum Fourier transform. Therefore, there is a trade-off between accuracy and efficiency in phase estimation.