### Introduction for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Quantum error correction (QEC) is a set of techniques that aim to protect quantum information from noise, decoherence, and errors that may occur during quantum computation or communication .
- QEC is essential for achieving fault-tolerant quantum computing, which means that quantum algorithms can be executed reliably and efficiently even in the presence of imperfect hardware and noisy operations .
- QEC is different from classical error correction in several ways:
  - Quantum errors are continuous and probabilistic, not discrete and deterministic. This means that quantum errors can affect both the amplitude and the phase of a quantum state, and that they can occur with any probability between 0 and 1 .
  - Quantum errors cannot be detected or corrected directly, due to the no-cloning theorem and the no-deleting theorem. These theorems state that quantum information cannot be copied or erased without disturbing it .
  - Quantum errors can affect entangled qubits, even if they are physically separated. This means that quantum errors can propagate and correlate across a quantum system, and that they can cause decoherence and loss of quantum coherence .
- QEC relies on two main concepts: encoding and syndrome measurement  .
  - Encoding is the process of representing a logical qubit (the qubit that carries the quantum information) by a physical qubit (the qubit that interacts with the hardware and the environment) or a group of physical qubits. The encoding scheme defines how the logical qubit is mapped to the physical qubits, and how the logical operations are implemented on the physical qubits  .
  - Syndrome measurement is the process of performing a multi-qubit measurement that does not disturb the quantum information in the logical qubit, but retrieves information about the error that may have occurred on the physical qubits. The syndrome measurement can determine the occurrence, location, and type of errors, and can be used to correct them by applying appropriate recovery operations  .
- QEC codes are the specific encoding schemes and syndrome measurement protocols that are designed to correct certain types of errors. There are many types of QEC codes, such as stabilizer codes, topological codes, concatenated codes, etc. Each QEC code has its own advantages and disadvantages, such as the number of physical qubits required, the error threshold, the fault-tolerance level, the circuit depth, etc  .
- QEC can be applied to both discrete-variable systems (such as qubits) and continuous-variable systems (such as harmonic oscillators). QEC can also be combined with other techniques, such as quantum error mitigation, quantum error detection, quantum error avoidance, etc., to enhance the performance and robustness of quantum computing and communication   .

: Quantum error correction - Wikipedia
: [1907.11157] Quantum Error Correction: An Introductory Guide - arXiv.org
: [2111.08894] Introduction to Quantum Error Correction and Fault Tolerance - arXiv.org
: Quantum Error Correction, an informal introduction - users.physics.ox.ac.uk