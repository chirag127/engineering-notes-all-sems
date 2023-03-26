### Quantum Operations

In quantum computing, quantum operations are used to manipulate quantum states to perform various computational tasks. These operations are represented by unitary matrices, which are reversible and preserve the probability amplitudes of the quantum state.

Here are some common quantum operations:

1. **Pauli-X gate**: This operation flips the value of a qubit from |0⟩ to |1⟩ or vice versa. It is represented by the matrix:

   ```
   X = [[0, 1],
        [1, 0]]
   ```

2. **Pauli-Y gate**: This operation changes the phase of a qubit and flips its value. It is represented by the matrix:

   ```
   Y = [[0, -i],
        [i, 0]]
   ```

3. **Pauli-Z gate**: This operation flips the phase of a qubit. It is represented by the matrix:

   ```
   Z = [[1, 0],
        [0, -1]]
   ```

4. **Hadamard gate**: This operation creates a superposition of the |0⟩ and |1⟩ states. It is represented by the matrix:

   ```
   H = [[1, 1],
        [1, -1]] / sqrt(2)
   ```

5. **CNOT gate**: This operation is a two-qubit gate that flips the second qubit if the first qubit is |1⟩. It is represented by the matrix:

   ```
   CNOT = [[1, 0, 0, 0],
           [0, 1, 0, 0],
           [0, 0, 0, 1],
           [0, 0, 1, 0]]
   ```

6. **SWAP gate**: This operation swaps the values of two qubits. It is represented by the matrix:

   ```
   SWAP = [[1, 0, 0, 0],
           [0, 0, 1, 0],
           [0, 1, 0, 0],
           [0, 0, 0, 1]]
   ```

7. **Controlled-Z gate**: This operation is a two-qubit gate that flips the phase of the second qubit if the first qubit is |1⟩. It is represented by the matrix:

   ```
   CZ = [[1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 1, 0],
         [0, 0, 0, -1]]
   ```

8. **Phase gate**: This operation adds a phase to the |1⟩ state. It is represented by the matrix:

   ```
   S = [[1, 0],
        [0, i]]
   ```

These are just some of the many quantum operations that are used in quantum computing. By combining these operations, more complex quantum circuits can be constructed to perform various computational tasks.