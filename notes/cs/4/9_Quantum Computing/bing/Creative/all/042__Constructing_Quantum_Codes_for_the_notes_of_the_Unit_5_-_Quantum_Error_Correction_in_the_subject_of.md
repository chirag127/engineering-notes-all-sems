### Constructing Quantum Codes for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

Quantum codes are methods of encoding quantum information in such a way that errors due to noise or decoherence can be detected and corrected. Quantum codes are essential for quantum information processing and quantum computation, as quantum systems are very sensitive to disturbances from the environment.

There are several ways of constructing quantum codes from classical codes, which are methods of encoding classical information (such as bits) in such a way that errors due to noise or interference can be detected and corrected. Classical codes have been extensively studied in the field of information theory and coding theory, and many examples of good classical codes are known.

One of the most common ways of constructing quantum codes from classical codes is the CSS construction, named after Calderbank, Shor and Steane, who independently discovered it in 1996 . The CSS construction takes two classical linear codes, C1 and C2, that satisfy a certain self-orthogonality condition, and produces a quantum code Q that can correct both bit-flip and phase-flip errors. The CSS construction is general and can be applied to any pair of classical linear codes that meet the self-orthogonality condition. Some examples of quantum codes obtained by the CSS construction are:

- The Shor code, which is a 9-qubit code that can correct any single-qubit error, obtained from the classical repetition code of length 9.
- The Steane code, which is a 7-qubit code that can correct any single-qubit error, obtained from the classical Hamming code of length 7.
- The quantum Reed-Muller codes, which are quantum codes that can correct multiple errors, obtained from the classical Reed-Muller codes of various lengths and orders.

Another way of constructing quantum codes from classical codes is the Hermitian construction, which is a generalization of the CSS construction that allows the use of non-linear or non-self-orthogonal classical codes. The Hermitian construction takes a classical code C over a finite field GF(q^2^) that is Hermitian self-orthogonal, meaning that the inner product of any two codewords is zero when conjugated by the Frobenius automorphism. The Hermitian construction then produces a quantum code Q over GF(q) that can correct both bit-flip and phase-flip errors. The Hermitian construction can produce quantum codes with better parameters than the CSS construction, such as quantum MDS codes, which are quantum codes that have the maximum possible distance for a given length and dimension.

A third way of constructing quantum codes from classical codes is the polynomial construction, which is a generalization of the Hermitian construction that allows the use of codes over polynomial rings. The polynomial construction takes a classical code C over a ring R that is skew-Hermitian self-orthogonal, meaning that the inner product of any two codewords is zero when conjugated by a skew-Frobenius automorphism. The polynomial construction then produces a quantum code Q over a subring of R that can correct both bit-flip and phase-flip errors. The polynomial construction can produce quantum codes with better parameters than the Hermitian construction, such as quantum codes with linear distance and constant rate.

Some mnemonics and learning tricks for constructing quantum codes are:

- Remember that the CSS construction is based on the idea of encoding the bit-flip and phase-flip information separately using two classical linear codes that are self-orthogonal.
- Remember that the Hermitian construction is based on the idea of encoding the bit-flip and phase-flip information together using a classical code over a quadratic extension field that is Hermitian self-orthogonal.
- Remember that the polynomial construction is based on the idea of encoding the bit-flip and phase-flip information together using a classical code over a polynomial ring that is skew-Hermitian self-orthogonal.
- Remember that the distance of a quantum code is the minimum weight of a non-trivial logical operator that can cause an error on the encoded quantum information.
- Remember that the rate of a quantum code is the ratio of the number of logical qubits to the number of physical qubits used to encode them.