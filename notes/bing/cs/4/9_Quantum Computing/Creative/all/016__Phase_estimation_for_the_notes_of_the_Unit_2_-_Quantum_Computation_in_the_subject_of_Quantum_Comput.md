### Phase estimation for the notes of the Unit 2 - Quantum Computation in the subject of Quantum Computing

- Phase estimation is a quantum algorithm to estimate the phase (or eigenvalue) of an eigenvector of a unitary operator.
- It is one of the most important subroutines in quantum computation, as it serves as a central building block for many quantum algorithms, such as Shor's algorithm, quantum counting, quantum amplitude amplification, and quantum simulation.
- The objective of the algorithm is to estimate θ θ in U |ψ = e2πiθ|ψ U | ψ = e 2 π i θ | ψ , where U U is a unitary operator and |ψ | ψ is an eigenvector of U U with eigenvalue e2πiθ e 2 π i θ .
- The algorithm uses two quantum registers: a control register of n n qubits initialized to |0 | 0 and a target register of m m qubits initialized to |ψ | ψ . The algorithm consists of the following steps:

  1. Apply a Hadamard gate to each qubit in the control register, creating an equal superposition of all possible states.
  2. Apply a controlled-U gate to each qubit in the control register, with the target register as the control qubit. The controlled-U gate applies U2j U 2 j to the target register, where j j is the index of the control qubit. This creates a phase kickback effect, where the phase of the eigenvalue is transferred to the control register.
  3. Apply an inverse quantum Fourier transform (QFT) to the control register, which converts the phase information into a binary representation of θ θ .
  4. Measure the control register, which gives an estimate of 2nθ 2 n θ modulo 1 1 . The precision of the estimate depends on the number of qubits in the control register and the value of θ θ .

- The algorithm can be illustrated by the following circuit diagram:

```
|0> ---H---*-----------------*-----------------*--- ... ---QFT---M---
            |                 |                 |
|0> ---H---*--------*--------|-----------------|--- ... ---QFT---M---
            |        |        |                 |
|0> ---H---*---*----|--------*-----------------|--- ... ---QFT---M---
            |   |    |        |                 |
|0> ---H---*-*-*----*--------*-----------------|--- ... ---QFT---M---
            | | |    |        |                 |
|ψ> -------U-U-U----U--------U-----------------U--- ... ---I--------
```

- A possible mnemonic to remember the steps of the algorithm is: **H**ave **C**ontrol, **K**ickback **P**hase, **F**ourier **T**ransform, **M**easure.
- A possible learning trick to understand the algorithm is to use a simple example, such as U = Z U = Z and |ψ = |+ | ψ = | + , where Z Z is the Pauli-Z gate and |+ = 1/√2(|0 + |1) | + = 1 / √ 2 ( | 0 + | 1 ) . In this case, the eigenvalue is eπi e π i and the phase is 1/2 1 / 2 . Using one qubit in the control register, the algorithm will produce the state |1 | 1 in the control register with probability 1 1 , which gives an estimate of 2 × 1/2 = 1 2 × 1 / 2 = 1 modulo 1 1 .