### Stabilizer codes for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Quantum error correction (QEC) is a technique to protect quantum states from noise and decoherence by encoding them into larger Hilbert spaces and applying recovery operations when errors occur .
- Stabilizer codes are a subclass of QEC codes that are based on the stabilizer formalism, which uses a group of unitary operators (called stabilizers) to specify a subspace of the Hilbert space (called the code space) where the encoded states live  .
- Stabilizer codes have the following properties  :
  - They can be constructed from classical binary or quaternary codes that satisfy the dual-containing or self-orthogonal constraint, which means that the code space is orthogonal to its dual space under the symplectic inner product.
  - They can correct any error that commutes with all the stabilizers, and detect any error that anti-commutes with at least one stabilizer.
  - They can be efficiently encoded and decoded using classical algorithms, such as the syndrome decoding algorithm, which measures the eigenvalues of the stabilizers and determines the most likely error based on the syndrome vector.
  - They can be generalized to higher-dimensional systems (qudits) and entanglement-assisted schemes, which use preshared entangled states to improve the error correction capability.
- Examples of stabilizer codes include the Shor code, the Steane code, the CSS code, the toric code, and the surface code  .