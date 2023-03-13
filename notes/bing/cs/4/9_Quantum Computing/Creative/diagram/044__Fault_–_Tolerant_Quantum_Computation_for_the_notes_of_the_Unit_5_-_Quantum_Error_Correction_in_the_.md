Fault-tolerant quantum computation is a technique to protect quantum information from errors that arise due to decoherence, noise, or imperfect operations. It involves encoding quantum information into logical qubits that are more robust than physical qubits, and applying quantum error correction schemes to detect and correct errors. The quantum threshold theorem states that if the physical error rate is below a certain threshold, the logical error rate can be made arbitrarily low.

The following diagram illustrates the basic architecture of a fault-tolerant quantum computation system:

```
+-----------------+    +-----------------+    +-----------------+
| Logical qubits  |    | Logical qubits  |    | Logical qubits  |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  +-----------+  |    |  +-----------+  |    |  +-----------+  |
|  | Encoding  |  |    |  | Encoding  |  |    |  | Encoding  |  |
|  +-----------+  |    |  +-----------+  |    |  +-----------+  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  +-----------+  |    |  +-----------+  |    |  +-----------+  |
|  | Physical  |  |    |  | Physical  |  |    |  | Physical  |  |
|  | qubits    |  |    |  | qubits    |  |    |  | qubits    |  |
|  +-----------+  |    |  +-----------+  |    |  +-----------+  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  +-----------+  |    |  +-----------+  |    |  +-----------+  |
|  | Quantum   |  |    |  | Quantum   |  |    |  | Quantum   |  |
|  | operations|  |    |  | operations|  |    |  | operations|  |
|  +-----------+  |    |  +-----------+  |    |  +-----------+  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  +-----------+  |    |  +-----------+  |    |  +-----------+  |
|  | Error     |  |    |  | Error     |  |    |  | Error     |  |
|  | detection |  |    |  | detection |  |    |  | detection |  |
|  +-----------+  |    |  +-----------+  |    |  +-----------+  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  +-----------+  |    |  +-----------+  |    |  +-----------+  |
|  | Error     |  |    |  | Error     |  |    |  | Error     |  |
|  | correction|  |    |  | correction|  |    |  | correction|  |
|  +-----------+  |    |  +-----------+  |    |  +-----------+  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
|                 |    |                 |    |                 |
|  +-----------+  |    |  +-----------+  |    |  +-----------+  |
|  | Decoding  |  |    |  | Decoding  |  |    |  | Decoding  |  |
|  +-----------+  |    |  +-----------+  |    |  +-----------+  |
|                 |    |                 |    |                 |
+-----------------+    +-----------------+    +-----------------+
| Logical qubits  |    | Logical qubits  |    | Logical qubits  |
+-----------------+    +-----------------+    +-----------------+
```

The system consists of several logical qubits, each