### Shor code for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Quantum error correction (QEC) is used in quantum computing to protect quantum information from errors due to decoherence and other quantum noise.
- A quantum error-correcting code is defined to be a unitary mapping (encoding) of k qubits into a subspace of the quantum state space of n qubits such that if any t of the qubits undergo arbitrary decoherence, not necessarily independently, the resulting n qubits can be used to faithfully reconstruct the original quantum state of the k encoded qubits .
- Peter Shor first discovered this method of formulating a quantum error correcting code by storing the information of one qubit onto a highly entangled state of nine qubits. This code is called the Shor code or the 9-qubit code.
- The Shor code can correct any single-qubit error, whether it is a bit flip, a phase flip, or a combination of both.
- The Shor code works by using three repetitions of the 3-qubit bit flip code and three repetitions of the 3-qubit phase flip code, which are concatenated together.
- The 3-qubit bit flip code encodes a single qubit |ψ⟩ = α|0⟩ + β|1⟩ as |ψ⟩|ψ⟩|ψ⟩, and uses two ancilla qubits to measure the parity of the first and second qubits, and the parity of the second and third qubits. If an error occurs on any of the qubits, the parity measurements will reveal which qubit is corrupted, and a bit flip correction can be applied.
- The 3-qubit phase flip code encodes a single qubit |ψ⟩ = α|0⟩ + β|1⟩ as |ψ⟩|ψ⟩|ψ⟩, but in the Hadamard basis, i.e., |0⟩ + |1⟩ and |0⟩ - |1⟩. It also uses two ancilla qubits to measure the parity of the first and second qubits, and the parity of the second and third qubits, in the Hadamard basis. If a phase flip occurs on any of the qubits, the parity measurements will reveal which qubit is corrupted, and a phase flip correction can be applied.
- The Shor code concatenates the 3-qubit bit flip code and the 3-qubit phase flip code by applying the bit flip code to each qubit of the phase flip code. The resulting code encodes a single qubit |ψ⟩ = α|0⟩ + β|1⟩ as a 9-qubit state:

|ψ⟩ = α|000⟩ + β|111⟩
|ψ⟩ = α|000⟩ + β|111⟩
|ψ⟩ = α|000⟩ + β|111⟩

- The Shor code uses six ancilla qubits to measure the parity of the first and second qubits, the parity of the second and third qubits, the parity of the fourth and fifth qubits, the parity of the fifth and sixth qubits, the parity of the seventh and eighth qubits, and the parity of the eighth and ninth qubits, in both the computational and the Hadamard basis.
- If a single-qubit error occurs on any of the qubits, the parity measurements will reveal which qubit is corrupted, and a bit flip and/or a phase flip correction can be applied.
- The Shor code can be represented by the following circuit diagram:

![Shor code circuit diagram](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9c/Shor_code.svg/1200px-Shor_code.svg.png)

- A possible mnemonic to remember the Shor code is: "Shor code is short for nine qubits, three times three, bit flip and phase flip, parity check and correct."
- Some advantages of the Shor code are:
  - It can correct any single-qubit error, which is the most common type of error in quantum systems.
  - It is based on simple and well-known codes, the 3-qubit bit flip code and the 3-qubit phase flip code.
  - It is the first example of a quantum error-correcting code, and inspired many other codes and techniques[^5