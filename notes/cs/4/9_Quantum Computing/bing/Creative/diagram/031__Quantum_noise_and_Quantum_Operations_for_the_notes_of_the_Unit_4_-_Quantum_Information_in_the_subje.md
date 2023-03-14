Quantum noise and quantum operations are important topics in quantum information and quantum computing. Quantum noise refers to the random fluctuations and errors that affect quantum systems due to imperfect control signals, interference from the environment, and unwanted interactions between qubits. Quantum operations are the mathematical descriptions of how quantum states change under the influence of quantum noise and quantum gates. Quantum gates are the basic operations that manipulate qubits in a quantum circuit.

The following diagram illustrates the basic architecture of a quantum circuit:

```
    Input qubits         Quantum gates         Output qubits
    |0>  |0>  |0>  |0>   |---| |---| |---|      |0>  |0>  |0>  |0>
    |   \|/   |   \|/   | H | | C | | C |      |   \|/   |   \|/   
    |0>  |0>  |0>  |0>   |---| | N | | N |      |0>  |0>  |0>  |0>
    |   \|/   |   \|/   | H | | O | | O |      |   \|/   |   \|/   
    |0>  |0>  |0>  |0>   |---| | T | | T |      |0>  |0>  |0>  |0>
    |   \|/   |   \|/   | H | |---| |---|      |   \|/   |   \|/   
    |0>  |0>  |0>  |0>   |---| |---| |---|      |0>  |0>  |0>  |0>
```

In this diagram, each vertical line represents a qubit, and each box represents a quantum gate. The input qubits are initialized to the state |0>, and the output qubits are the result of applying the quantum gates to the input qubits. The quantum gates in this example are the Hadamard gate (H), which creates a superposition of |0> and |1> states, and the controlled-NOT gate (CNOT), which flips the target qubit (the lower one) if the control qubit (the upper one) is |1>. The quantum circuit performs a quantum operation that transforms the input state to the output state.

However, due to quantum noise, the output state may not be exactly the same as the ideal one. Quantum noise can be modeled by adding extra quantum gates that represent the noise sources, such as bit-flip errors, phase-flip errors, or depolarizing errors. The following diagram shows how quantum noise can affect the quantum circuit:

```
    Input qubits         Quantum gates         Noise gates         Output qubits
    |0>  |0>  |0>  |0>   |---| |---| |---|      |---| |---| |---|   |0>  |0>  |0>  |0>
    |   \|/   |   \|/   | H | | C | | C |      | B | | B | | B |   |   \|/   |   \|/   
    |0>  |0>  |0>  |0>   |---| | N | | N |      |---| |---| |---|   |0>  |0>  |0>  |0>
    |   \|/   |   \|/   | H | | O | | O |      | P | | P | | P |   |   \|/   |   \|/   
    |0>  |0>  |0>  |0>   |---| | T | | T |      |---| |---| |---|   |0>  |0>  |0>  |0>
    |   \|/   |   \|/   | H | |---| |---|      | D | | D | | D |   |   \|/   |   \|/   
    |0>  |0>  |0>  |0>   |---| |---| |---|      |---| |---| |---|   |0>  |0>  |0>  |0>
```

In this diagram, each extra box represents a noise gate that