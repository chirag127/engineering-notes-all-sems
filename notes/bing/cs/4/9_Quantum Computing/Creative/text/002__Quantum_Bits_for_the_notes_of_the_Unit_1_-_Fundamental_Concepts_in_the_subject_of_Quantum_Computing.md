### Quantum Bits

- A quantum bit or qubit is the basic unit of quantum information. It is a two-state quantum system that can exist in a superposition of two basis states, usually denoted as |0> and |1>.
- Unlike a classical bit, which can only store one of the two values 0 or 1, a qubit can store a linear combination of both values, called a quantum state. The quantum state of a qubit can be written as:

  |ψ> = α|0> + β|1>

  where α and β are complex numbers such that |α|^2 + |β|^2 = 1.

- The quantum state of a qubit represents the probability amplitudes of measuring the qubit in either of the basis states. The square of the absolute value of α gives the probability of measuring the qubit as |0>, and the square of the absolute value of β gives the probability of measuring the qubit as |1>. For example, if the quantum state of a qubit is:

  |ψ> = 1/√2|0> + 1/√2|1>

  then the probability of measuring the qubit as |0> or |1> is both 1/2.

- The quantum state of a qubit can be manipulated by applying quantum gates, which are unitary operators that act on one or more qubits. Quantum gates can change the relative phases and amplitudes of the basis states, resulting in different superpositions. For example, applying the Hadamard gate H to a qubit in the state |0> results in the state:

  H|0> = 1/√2|0> + 1/√2|1>

  which is an equal superposition of |0> and |1>.

- The quantum state of a qubit can also be entangled with another qubit, meaning that their quantum states are correlated and cannot be described independently. For example, two qubits can be entangled in the state:

  |ψ> = 1/√2|00> + 1/√2|11>

  which is called a Bell state. This state implies that if one qubit is measured as |0>, the other qubit will also be measured as |0>, and vice versa. Entanglement is a quantum phenomenon that has no classical analogue and enables quantum algorithms to perform tasks that are impossible or inefficient for classical algorithms.