### Quantum Algorithms

Quantum algorithms are algorithms that run on a quantum computer, which is a machine that combines the power of classical and quantum computing. A quantum computer consists of a classical computer that controls a quantum processor, which is a device that manipulates quantum bits or qubits. Qubits are the basic units of quantum information, and they can exist in superpositions of two states, such as 0 and 1. Quantum algorithms exploit the quantum phenomena of superposition, entanglement and interference to perform tasks that are hard or impossible for classical algorithms.

The following diagram illustrates the basic architecture of a quantum computer:

```
+-----------------+       +-----------------+
| Classical       |       | Quantum         |
| Computer        |       | Processor       |
|                 |       |                 |
| +-------------+ |       | +-------------+ |
| | Control     | |       | | Qubits      | |
| | Software    | |       | |             | |
| +-------------+ |       | +-------------+ |
|                 |       |                 |
| +-------------+ |       | +-------------+ |
| | Quantum     | |       | | Quantum     | |
| | Algorithm   | |       | | Gates       | |
| +-------------+ |       | |             | |
|                 |       | +-------------+ |
|                 |       |                 |
| +-------------+ |       | +-------------+ |
| | Measurement | |       | | Measurement | |
| | Software    | |       | | Devices     | |
| +-------------+ |       | |             | |
|                 |       | +-------------+ |
+-----------------+       +-----------------+
```

A quantum algorithm is usually described by a quantum circuit, which is a sequence of quantum gates that act on some input qubits and terminate with a measurement. A quantum gate is a unitary transformation that changes the state of one or more qubits. A measurement is a process that collapses the quantum state of a qubit to one of its classical values, such as 0 or 1, with some probability.

The following diagram illustrates an example of a quantum circuit:

```
+---+     +---+     +---+     +---+     +---+
| 0 | --- | H | --- | X | --- | H | --- | M |
+---+     +---+     +---+     +---+     +---+
| 0 | --- | H | --- |   | --- | H | --- | M |
+---+     +---+     | C |     +---+     +---+
| 0 | --- | H | --- | N | --- | H | --- | M |
+---+     +---+     | O |     +---+     +---+
| 0 | --- | H | --- | T | --- | H | --- | M |
+---+     +---+     +---+     +---+     +---+
```

In this circuit, the input is four qubits initialized to 0. The H gate is the Hadamard gate, which creates a superposition of 0 and 1 with equal probability. The X gate is the NOT gate, which flips the state of a qubit. The CNOT gate is the controlled-NOT gate, which flips the state of the target qubit (the bottom one) if the control qubit (the top one) is 1. The M gate is the measurement gate, which collapses the state of a qubit to 0 or 1 and outputs the result.

Quantum algorithms can be categorized by the main techniques used by the algorithm. Some commonly used techniques/ideas in quantum algorithms include phase kick-back, phase estimation, the quantum Fourier transform, quantum walks, amplitude amplification and topological quantum field theory. Some examples of quantum algorithms are:

- Shor's algorithm, which can factor large numbers in polynomial time, using the quantum Fourier transform and modular arithmetic.
- Grover's algorithm, which can search an unsorted database in quadratic speedup, using amplitude amplification and quantum oracle.
- Deutsch-Jozsa algorithm, which can determine if a function is constant or balanced in one query, using phase kick-back and superposition.
- Simon's algorithm, which can find a hidden periodicity in a function in polynomial time, using the quantum Fourier transform and linear algebra.
- Quantum error correction, which can protect quantum information from noise and decoherence, using entanglement and redundancy.