### Quantum Bits for the notes of the Unit 1 - Fundamental Concepts in the subject of Quantum Computing

- A quantum bit or qubit is the basic unit of quantum information, which is the quantum analog of the classic binary bit  .
- A qubit is a two-state or two-level quantum-mechanical system, such as an electron or photon, that can exist in a superposition of two states  .
- A superposition means that a qubit can be in a linear combination of both states at the same time, with some probability amplitude for each state  .
- The two states of a qubit are usually denoted by |0> and |1>, which are called computational basis states or standard basis states  .
- The general state of a qubit can be written as |ψ> = α|0> + β|1>, where α and β are complex numbers such that |α|^2 + |β|^2 = 1  .
- The coefficients α and β are called probability amplitudes, and their squared magnitudes |α|^2 and |β|^2 represent the probabilities of measuring the qubit in the state |0> or |1>, respectively  .
- A qubit can be manipulated by applying unitary transformations, which are reversible and preserve the norm of the state vector   .
- A unitary transformation can be represented by a 2x2 matrix U such that UU† = U†U = I, where U† is the adjoint or complex conjugate transpose of U, and I is the identity matrix   .
- A unitary transformation can change the state of a qubit from |ψ> to U|ψ>, which is another valid superposition of |0> and |1>   .
- A qubit can also be measured, which collapses the state of the qubit to either |0> or |1>, with probabilities |α|^2 and |β|^2, respectively  .
- A measurement destroys the superposition and the information about the original state of the qubit  .
- A qubit can store more information than a classical bit, because it can be in a superposition of two states, rather than just one  .
- A qubit can also exhibit quantum entanglement, which is a phenomenon where two or more qubits can share a quantum state and influence each other, even when they are physically separated  .
- Quantum entanglement enables quantum algorithms to perform parallel computations and achieve exponential speedups over classical algorithms  .

Some possible mnemonics and learning tricks for quantum bits are:

- Qubit = Quantum + Bit
- Qubit = Two-state + Superposition
- Qubit = |0> + |1>
- Qubit = α|0> + β|1>
- Qubit = Unitary + Measurement
- Qubit = More information + Entanglement

Some possible ascii diagrams for quantum bits are:

- A qubit in a superposition of |0> and |1>:

```
     |ψ>
     / \
    /   \
   /     \
  /       \
 |0>     |1>
```

- A unitary transformation on a qubit:

```
|ψ>  --U-->  U|ψ>
```

- A measurement on a qubit:

```
|ψ>  --M-->  |0> or |1>
```

- Two entangled qubits:

```
|ψ> = 1/√2 (|00> + |11>)

|0> ---|       |--- |0>
       |       |
|0> ---|---H---|--- |1>
```

Here