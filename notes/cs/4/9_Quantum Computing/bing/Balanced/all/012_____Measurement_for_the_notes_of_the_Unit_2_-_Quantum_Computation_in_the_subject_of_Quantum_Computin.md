# Measurement for the notes of the Unit 2 - Quantum Computation in the subject of Quantum Computing

- Measurement is a fundamental process in quantum mechanics that reveals the properties of a quantum system, such as its state, energy, spin, etc.
- Measurement can also be used as a tool for quantum computation, where the outcome of a measurement can determine the next step of the computation.
- Measurement-based quantum computation (MBQC) is a framework of quantum computation, where entanglement is used as a resource and local measurements on qubits are used to drive the computation .
- The standard process of MBQC consists of three steps:
  - Entangle the qubits, forming a cluster state that serves as the source state for the computation.
  - Measure the ancillae (auxiliary qubits) in a specific order and basis, depending on the desired computation. The measurement outcomes are used to adjust the basis of the subsequent measurements.
  - Correct the outputs by applying classical post-processing on the final measurement outcomes, using the information from the previous measurements.
- MBQC is equivalent to the circuit model of quantum computation in terms of computational power, but it has some advantages, such as:
  - It reduces the need for quantum gates and quantum memory, as the computation is performed by measurements only.
  - It allows for parallelism and fault-tolerance, as the cluster state can be prepared in advance and the measurements can be done independently and locally.
  - It enables novel applications, such as blind quantum computation, where the user can delegate the computation to a server without revealing the input, output, or algorithm .