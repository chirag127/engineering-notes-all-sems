### Phase estimation

Phase estimation is a quantum algorithm that estimates the phase (or eigenvalue) of an eigenvector of a unitary operator. It is a central building block for many quantum algorithms, such as Shor's algorithm and the quantum algorithm for linear systems of equations. It also implements a measurement for essentially any Hermitian operator, by discretizing the pointer register using qubits.

The problem that phase estimation solves is the following: given a unitary operator U and a quantum state |ψ⟩ that is an eigenvector of U, such that U|ψ⟩ = e<sup>2πiθ</sup>|ψ⟩, where 0 ≤ θ < 1, find the eigenvalue e<sup>2πiθ</sup> or equivalently, the phase θ, to a desired level of precision.

The algorithm consists of the following steps:

1. Setup: The input consists of two registers: the upper n qubits comprise the first register, and the lower m qubits are the second register. The first register is initialized to the state |0⟩<sup>⊗n</sup>, and the second register is initialized to the state |ψ⟩. The total initial state is |0⟩<sup>⊗n</sup>|ψ⟩.
2. Create superposition: Apply the Hadamard gate to each qubit in the first register, creating an equal superposition of all computational basis states. The state becomes (1/√2<sup>n</sup>)∑<sub>j=0</sub><sup>2<sup>n</sup>-1</sup>|j⟩|ψ⟩, where j is the binary representation of the integer j.
3. Apply controlled unitary operations: For each qubit j in the first register, apply a controlled-U<sup>2<sup>j</sup></sup> operation, where U is the unitary operator whose eigenvalue we want to estimate. The state becomes (1/√2<sup>n</sup>)∑<sub>j=0</sub><sup>2<sup>n</sup>-1</sup>|j⟩U<sup>j</sup>|ψ⟩ = (1/√2<sup>n</sup>)∑<sub>j=0</sub><sup>2<sup>n</sup>-1</sup>|j⟩e<sup>2πijθ</sup>|ψ⟩.
4. Apply inverse quantum Fourier transform: Apply the inverse quantum Fourier transform (QFT<sup>-1</sup>) to the first register, which transforms the state to |φ⟩|ψ⟩, where |φ⟩ is an approximation of the binary representation of θ, with n bits of precision.
5. Measurement: Measure the first register in the computational basis, and obtain the value φ. This value is an estimate of θ, with a high probability of being correct. The error can be reduced by increasing the number of qubits in the first register.

The following circuit diagram illustrates the phase estimation algorithm:

![Phase estimation circuit](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Phase_estimation.svg/800px-Phase_estimation.svg.png)

Source: [Quantum phase estimation algorithm - Wikipedia](https://en.wikipedia.org/wiki/Quantum_phase_estimation_algorithm)