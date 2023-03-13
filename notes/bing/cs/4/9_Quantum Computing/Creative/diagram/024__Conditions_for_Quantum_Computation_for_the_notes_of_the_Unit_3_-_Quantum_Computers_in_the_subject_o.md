The following is a detailed ASCII diagram for the conditions for quantum computation for the notes of the Unit 3 - Quantum Computers in the subject of Quantum Computing.

### Conditions for Quantum Computation

According to DiVincenzo's criteria, there are five conditions necessary for quantum computation:

1. A scalable physical system with well-characterized qubits
2. The ability to initialize the state of the qubits to a simple fiducial state
3. Long relevant decoherence times
4. A "universal" set of quantum gates
5. A qubit-specific measurement capability

The diagram below illustrates these conditions using a simple example of a quantum circuit with two qubits.

```
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|  Qubit 1        |  Qubit 2        |  Qubit 1        |  Qubit 2        |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|  |0>            |  |0>            |  |+>            |  |0>            |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|  Initialization |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|  H              |                 |                 |                 |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|  Qubit 1        |  Qubit 2        |  Qubit 1        |  Qubit 2        |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|  |+>            |  |0>            |  |+>            |  |->            |
|                 |                 |                 |                 |
+-----------------+-----------------+-----------------+-----------------+
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|                 |                 |                 |                 |
|  Quantum Gate   |                 |                 |                 |
|                 |                 |                 |                 |
|                 |  H              |                 |                 |
|                 |                 |                 |                 |