# Measurement for the notes of the Unit 2 - Quantum Computation in the subject of Quantum Computing

- Measurement is a fundamental operation in quantum computation, where the state of a quantum system is observed and recorded.
- Measurement can also be used to manipulate and control quantum systems, by exploiting the effects of entanglement and superposition.
- Measurement-based quantum computation (MBQC) is a framework of quantum computation, where entanglement is used as a resource and local measurements on qubits are used to drive the computation .
- MBQC can be seen as a generalization of the one-way quantum computer, where a large entangled state, called a cluster state, is prepared and then measured in a specific order and basis to perform a desired quantum algorithm .
- The standard process of MBQC consists of three steps: entangle the qubits, measure the ancillae (auxiliary qubits) and correct the outputs.
- In the first step, the qubits are entangled in order to prepare the source state, which can be a cluster state or a more general graph state.
- In the second step, the ancillae qubits are measured in a certain order and basis, which depends on the input, the desired output and the previous measurement outcomes. The measurement outcomes are used to update the measurement bases for the remaining qubits.
- In the third step, the outputs are corrected by applying classical operations, such as bit flips or phase flips, based on the measurement outcomes of the ancillae qubits.
- MBQC is equivalent to the quantum circuit model in terms of computational power, but it offers some advantages, such as reduced communication complexity, fault-tolerance and parallelism  .
- MBQC also reveals some interesting connections between quantum computation, entanglement theory and graph theory .