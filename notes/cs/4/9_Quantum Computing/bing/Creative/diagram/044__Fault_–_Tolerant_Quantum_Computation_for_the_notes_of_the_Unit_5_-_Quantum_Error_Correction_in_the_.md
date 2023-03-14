The following diagram illustrates the basic architecture of a fault-tolerant quantum computation  :

```
+-----------------+   +-----------------+   +-----------------+
| Logical qubits  |   | Logical qubits  |   | Logical qubits  |
| encoded in      |   | encoded in      |   | encoded in      |
| physical qubits |   | physical qubits |   | physical qubits |
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|  Error          |   |  Error          |   |  Error          |
|  correction     |   |  correction     |   |  correction     |
|  circuit        |   |  circuit        |   |  circuit        |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|  Logical        |   |  Logical        |   |  Logical        |
|  gate           |   |  gate           |   |  gate           |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|  Transversal    |   |  Transversal    |   |  Transversal    |
|  gate           |   |  gate           |   |  gate           |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|  Physical       |   |  Physical       |   |  Physical       |
|  gate           |   |  gate           |   |  gate           |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|  Physical       |   |  Physical       |   |  Physical       |
|  qubits         |   |  qubits         |   |  qubits         |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
```

The diagram shows how logical qubits are encoded in physical qubits using quantum error correction codes. The error correction circuit detects and corrects errors that occur in the physical qubits due to noise or imperfect control. The logical gate performs a quantum operation on the logical qubits, which can be implemented by a transversal gate that applies the same physical gate to each physical qubit in the code block. The physical gate performs a quantum operation on the physical qubits, which can be subject to errors. The fault-tolerant quantum computation can achieve arbitrarily low logical error rates, as long as the physical error rate is below a certain threshold.