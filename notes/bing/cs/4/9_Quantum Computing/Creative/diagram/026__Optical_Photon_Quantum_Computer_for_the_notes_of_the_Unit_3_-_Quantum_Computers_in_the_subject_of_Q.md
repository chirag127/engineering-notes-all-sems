The following diagram illustrates the basic architecture of a linear optical quantum computer, which is one of the paradigms of optical photon quantum computing. It uses photons as qubits, linear optical elements such as beam splitters, phase shifters, and mirrors as quantum gates, and single photon detectors and quantum memories as measurement and storage devices .

```
+----------------+    +----------------+    +----------------+
| Single photon  |    | Linear optical |    | Single photon  |
| source         |    | element        |    | detector       |
|                |    |                |    |                |
|                |    |                |    |                |
|                |    |                |    |                |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
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
       v                     v                     v
+----------------+    +----------------+    +----------------+
| Quantum memory |    | Quantum memory |    | Quantum memory |
|                |    |                |    |                |
|                |    |                |    |                |
|                |    |                |    |                |
|                |    |                |    |                |
+----------------+    +----------------+    +----------------+
```

The single photon source generates a photon with a specific polarization, which encodes the qubit state. The linear optical element performs a unitary transformation on the photon's polarization, which implements a quantum gate. The single photon detector measures the photon's polarization, which collapses the qubit state. The quantum memory stores the qubit state for later use or manipulation .

There are different types of linear optical elements, such as polarizing beam splitters, half-wave plates, and Mach-Zehnder interferometers, that can perform different quantum gates on the photons. Some of the common quantum gates are the Hadamard gate, the phase gate, the Pauli-X gate, and the controlled-NOT gate.

The main challenge of linear optical quantum computing is that it requires a large number of photons and optical elements to perform complex quantum algorithms, and the probability of success decreases exponentially with the number of qubits. Therefore, some techniques such as quantum teleportation, quantum error correction, and quantum repeaters are needed to improve the scalability and reliability of optical photon quantum computing  .