### Single Orbit Operations for the notes of the Unit 2 - Quantum Computation in the subject of Quantum Computing

In quantum computing, single-qubit operations are used to manipulate the state of a single qubit. These operations are essential for quantum algorithms and can be performed using various techniques. In this section, we will discuss the common single-qubit operations used in quantum computing.

1. **Pauli-X Gate (NOT Gate)**  
The Pauli-X gate is a single-qubit operation that flips the state of a qubit from 0 to 1 or vice versa. This gate is equivalent to the classical NOT gate and is represented by the matrix:

    ```
    X = |0 1|
        |1 0|
    ```
    
2. **Pauli-Y Gate**  
The Pauli-Y gate is a single-qubit operation that rotates the state of a qubit around the y-axis of the Bloch sphere. This gate is represented by the matrix:
    ```
    Y = |0 -i|
        |i 0|
    ```
    
3. **Pauli-Z Gate**  
The Pauli-Z gate is a single-qubit operation that rotates the state of a qubit around the z-axis of the Bloch sphere. This gate is represented by the matrix:
    ```
    Z = |1 0|
        |0 -1|
    ```
    
4. **Hadamard Gate**  
The Hadamard gate is a single-qubit operation that creates superposition by evenly distributing the probability amplitudes of a qubit. This gate is represented by the matrix:
    ```
    H = 1/√2 |1 1|
            |1 -1|
    ```
    
5. **Phase Gate**  
The phase gate is a single-qubit operation that introduces a phase shift of π radians to the state of a qubit. This gate is represented by the matrix:
    ```
    S = |1 0|
        |0 i|
    ```
    
6. **Pi/8 Gate (T Gate)**  
The Pi/8 gate, also known as the T gate, is a single-qubit operation that introduces a phase shift of π/4 radians to the state of a qubit. This gate is represented by the matrix:
    ```
    T = |1 0|
        |0 e^(iπ/4)|
    ```

These single-qubit operations are the building blocks of more complex quantum gates and algorithms. By combining these operations with multi-qubit gates, quantum circuits can be designed to perform specific quantum computations.