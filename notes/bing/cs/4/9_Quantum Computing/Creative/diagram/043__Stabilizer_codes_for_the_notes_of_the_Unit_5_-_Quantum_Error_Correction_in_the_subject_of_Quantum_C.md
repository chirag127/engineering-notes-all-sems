The following is a detailed ASCII diagram for stabilizer codes for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing.

A stabilizer code is a quantum error-correcting code that appends ancilla qubits to the qubits that we want to protect. A unitary encoding circuit rotates the global state into a subspace of a larger Hilbert space. This highly entangled, encoded state corrects for local noisy errors.

The basic architecture of a stabilizer code consists of three main components: an encoder, a syndrome measurement, and a decoder. The encoder is a unitary circuit that maps the logical qubits to the physical qubits. The syndrome measurement is a set of commuting observables that detect the errors without disturbing the encoded state. The decoder is a recovery operation that corrects the errors based on the syndrome outcome.

The diagram below shows an example of a stabilizer code that encodes one logical qubit into three physical qubits. The encoder is a Hadamard gate followed by a controlled-NOT gate. The syndrome measurement is a set of two stabilizer generators: X1X2 and X2X3. The decoder is a set of conditional X gates based on the syndrome bits.

```
Logical qubit: |ψ> = α|0> + β|1>

Encoder: U = H1 ⊗ CNOT12 ⊗ CNOT23

Encoded state: |ψ'> = U|ψ> = α|000> + β|111>

Syndrome measurement: M = {X1X2, X2X3}

Syndrome outcome: s = (s1, s2) = (M1|ψ'>, M2|ψ'>)

Decoder: R = X1^s1 ⊗ X3^s2

Recovered state: |ψ''> = R|ψ'> = |ψ>

Diagram:

|ψ> ──H──●───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────|ψ''>
         │
         │
         │
         │
         │
         │
         │
         │
         │
         │
         │
         │
         │
         │
         │
         │
         │
         │
         │
         │
         │
         │
         │
         └──X──●──M1──●──X^s1──●
              │      │         │
              │      │         │
              │      │         │
              │      │         │
              │      │         │
              │      │         │
              │      │         │
              │      │         │
              │      │         │
              │      │         │
              │      │         │
              │      │         │
              │      │         │
              └──X──●──M2──●──X^s2──●
                   │      │         │
                   │      │         │
                   │      │         │
                   │      │         │
                   │      │         │
                   │      │         │
                   │      │         │
                   │      │         │
                   │      │         │
                   │      │         │
                   │      │         │
                   │      │         │
                   │      │         │
                   └──────┘         └───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────|ψ''>
```