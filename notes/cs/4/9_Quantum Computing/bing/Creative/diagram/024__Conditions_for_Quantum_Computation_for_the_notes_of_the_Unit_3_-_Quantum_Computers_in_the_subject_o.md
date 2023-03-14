The conditions for quantum computation are also known as DiVincenzo's criteria, which are seven requirements that a physical system must satisfy to implement quantum algorithms and communication. The first five criteria are for quantum computation, and the last two are for quantum communication. They are:

1. A scalable physical system with well-characterized qubits
2. The ability to initialize the state of the qubits to a simple fiducial state
3. Long relevant decoherence times
4. A "universal" set of quantum gates
5. A qubit-specific measurement capability
6. Interconverting stationary and flying qubits and faithfully transmitting flying qubits between specified locations
7. The ability to interconvert stationary and flying qubits

A possible ASCII diagram for these criteria is:

```
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
|  Scalable and   |     |  Initialization |     |   Decoherence   |
|  well-defined   |     |    of qubits    |     |     times       |
|     qubits      |     |                 |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
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
         V                      V                      V
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
| Universal gates |     |  Measurement    |     |  Flying qubits  |
|                 |     |    of qubits    |     |                 |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
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
         V                      V                      V
+-----------------+     +-----------------+     +-----------------+
|                 |     |                 |     |                 |
| Interconversion |     |  Transmission   |     | Interconversion |
|  of qubits      |     |    of qubits    |     |  of qubits      |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
```