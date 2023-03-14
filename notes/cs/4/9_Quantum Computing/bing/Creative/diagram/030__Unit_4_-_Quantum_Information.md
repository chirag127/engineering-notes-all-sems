## Unit 4 - Quantum Information

Quantum information is the study of how quantum physics and computing theory can be combined to create new ways of processing and transmitting information. Quantum information breaks the rules of classical information in a way that could allow us to answer questions that a classical computer cannot.

The fundamental object of quantum information is the qubit (quantum bit), which can have a value that is either 0, 1 or a quantum superposition of 0 and 1. The state of a single qubit can be described by a two-dimensional column vector of unit norm, that is, the magnitude squared of its entries must sum to 1. This vector, called the quantum state vector, holds all the information needed to describe the one-qubit quantum system.

The following diagram illustrates the basic architecture of a quantum information system:

```
+----------------+     +----------------+     +----------------+
| Classical      |     | Quantum        |     | Classical      |
| Information    |     | Information    |     | Information    |
| Source         |     | Processor      |     | Sink           |
| (e.g. keyboard)|     | (e.g. qubits)  |     | (e.g. screen)  |
+----------------+     +----------------+     +----------------+
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
+----------------+     +----------------+     +----------------+
| Classical      |     | Quantum        |     | Classical      |
| Encoder        |     | Channel        |     | Decoder        |
| (e.g. encoder) |     | (e.g. photons) |     | (e.g. detector)|
+----------------+     +----------------+     +----------------+
```

The classical information source generates some classical information, such as a text or an image, that needs to be processed or transmitted. The classical encoder converts the classical information into quantum information, such as a sequence of qubits, that can be manipulated by quantum operations. The quantum channel is the medium that carries the quantum information from the encoder to the processor or from the processor to the decoder. The quantum processor is the device that performs quantum operations on the quantum information, such as quantum logic gates or quantum algorithms. The classical decoder converts the quantum information back into classical information, such as a measurement outcome or a result, that can be displayed or stored by the classical information sink.