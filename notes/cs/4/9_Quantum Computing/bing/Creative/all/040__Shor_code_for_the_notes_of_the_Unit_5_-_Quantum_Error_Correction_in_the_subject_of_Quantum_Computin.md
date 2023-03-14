### Shor code for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Quantum error correction (QEC) is a technique to protect quantum information from errors due to noise, decoherence, or other sources of error.
- QEC codes use multiple physical qubits to encode one logical qubit, such that errors can be detected and corrected without disturbing the quantum state.
- Shor code is one of the first and simplest QEC codes, proposed by Peter Shor in 1995  .
- Shor code can correct any single-qubit error, whether it is a bit flip error (X), a phase flip error (Z), or a combination of both (Y).
- Shor code uses nine physical qubits to encode one logical qubit, and eight ancillary qubits for syndrome measurement.
- The encoding circuit of Shor code is shown below:

```
|0> ---H---*-----------------*-----------------*---H---*-----------------*-----------------*---H---*-----------------*-----------------*---H---M
           |                 |                 |       |                 |                 |       |                 |                 |
|0> ---H---|---*---------*---|---*---------*---|---H---|---*---------*---|---*---------*---|---H---|---*---------*---|---*---------*---|---H---M
           |   |         |   |   |         |   |       |   |         |   |   |         |   |       |   |         |   |   |         |   |
|0> ---H---|---|---*---*---|---|---|---*---*---|---H---|---|---*---*---|---|---|---*---*---|---H---|---|---*---*---|---|---|---*---*---|---H---M
           |   |   |   |   |   |   |   |   |   |       |   |   |   |   |   |   |   |   |   |       |   |   |   |   |   |   |   |   |   |
|0> -------X---|---|---|---X---|---|---|---X---|-------X---|---|---|---X---|---|---|---X---|-------X---|---|---|---X---|---|---|---X---|-------
               |   |   |       |   |   |       |           |   |   |       |   |   |       |           |   |   |       |   |   |       |
|0> -----------X---|---X-------|---|---X-------|-----------X---|---X-------|---|---X-------|-----------X---|---X-------|---|---X-------|-------
                   |           |   |           |               |           |   |           |               |           |   |           |
|0> ---------------X-----------|---X-----------|---------------X-----------|---X-----------|---------------X-----------|---X-----------|-------
                               |               |                           |               |                           |               |
|0> ---------------------------X---------------|---------------------------X---------------|---------------------------X---------------|-------
                                               |                                               |                                               |
|0> -------------------------------------------X-------------------------------------------|-------------------------------------------X-------
                                                                                           |                                               |
|0> -----------------------------------------------------------------------------------------------------------X-----------------------------------
```

- The encoding circuit works as follows:
  - The first three qubits (0, 1, 2) are used to encode the logical qubit, which is initially in state |0>.
  - The first qubit is entangled with the second and third qubits using CNOT gates, creating a three-qubit GHZ state.
  - The GHZ state is then put into superposition using Hadamard gates on each qubit, creating a nine-qubit GHZ state.
  - The next three qubits (3, 4, 5) are entangled with the first three qubits using CNOT gates, creating a copy of the logical qubit.
  - The last three qubits (6, 7, 8) are entangled with the first three qubits using CNOT gates, creating another copy of the logical qubit.