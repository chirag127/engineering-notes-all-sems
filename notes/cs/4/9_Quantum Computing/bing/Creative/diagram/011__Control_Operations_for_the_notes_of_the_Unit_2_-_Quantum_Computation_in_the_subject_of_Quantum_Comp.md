Control operations are operations that manipulate the quantum state of one or more qubits in a quantum circuit. They can be either unitary or non-unitary, depending on whether they preserve the norm of the quantum state or not. Unitary operations include quantum gates, such as the Hadamard gate, the Pauli gates, the CNOT gate, and the phase gates. Non-unitary operations include measurement, reset, and conditional operations. Control operations can be implemented by applying classical or quantum control fields to the qubits, such as electric, magnetic, or electromagnetic fields. Quantum optimal control is a branch of quantum control that aims to design the best control fields for a given task, such as implementing a desired quantum operation with minimum energy consumption and maximum robustness.

The following diagram illustrates the basic architecture of a quantum control system:

```
+----------------+    +----------------+    +----------------+
| Classical      |    | Quantum        |    | Classical      |
| Computer       |    | Processor      |    | Measurement    |
|                |    |                |    | Device         |
|                |    |                |    |                |
|                |    |                |    |                |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      +---------------------->                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      +----------------------+
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      <----------------------+                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |                      |
      |                      |