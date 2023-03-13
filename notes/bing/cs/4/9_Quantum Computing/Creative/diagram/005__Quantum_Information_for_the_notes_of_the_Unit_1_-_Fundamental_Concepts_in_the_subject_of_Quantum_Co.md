I am Sydney, your AI assistant. I will draw a detailed ASCII diagram for quantum information for the notes of the Unit 1 - Fundamental Concepts in the subject of Quantum Computing.

### Quantum Information

Quantum information refers to data that can be physically stored in a quantum system, such as a qubit. A qubit is the basic unit of quantum information, analogous to a bit in classical computing. A qubit can exist in a superposition of two basis states, usually denoted as |0> and |1>. Unlike a bit, which can only store one of these states at a time, a qubit can store both states simultaneously with certain probabilities. The state of a qubit can be represented by a two-dimensional column vector of complex numbers, called the quantum state vector. The norm of this vector must be equal to one, meaning that the sum of the squares of the absolute values of the coefficients must be one. For example, a possible state of a qubit is:

|ψ> = 1/√2 |0> + i/√2 |1>

This means that the qubit has a 50% chance of being measured as |0> and a 50% chance of being measured as |1>. The quantum state vector can also be represented by a point on the surface of a unit sphere, called the Bloch sphere. The Bloch sphere is a useful tool for visualizing the state of a qubit and the effects of quantum operations on it. The following ASCII diagram illustrates the Bloch sphere and the state vector of the qubit:

    |1>
     ^
     |
     |
     |   /|ψ>
     |  / |
     | /  |
     |/   |
     +----+----> |0>
    /    /
   /    /
  /    /
 v   v
|0> |1>

Quantum information can also be stored in systems of multiple qubits, called quantum registers. The state of a quantum register is the tensor product of the states of the individual qubits. For example, if we have two qubits in the states |ψ> and |φ>, then the state of the quantum register is:

|ψ> ⊗ |φ> = (1/√2 |0> + i/√2 |1>) ⊗ (1/√2 |0> - 1/√2 |1>) 
            = 1/2 |00> + i/2 |01> - 1/2 |10> - i/2 |11>

The state of a quantum register can also be represented by a vector of 2^n complex numbers, where n is the number of qubits. For example, the state of the quantum register above can be written as:

|ψ> ⊗ |φ> = [1/2, i/2, -1/2, -i/2]^T

Quantum information can be manipulated by applying quantum operations, such as quantum gates, to the quantum system. Quantum gates are unitary matrices that act on the state vector of the qubit or the quantum register. For example, the Hadamard gate is a quantum gate that creates a superposition of |0> and |1> from either state. It is represented by the following matrix:

H = 1/√2 [1,  1]
         [1, -1]

If we apply the Hadamard gate to a qubit in the state |0>, we get:

H |0> = 1/√2 [1,  1] [1] = 1/√2 [1] + 1/√2 [1] = 1/√2 |0> + 1/√2 |1>

If we apply the Hadamard gate to a qubit in the state |1>, we get:

H |1> = 1/√2 [1,  1] [0] = 1/√2 [1] - 1/√2 [1] = 1/√2 |0> - 1/√2 |1>

Quantum gates can also act on multiple qubits, such as the CNOT gate, which flips the second qubit if the first qubit is |1>. It is represented by the following matrix:

CNOT = [1, 0, 0, 0]
       [0, 1, 0, 0]
       [0,