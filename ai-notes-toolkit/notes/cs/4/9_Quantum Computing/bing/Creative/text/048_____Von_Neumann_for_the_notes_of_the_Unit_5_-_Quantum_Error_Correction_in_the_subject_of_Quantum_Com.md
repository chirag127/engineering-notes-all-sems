### Von Neumann quantum error correction

- Quantum error correction (QEC) is used in quantum computing to protect quantum information from errors due to decoherence and other quantum noise.
- QEC is theorised as essential to achieve fault tolerant quantum computing that can reduce the effects of noise on stored quantum information, faulty quantum gates, faulty quantum measurements, and faulty quantum preparation.
- The problem of noise occurring in classical computation was considered by von Neumann in the 1950s.
- Von Neumann proposed a method of error correction using redundancy, where each bit of information is encoded into multiple bits, and a majority vote is used to correct errors.
- However, this method does not work for quantum information, because quantum states cannot be copied or measured without disturbing them, due to the no-cloning theorem and the measurement postulate.
- Therefore, QEC requires a different approach, where quantum information is encoded into entangled states of multiple qubits, and non-destructive measurements are performed on error syndromes, which are combinations of qubits that reveal the type and location of errors without revealing the encoded information .
- QEC schemes can be classified into two types: discrete and continuous .
- Discrete QEC schemes use projective von Neumann measurements on stabilizers to discretize the error syndromes into a finite set, and fast unitary gates are applied to recover the corrupted information .
- Continuous QEC schemes use weak measurements or homodyne detection to estimate the error syndromes continuously, and feedback control is applied to correct the errors in real time .
- QEC schemes can also be classified into two types: active and passive.
- Active QEC schemes require periodic measurements and corrections to maintain the encoded information.
- Passive QEC schemes use error-detecting codes or decoherence-free subspaces to avoid measurements and corrections, but they are more limited in the types of errors they can correct.