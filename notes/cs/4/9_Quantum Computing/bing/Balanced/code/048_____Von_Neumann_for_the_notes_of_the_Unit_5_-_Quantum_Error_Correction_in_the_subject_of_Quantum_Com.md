# Von Neumann quantum error correction

- Quantum error correction (QEC) is used in quantum computing to protect quantum information from errors due to decoherence and other quantum noise.
- QEC is essential to achieve fault tolerant quantum computing that can reduce the effects of noise on stored quantum information, faulty quantum gates, faulty quantum measurements, and faulty quantum preparation.
- The problem of noise occurring in classical computation was considered by von Neumann in the 1950s. He proposed a method of encoding classical bits into redundant bits and using majority voting to correct errors.
- However, this method does not work for quantum bits (qubits) because of the no-cloning theorem, which states that an arbitrary quantum state cannot be copied exactly.
- Therefore, QEC requires a different approach that exploits the properties of quantum entanglement and superposition.
- One of the main approaches to QEC is based on stabilizer codes, which are a class of quantum codes that use projective von Neumann measurements on stabilizers to discretize the error syndromes into a finite set .
- A stabilizer is a set of commuting operators that leave the code subspace invariant. A stabilizer code encodes k logical qubits into n physical qubits, where n > k, and can correct errors up to a certain weight.
- A projective von Neumann measurement on a stabilizer operator can reveal the presence or absence of an error without disturbing the encoded quantum information.
- By measuring a set of stabilizer operators, one can obtain a syndrome that indicates the type and location of the error.
- Then, a recovery operation can be applied to correct the error and restore the quantum information.
- An example of a stabilizer code is the Shor code, which encodes one logical qubit into nine physical qubits and can correct any single-qubit error.
- Another example is the Steane code, which encodes one logical qubit into seven physical qubits and can correct any single-qubit error or any single-qubit phase error.
- There are also other types of QEC codes, such as topological codes, surface codes, and concatenated codes, that have different advantages and disadvantages.
- QEC is a very active and important area of research in quantum computing, as it is crucial for achieving scalable and reliable quantum computation.