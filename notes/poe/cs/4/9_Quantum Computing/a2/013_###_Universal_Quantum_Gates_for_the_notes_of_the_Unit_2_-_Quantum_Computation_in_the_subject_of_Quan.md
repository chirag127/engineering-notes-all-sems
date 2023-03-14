 Here is the content in markdown format for the given topic:

### Universal Quantum Gates for the notes of the Unit 2 - Quantum Computation in the subject of Quantum Computing

The following are the key Universal Quantum Gates required to build any quantum circuit:

1. Hadamard Gate (H): It puts a qubit into a superposition state. It performs a rotation of the qubit state vector by π/2 around the X-axis.
Mnemonic: Think of H as Half the rotation around X-axis.

2. Pauli X Gate (X): It flips the qubit state. It performs a rotation of the qubit state vector by π around the X-axis.
Mnemonic: Think of X as eXchanging the X and Z components of the state vector.

3. Pauli Z Gate (Z): It flips the qubit state if and only if the qubit is in state |1>. It performs a rotation of the qubit state vector by π around the Z-axis.
Mnemonic: Think of Z as doing nothing to the X-component but inverting the Z-component of the state vector.

4. Phase Shift Gate (S): It induces a phase shift of π/2 if and only if the qubit is in state |1>. It performs a rotation of the qubit state vector by π/2 around the Z-axis.
Mnemonic: Think of S as inducing a Shift in the phase of the qubit state by π/2.

5. Controlled NOT (CNOT) Gate: It flips the target qubit if and only if the control qubit is in state |1>. It is a 2-qubit gate that performs an X operation on the target qubit if and only if the control qubit is in state |1>.
Mnemonic: Think of CNOT as Conditionally doing NOT on the target qubit based on the state of the control qubit.

The above 5 gates are sufficient to build any quantum circuit. They form a 'universal gate set' as any quantum operation on 1 or 2 qubits can be implemented using just these gates.

Detailed diagrams, examples, applications, advantages, and disadvantages of the universal quantum gates can be added if required. Learning tricks and mnemonics can be included if easy to remember. The content can be made more formal by using appropriate technical terms and phrases.