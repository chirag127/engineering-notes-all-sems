### Phase estimation for the notes of the Unit 2 - Quantum Computation in the subject of Quantum Computing

- Phase estimation is a quantum algorithm to estimate the phase (or eigenvalue) of an eigenvector of a unitary operator.
- The algorithm takes as input a unitary matrix U and a quantum state |ψ⟩ that is an eigenvector of U, such that U|ψ⟩ = e<sup>2πiθ</sup>|ψ⟩, where 0 ≤ θ < 1 is the phase (or eigenvalue) to be estimated.
- The algorithm uses two registers: the first register consists of n qubits initialized to |0⟩, and the second register consists of m qubits initialized to |ψ⟩.
- The algorithm performs the following steps: 
  - Apply a Hadamard gate to each qubit in the first register, creating a superposition of all possible states.
  - Apply controlled-U<sup>2<sup>k</sup></sup> operations to the first register, where k is the index of the qubit and U is the unitary operator. This encodes the phase θ into the first register.
  - Apply an inverse quantum Fourier transform (QFT<sup>†</sup>) to the first register, which transforms the phase θ into a binary representation.
  - Measure the first register, obtaining an n-bit approximation of θ.
- The algorithm outputs the measured value of θ with high probability within additive error ε, using O(log(1/ε)) qubits and O(1/ε) controlled-U operations.
- Phase estimation is frequently used as a subroutine in other quantum algorithms, such as Shor's algorithm and the quantum algorithm for linear systems of equations.
- A mnemonic to remember the steps of the algorithm is: **HUCQUM** (Hadamard, U<sup>2<sup>k</sup></sup>, QFT<sup>†</sup>, Measure).
- A simple example of phase estimation is to estimate the phase of the Z gate, which has eigenvalues ±1 and eigenvectors |0⟩ and |1⟩. If the second register is initialized to |1⟩, then the phase is 1/2 and the algorithm will output 10<sub>2</sub> = 2<sub>10</sub> with high probability.
- A diagram of the phase estimation circuit is shown below:

```
|0> ---H---*-----------------*-------------------*-----QFT†---M---|θ1>
           |                 |                   |
|0> ---H---|--------*--------|---------*---------|-----QFT†---M---|θ2>
           |        |        |         |         |
|0> ---H---|--------|--------*---------|---*-----|-----QFT†---M---|θ3>
           |        |        |         |   |     |
|0> ---H---|--------|--------|---------*---|---*--|-----QFT†---M---|θ4>
           |        |        |         |   |   |
|ψ> -------U2^0-----U2^1-----U2^2-----U2^3-U2^4-U2^5----------------|ψ>
```