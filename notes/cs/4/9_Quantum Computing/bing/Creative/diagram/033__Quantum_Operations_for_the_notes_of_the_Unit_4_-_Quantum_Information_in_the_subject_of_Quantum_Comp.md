Quantum operations are transformations that a quantum mechanical system can undergo. They can be used to manipulate quantum bits (qubits) in a quantum circuit. Quantum operations can be unitary or non-unitary, depending on whether they preserve the norm of the quantum state or not. Unitary operations are reversible and can be represented by unitary matrices. Non-unitary operations are irreversible and can be represented by Kraus operators or superoperators. Quantum operations can also be classified as completely positive (CP) or non-completely positive (NCP), depending on whether they preserve the positivity of the quantum state or not. CP operations are physical and can be realized by coupling the system to an environment and tracing out the environment. NCP operations are unphysical and cannot be realized by any physical process.

The following diagram illustrates the basic architecture of a quantum operation:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Quantum state  |     | Quantum state   |     | Quantum state   |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|      rho        |---->|  E(rho)         |---->|  rho'           |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Density matrix |     | Quantum operation|    | Density matrix  |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

A quantum operation E takes a quantum state rho as input and produces a quantum state rho' as output. The quantum state can be represented by a density matrix, which is a positive semi-definite matrix with trace one. A quantum operation can be represented by a linear map, a matrix, or a set of operators, depending on the type of operation. Some examples of quantum operations are:

- Identity operation: E(rho) = rho. This operation does nothing to the quantum state. It is unitary, CP, and trace-preserving.
- Bit-flip operation: E(rho) = X rho X, where X is the Pauli-X matrix. This operation flips the qubit from 0 to 1 or vice versa. It is unitary, CP, and trace-preserving.
- Measurement operation: E(rho) = sum_k M_k rho M_k^dagger, where M_k are the measurement operators. This operation collapses the quantum state to one of the measurement outcomes with some probability. It is non-unitary, CP, and trace-reducing.
- Depolarizing operation: E(rho) = (1-p) rho + p I/2, where p is the depolarizing probability and I is the identity matrix. This operation introduces noise to the quantum state and makes it more mixed. It is non-unitary, CP, and trace-preserving.