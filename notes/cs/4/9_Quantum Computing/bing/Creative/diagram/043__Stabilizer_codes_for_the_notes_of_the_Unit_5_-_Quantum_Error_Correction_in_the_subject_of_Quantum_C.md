Stabilizer codes are a subclass of quantum error-correcting codes that use a group-theoretical structure to protect quantum states from local noisy errors. They append ancilla qubits to the qubits that we want to protect and rotate the global state into a subspace of a larger Hilbert space using a unitary encoding circuit. This creates a highly entangled, encoded state that can be corrected by measuring the stabilizer generators of the code. Stabilizer codes are related to some classical binary or quaternary codes, but they must satisfy the dual-containing or self-orthogonality constraint.

The following diagram illustrates the basic architecture of a stabilizer code:

```
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Logical qubit  |    |  Logical qubit  |    |  Logical qubit  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       V                     V                     V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Ancilla qubit  |    |  Ancilla qubit  |    |  Ancilla qubit  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       |                     |                     |
       V                     V                     V
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  Physical qubit |    |  Physical qubit |    |  Physical qubit |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
```

Each logical qubit is encoded into a subspace of n physical qubits using a unitary encoding circuit. Each physical qubit is coupled to an ancilla qubit that is used to measure the stabilizer generators of the code. The measurement results are used to correct the errors on the physical qubits and recover the logical qubits. The stabilizer code can correct up to t errors on the physical qubits, where t depends on the parameters of the code. For more details on stabilizer codes and quantum error correction, please refer to the sources in the search results.