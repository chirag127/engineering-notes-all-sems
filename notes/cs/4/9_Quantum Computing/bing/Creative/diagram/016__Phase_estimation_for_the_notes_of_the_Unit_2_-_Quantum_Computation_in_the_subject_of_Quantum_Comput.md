### Phase estimation for the notes of the Unit 2 - Quantum Computation in the subject of Quantum Computing

The following diagram illustrates the basic architecture of a phase estimation algorithm for a unitary operator U and an eigenvector |ψ⟩ of U with eigenvalue e2πiθ, where 0≤θ<1. The algorithm uses n qubits as the first register and m qubits as the second register. The first register is initialized to |0⟩ and the second register is initialized to |ψ⟩. The algorithm consists of the following steps:

1. Apply a Hadamard gate to each qubit in the first register to create a superposition of all possible states.
2. Apply controlled-Uk gates to the first register, where k is the power of 2 corresponding to the position of the qubit. For example, the most significant qubit is controlled by U2n-1, and the least significant qubit is controlled by U.
3. Apply an inverse quantum Fourier transform (QFT†) to the first register to obtain an approximation of θ in binary representation.
4. Measure the first register to get an n-bit estimate of θ.

The diagram is shown below using ASCII art. The symbols are as follows:

- |0⟩ and |ψ⟩ are the initial states of the registers.
- H is the Hadamard gate.
- C is the control qubit for the controlled-Uk gate.
- U is the unitary operator U.
- k is the power of 2 for the controlled-Uk gate.
- QFT† is the inverse quantum Fourier transform.
- M is the measurement operation.

```
|0⟩-H-C-U2n-1---QFT†-M-θn
|0⟩-H-C-U2n-2---QFT†-M-θn-1
|0⟩-H-C-U2n-3---QFT†-M-θn-2
|0⟩-H-C-U2n-4---QFT†-M-θn-3
|0⟩-H-C-U2n-5---QFT†-M-θn-4
|0⟩-H-C-U2n-6---QFT†-M-θn-5
|0⟩-H-C-U2n-7---QFT†-M-θn-6
|0⟩-H-C-U2n-8---QFT†-M-θn-7
|0⟩-H-C-U2n-9---QFT†-M-θn-8
|0⟩-H-C-U2n-10--QFT†-M-θn-9
|0⟩-H-C-U2n-11--QFT†-M-θn-10
|0⟩-H-C-U2n-12--QFT†-M-θn-11
|0⟩-H-C-U2n-13--QFT†-M-θn-12
|0⟩-H-C-U2n-14--QFT†-M-θn-13
|0⟩-H-C-U2n-15--QFT†-M-θn-14
|0⟩-H-C-U-------QFT†-M-θ1
|ψ⟩-------------Uk
```