 Here is the content in markdown format for Unit 2 - Quantum Computation:

## Unit 2 - Quantum Computation

* Quantum bits or `qubits` - Unlike classical bits which can have a value of either 0 or 1, qubits can be in a superposition of states, having a probability of being 0 and 1 at the same time. Qubits can be represented by particles, photons, ions, etc. and their quantum properties like spin, polarization, etc. The state of a qubit can be represented by a vector $(a,b)$ where $a$ and $b$ are complex numbers and the absolute square of $a$ gives the probability of the qubit being 0 and the absolute square of $b$ gives the probability of the qubit being 1.
* Qubit operations - Qubits can be manipulated using quantum gates which are the quantum analog of classical logic gates. Some important quantum gates are:
    * Hadamard gate - It puts a qubit into an equal superposition of 0 and 1 states. It can be represented by the matrix $\dfrac{1}{\sqrt{2}}\begin{bmatrix}1&1\\1&-1\end{bmatrix}$.
    * Phase shift gate - It can change the relative phase of the superposition states. It is represented by the matrix $\begin{bmatrix}1&0\\0&e^{i\theta}\end{bmatrix}$ where $\theta$ is the amount of phase shift.
    * Controlled-NOT (CNOT) gate - It flips the state of the target qubit if the control qubit is 1. It is represented by the matrix $\begin{bmatrix}1&0&0&0\\0&1&0&0\\0&0&0&1\\0&0&1&0\end{bmatrix}$.
    * etc.
* Quantum algorithms - Quantum algorithms like Simon's algorithm and Shor's algorithm can be used to solve certain problems much more efficiently than classical algorithms. For example, Shor's algorithm can be used to factor numbers in polynomial time and break RSA encryption.

**Mnemonics** - Remember that qubits can be in superposition and manipulated using quantum gates. The key quantum gates to know are Hadamard gate, phase shift gate and CNOT gate. Also know that quantum algorithms like Shor's algorithm can solve certain problems much more efficiently than classical algorithms.

**Learning tricks** - The best way to understand qubits and quantum gates is by visualizing the states and operations using the Bloch sphere. Also try implementing the gates and Shor's algorithm on a quantum computer simulator to understand them better. Solving examples of factoring numbers using Shor's algorithm will help strengthen the understanding.