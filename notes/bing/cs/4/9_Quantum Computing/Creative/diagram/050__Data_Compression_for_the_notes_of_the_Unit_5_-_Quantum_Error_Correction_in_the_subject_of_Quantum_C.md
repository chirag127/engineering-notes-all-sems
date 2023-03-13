### Data Compression for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

Quantum error correction (QEC) is a set of methods to protect quantum information from unwanted environmental interactions and other forms of noise. The information is stored in a quantum error-correcting code, which is a subspace in a larger Hilbert space. QEC protocols will play a central role in the realisation of quantum computing, as they will influence the full quantum computing stack, from the layout of qubits at the physical level to gate compilation strategies at the software level.

The core idea of QEC is to make a logical qubit by distributing its quantum state across many physical data qubits. When a physical error occurs, one can detect it by repeatedly checking certain properties of the qubits, allowing it to be corrected, preventing any error from occurring on the logical qubit state.

The following diagram illustrates the basic architecture of a QEC protocol:

```
+-----------------+   +-----------------+   +-----------------+
| Logical qubit   |   | Logical qubit   |   | Logical qubit   |
| (encoded state) |   | (encoded state) |   | (encoded state) |
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
| Data qubits     |   | Data qubits     |   | Data qubits     |
| (physical qubits|   | (physical qubits|   | (physical qubits|
| storing the     |   | storing the     |   | storing the     |
| encoded state)  |   | encoded state)  |   | encoded state)  |
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
| Ancilla qubits  |   | Ancilla qubits  |   | Ancilla qubits  |
| (auxiliary      |   | (auxiliary      |   | (auxiliary      |
| qubits for      |   | qubits for      |   | qubits for      |
| error detection)|   | error detection)|   | error detection)|
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
| Classical       |   | Classical       |   | Classical       |
| controller      |   | controller      |   | controller      |
| (performs error |   | (performs error |   | (performs error |
| detection and   |   | detection and   |   | detection and   |
| correction      |   | correction      |   | correction      |
| based on the    |   | based on the    |   | based on the    |
| ancilla qubits) |   | ancilla qubits) |   | ancilla qubits) |
+-----------------+   +-----------------+   +-----------------+
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
|                 |   |                 |   |                 |
+-----------------+   +-----------------+   +-----------------+
| Quantum channel |   | Quantum channel |   | Quantum channel |
| (noisy medium   |   |