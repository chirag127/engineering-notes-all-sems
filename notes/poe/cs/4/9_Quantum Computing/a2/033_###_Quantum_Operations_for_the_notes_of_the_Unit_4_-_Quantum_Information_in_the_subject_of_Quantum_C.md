 Here is the content in markdown format for the topic ### Quantum Operations for the notes of the Unit 4 - Quantum Information in the subject of Quantum Computing:

### Quantum Operations for the notes of the Unit 4 - Quantum Information in the subject of Quantum Computing

The quantum operations that can be performed on quantum bits (qubits) are:

1. Initialization: Setting a qubit to a known initial state (usually $\lvert{0}\rangle$).
2. Measurements: Measuring the state of a qubit by observing its quantum properties. This operation collapses the superposition state of the qubit into a definite classical state.
3. Manipulations: Performing operations on qubits to create and transform entanglement and superposition. These include:

- Rotations: Applying unitary transformations that rotate the state vector in the Bloch sphere. Examples are rotations about X, Y and Z axes (Rx, Ry and Rz respectively).
- Controlled-NOT (CNOT) gate: A 2-qubit gate that flips the target qubit if the control qubit is $\lvert{1}\rangle$. It is used to create entanglement.
- Hadamard gate: A single-qubit gate that puts the qubit into an equal superposition state of $\lvert{0}\rangle$ and $\lvert{1}\rangle$ (i.e. $(|0\rangle + |1\rangle)/\sqrt{2}$). It is used at the start of many quantum algorithms like quantum Fourier transform.

Mnemonics and learning tricks:

- Think of initialization as setting the initial 'input' to the qubit.
- Measurements 'output' either 0 or 1 and collapse superposition.
- Rotations rotate the Bloch sphere, CNOT flips target qubit based on control qubit and Hadamard creates equal superposition.

The operations can be represented using quantum logic gates and matrices in quantum circuits. They are used to build quantum algorithms like quantum Fourier transform and Shor's algorithm. The operations can have applications in quantum machine learning, quantum cryptography, quantum error correction, etc.