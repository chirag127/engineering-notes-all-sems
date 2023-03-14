 Here is the content in markdown format:

### Quantum Bits for the notes of the Unit 1 - Fundamental Concepts in the subject of Quantum Computing

Quantum bits or `Qubits` are the basic units of information in a quantum computer. They are analogous to bits in a classical computer which can have a value of either 0 or 1. However, qubits can be in a superposition of states, having a probability of containing 0 and 1 at the same time. This allows a quantum computer to explore many possible solutions in parallel and leads to a speed up over classical algorithms for certain problems.

**Representation of Qubits:**

-   Qubits are represented by quantum mechanical two-state systems, such as spin-1⁄2 particles, photons, ions, or circuits.
-   The two states of a qubit can be denoted as $\vert 0 \rangle$ and $\vert 1 \rangle$.
-   Due to the superposition principle, a qubit can be in a superposition of the two states: $\alpha \vert 0 \rangle + \beta \vert 1 \rangle$, where $\alpha$ and $\beta$ are complex numbers satisfying $|\alpha|2 + |\beta|2 = 1$.

**Qubit Manipulation:**

-   Qubits can be manipulated using quantum gates which are the basic building blocks of quantum circuits.
-   Common one-qubit gates are the Hadamard gate, the phase shift gate and the $\pi/8$ gate. Two-qubit gates include the CNOT gate and the SWAP gate.
-   These gates can be applied using electromagnetic pulses to manipulate the quantum state of the physical system encoding the qubit.
-   The sequence of gates applied to the qubits is analogous to a classical circuit. However, due to the superposition principle, a quantum circuit can evolve a superposition of states leading to quantum parallelism.

**Qubit Measurement:**

-   The state of a qubit cannot be directly accessed. It can only be inferred through measurements.
-   Measuring a qubit causes it to collapse from a superposition of states into a single classical state of 0 or 1 with some probability.
-   The probability of the qubit collapsing into the $\vert 0 \rangle$ state is given by the square of the amplitude of that state, that is $|\alpha|2$. Similarly, the probability of collapsing into the $\vert 1 \rangle$ state is given by $|\beta|2$.

**Applications of Qubits:**

-   Qubits are the basic building blocks of quantum computers which can solve certain problems much faster than classical computers.
-   Some examples of problems that can have quantum speedups are quantum Fourier transform, quantum simulation, quantum search algorithms (e.g. Grover's search algorithm), quantum cryptography, etc.
-   Qubits can also be used to build quantum sensors which can achieve greater precision than their classical counterparts. For example, quantum gyroscopes can achieve higher sensitivity, and quantum clocks can have lower uncertainties.