# Von Neumann Quantum Error Correction

- Quantum error correction (QEC) is used in quantum computing to protect quantum information from errors due to decoherence and other quantum noise.
- QEC is theorised as essential to achieve fault tolerant quantum computing that can reduce the effects of noise on stored quantum information, faulty quantum gates, faulty quantum measurements, and faulty quantum preparation.
- The problem of noise occurring in classical computation was considered by von Neumann in the 1950s.
- Von Neumann proposed a method of error correction using redundancy, where each bit of information is encoded into multiple bits, and a majority vote is used to correct errors.
- However, this method does not work for quantum information, because quantum bits (qubits) cannot be copied or measured without disturbing their state due to the no-cloning theorem and the measurement postulate.
- Therefore, QEC requires a different approach, where quantum information is encoded into entangled states of multiple qubits, and errors are detected and corrected by performing non-destructive measurements on stabilizer operators .
- Stabilizer operators are tensor products of Pauli matrices that commute with the encoded state and have eigenvalue +1 on it.
- By measuring the stabilizer operators, one can obtain the error syndrome, which is a binary string that indicates the type and location of errors that have occurred on the qubits.
- The error syndrome can then be used to apply the appropriate recovery operation, which is a unitary transformation that reverses the effect of the errors and restores the encoded state.
- However, measuring the stabilizer operators directly may not be feasible in some physical implementations of quantum computing, where the measurement process itself may introduce errors .
- In such cases, one can use a measurement-based estimator scheme, where the stabilizer operators are measured indirectly by using ancillary qubits and entangling gates .
- The measurement-based estimator scheme can achieve continuous quantum error correction, where the errors are corrected as soon as they are detected, without waiting for the end of the computation .
- The measurement-based estimator scheme can also reduce the overhead of QEC, by using fewer ancillary qubits and gates, and by exploiting the correlations between different stabilizer operators .