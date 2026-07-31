### Universal Quantum Gates

In quantum computing, the basic building blocks of a quantum algorithm are quantum gates. A quantum gate is a unitary transformation that operates on qubits, the basic units of quantum information. Quantum gates are analogous to classical logic gates, but they operate on quantum states instead of classical bits. Universal quantum gates are a special class of quantum gates that can be used to construct any quantum algorithm.

Here are the most common universal quantum gates:

1. Hadamard gate (H gate): The Hadamard gate is a single-qubit gate that creates a superposition of the two basis states, |0⟩ and |1⟩. It is represented by the matrix:

    ```
    H gate = 1/√2 * [1 1; 1 -1]
    ```

2. Pauli-X gate (X gate): The Pauli-X gate is a single-qubit gate that flips the state of a qubit from |0⟩ to |1⟩ or vice versa. It is represented by the matrix:

    ```
    X gate = [0 1; 1 0]
    ```

3. CNOT gate: The CNOT (Controlled-NOT) gate is a two-qubit gate that flips the second qubit if the first qubit is in the state |1⟩. It is represented by the matrix:

    ```
    CNOT gate = [1 0 0 0; 0 1 0 0; 0 0 0 1; 0 0 1 0]
    ```

4. Phase gate (S gate): The Phase gate is a single-qubit gate that applies a phase shift to the state of a qubit. It is represented by the matrix:

    ```
    S gate = [1 0; 0 i]
    ```

5. π/8 gate (T gate): The π/8 gate is a single-qubit gate that applies a phase shift of π/4 to the state of a qubit. It is represented by the matrix:

    ```
    T gate = [1 0; 0 e^(iπ/4)]
    ```

These universal quantum gates can be combined to create any quantum algorithm. Other universal quantum gates include the Clifford gates and the Toffoli gate. Understanding the properties of these gates is essential for designing and implementing quantum algorithms.