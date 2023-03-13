Measurement is the process of extracting information from a quantum state by performing an observation on it. Measurement is a fundamental operation in quantum computing, as it allows us to access the results of a quantum computation. However, measurement is also a destructive and probabilistic process, as it collapses the quantum state to one of the possible outcomes and erases the previous superposition and entanglement.

The following diagram illustrates the basic architecture of a measurement for the notes of the Unit 2 - Quantum Computation in the subject of Quantum Computing:

```
+-----------------+     +-----------------+     +-----------------+
| Quantum state   |     | Measurement     |     | Classical state |
| (superposition) | --> | (basis choice)  | --> | (outcome)       |
+-----------------+     +-----------------+     +-----------------+
```

The quantum state is represented by a vector of complex amplitudes, such as |ψ⟩ = α|0⟩ + β|1⟩, where |α|^2 + |β|^2 = 1. The measurement is specified by a basis choice, such as the computational basis {|0⟩, |1⟩} or the Hadamard basis {|+⟩, |-⟩}. The classical state is the result of the measurement, such as 0 or 1, which occurs with a certain probability, such as |α|^2 or |β|^2. The classical state can then be used for further computation or communication.