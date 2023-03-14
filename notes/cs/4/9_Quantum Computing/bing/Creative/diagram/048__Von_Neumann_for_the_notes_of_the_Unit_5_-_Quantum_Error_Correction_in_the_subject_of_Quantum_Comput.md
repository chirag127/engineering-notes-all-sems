The following diagram illustrates the basic architecture of a quantum von Neumann machine, based on the paper by M. F. Brandl. It consists of a quantum central processing unit (QCPU) that executes quantum logic gates on qubits, a quantum random access memory (QRAM) that stores qubits, and a classical control unit (CCU) that provides instructions and feedback. The QCPU and the QRAM are connected by a quantum bus (QBUS) that allows the transfer of quantum information. The QRAM is divided into different regions, such as the computation region (CR), the memory region (MR), and the zeroing region (ZR), each with different functionalities and hardware requirements. The QCPU can also perform measurements on qubits and send the results to the CCU via a classical bus (CBUS).

```
+-----------------+     +-----------------+
|                 |     |                 |
|   Classical     |     |   Quantum       |
|   Control       |     |   Central       |
|   Unit (CCU)    |     |   Processing    |
|                 |     |   Unit (QCPU)   |
|                 |     |                 |
+-----------------+     +-----------------+
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  | CBUS                |  | QBUS
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
+-----------------+     +-----------------+
|                 |     |                 |
|   Quantum       |     |   Quantum       |
|   Random        |     |   Random        |
|   Access        |     |   Access        |
|   Memory        |     |   Memory        |
|   (QRAM)        |     |   (QRAM)        |
|                 |     |                 |
|                 |     |                 |
|                 |     |                 |
|                 |     |                 |
|                 |     |                 |
|                 |     |                 |
|                 |     |                 |
|                 |     |                 |
|                 |     |                 |
|                 |     |                 |
|                 |     |                 |
|                 |     |                 |
+-----------------+     +-----------------+
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
      |  | CBUS                |  | QBUS
      |  |                     |  |
      |  |                     |  |
      |  |                     |  |
+-----------------+     +-----------------+
|                 |     |                 |
|   Quantum       |     |   Quantum       |
|   Random        |     |   Random        |
|   Access        |     |   Access        |
|   Memory        |     |   Memory        |
|   (QRAM)        |     |   (QRAM)        |
|                 |     |                 |
|                 |     |                 |
|                 |     |                 |
|                 |     |                 |
|                 |     |                 |
|   CR            |     |   MR            |
|                 |     |