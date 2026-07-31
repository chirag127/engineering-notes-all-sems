# Von Neumann quantum error correction

- Quantum error correction (QEC) is used in quantum computing to protect quantum information from errors due to decoherence and other quantum noise.
- QEC is theorised as essential to achieve fault tolerant quantum computing that can reduce the effects of noise on stored quantum information, faulty quantum gates, faulty quantum measurements, and faulty quantum preparation.
- The problem of noise occurring in classical computation was considered by von Neumann in the 1950s.
- Von Neumann proposed a method of error correction using redundancy, where each bit of information is encoded into multiple bits, and a majority vote is used to correct errors.
- However, this method cannot be directly applied to quantum information, because of the no-cloning theorem and the measurement disturbance.
- Instead, QEC uses quantum codes, which are subspaces of the Hilbert space of a quantum system, where each logical quantum state is encoded into multiple physical qubits.
- QEC also uses quantum measurements, which are projections onto the orthogonal subspaces of the Hilbert space, to detect and correct errors without disturbing the encoded information.
- QEC can be classified into discrete QEC and continuous QEC, depending on the type of errors and measurements involved .
- Discrete QEC schemes use projective von Neumann measurements on stabilizers to discretize the error syndromes into a finite set, and fast unitary gates are applied to recover the corrupted information .
- Continuous QEC schemes use non-projective measurements on continuous variables to estimate the error syndromes in a continuous range, and feedback control is applied to correct the errors in real time .
- QEC can also be classified into active QEC and passive QEC, depending on the frequency and timing of the error correction procedures.
- Active QEC schemes require frequent measurements and corrections to keep the errors below a certain threshold.
- Passive QEC schemes rely on the natural dynamics of the quantum system to suppress the errors without active intervention.
- QEC can be implemented using various physical platforms, such as superconducting qubits, trapped ions, photonic qubits, and spin qubits.
- QEC is a challenging and active area of research in quantum computing, as it involves trade-offs between the complexity, efficiency, and reliability of the quantum codes and the error correction protocols.