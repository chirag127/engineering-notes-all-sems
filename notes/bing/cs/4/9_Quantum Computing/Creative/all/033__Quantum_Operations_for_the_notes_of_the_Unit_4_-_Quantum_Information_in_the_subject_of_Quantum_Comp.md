### Quantum Operations for the notes of the Unit 4 - Quantum Information in the subject of Quantum Computing

- Quantum operations are mathematical transformations that describe how a quantum system can evolve over time, interact with other systems, or be measured by an observer.
- Quantum operations are formulated in terms of the density operator, which is a matrix that represents the state of a quantum system as a mixture of pure states.
- A quantum operation is a linear, completely positive map from the set of density operators into itself. This means that it preserves the properties of being a valid density operator, such as being positive, trace one, and Hermitian.
- A quantum operation can be represented by a unitary matrix, a Kraus decomposition, a superoperator, or a quantum circuit.
- A unitary matrix is a matrix that preserves the inner product of vectors, and thus the norm and the angle between them. A unitary matrix can be applied to a quantum state vector to produce another quantum state vector. A unitary matrix is reversible and deterministic, meaning that it can be inverted and that it produces a unique output for a given input.
- A Kraus decomposition is a way of expressing a quantum operation as a sum of products of operators, called Kraus operators, that act on the quantum system. A Kraus decomposition can capture the effects of noise, decoherence, and measurement on a quantum system. A Kraus decomposition is not unique, meaning that there can be different sets of Kraus operators that represent the same quantum operation.
- A superoperator is a matrix that acts on the space of density operators, rather than on the space of state vectors. A superoperator can be obtained from a Kraus decomposition by taking the tensor product of each Kraus operator with its conjugate transpose. A superoperator is also reversible and deterministic, but it is usually larger and less efficient than a unitary matrix.
- A quantum circuit is a graphical representation of a quantum operation as a sequence of elementary quantum gates, which are unitary matrices that act on one or more qubits. A quantum circuit can be used to implement quantum algorithms, such as Shor's algorithm or Grover's algorithm, on a quantum computer. A quantum circuit can also include non-unitary operations, such as measurements, conditional branches, or classical feedback.

Some examples of quantum operations are:

- The Pauli-Z gate, which is a unitary matrix that flips the sign of the state |1⟩, leaving the state |0⟩ unchanged. It can be represented by the matrix:

```
Z = |0⟩⟨0| - |1⟩⟨1| = [1 0]
                        [0 -1]
```

- The Hadamard gate, which is a unitary matrix that creates a superposition of the states |0⟩ and |1⟩, with equal amplitudes and phases. It can be represented by the matrix:

```
H = 1/√2 (|0⟩⟨0| + |0⟩⟨1| + |1⟩⟨0| - |1⟩⟨1|) = 1/√2 [1 1]
                                                        [1 -1]
```

- The measurement operation, which is a non-unitary operation that collapses the quantum state to one of its basis states, with a probability proportional to the square of the amplitude of that state. It can be represented by a set of Kraus operators, such as:

```
M0 = |0⟩⟨0| = [1 0]
              [0 0]

M1 = |1⟩⟨1| = [0 0]
              [0 1]
```

- The IF operation, which is a non-unitary operation that applies a quantum gate to a quantum system only if a classical condition is satisfied. It can be represented by a quantum circuit, such as:

```
IF (c == 1) THEN Z
```

where c is a classical bit and Z is the Pauli-Z gate.