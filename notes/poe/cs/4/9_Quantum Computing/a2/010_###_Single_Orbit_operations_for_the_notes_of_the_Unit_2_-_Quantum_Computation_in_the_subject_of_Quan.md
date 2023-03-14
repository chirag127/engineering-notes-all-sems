 Here is the content in markdown format for the topic ### Single Orbit operations for the notes of the Unit 2 - Quantum Computation in the subject of Quantum Computing:

### Single Orbit operations for the notes of the Unit 2 - Quantum Computation

The single qubit operations in quantum computing are:

1. Bit flip or Not gate: It flips the state of the qubit. If the qubit is in state $\lvert 0 \rangle$, it moves to state $\lvert 1 \rangle$ and vice-versa. It is represented by `X gate` or `Pauli X gate`.

Mnemonic: Think of it as flipping a coin. Head becomes tail and tail becomes head.

2. Phase flip: It adds a phase of $\pi$ to the state of the qubit. If the qubit is in state $\lvert 0 \rangle$, it moves to state $\lvert 0 \rangle$ with a phase of $\pi$. If it is in state $\lvert 1 \rangle$, it moves to state $\lvert 1 \rangle$ with a phase of $-\pi$. It is represented by `Z gate` or `Pauli Z gate`.

Mnemonic: Think of it as changing the sign of the state. Plus becomes minus and minus becomes plus.

3. Hadamard gate: It puts the qubit into an equal superposition of states $\lvert 0 \rangle$ and $\lvert 1 \rangle$. It is represented by `H gate`.

Mnemonic: Think of it as putting the qubit into a balanced mixture of 0 and 1.

4. Phase shift gates: These gates add a phase to the state of the qubit. For example, a phase shift gate with phase $\theta$ denoted by `S gate` would change the state as:

$\lvert 0 \rangle \mapsto \lvert 0 \rangle$

$\lvert 1 \rangle \mapsto e^{i\theta} \lvert 1 \rangle$

These gates can be used to introduce controlled phase shifts in superposition states.

The single qubit gates form a universal set of gates which means any quantum operation on a qubit can be expressed as a sequence of these gates. They are the basic building blocks for multi-qubit operations and quantum algorithms.