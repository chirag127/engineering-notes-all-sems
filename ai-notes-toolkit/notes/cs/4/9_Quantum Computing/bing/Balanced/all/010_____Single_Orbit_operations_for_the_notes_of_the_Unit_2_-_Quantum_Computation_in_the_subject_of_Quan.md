# Single Orbit Operations

Single orbit operations are quantum operations that act on a single qubit, which is the basic unit of quantum information. A qubit is a two-level quantum system that can be in a superposition of two basis states, usually denoted as |0> and |1>. A single orbit operation can manipulate the state of a qubit by applying a unitary transformation or a measurement.

## Unitary Transformations

A unitary transformation is a linear operation that preserves the norm of a vector. In quantum computing, a unitary transformation can be represented by a 2x2 matrix that acts on a 2D qubit vector. A unitary transformation does not change the probability of measuring a qubit in either basis state, but it can change the relative phase and amplitude of the superposition.

Some examples of unitary transformations are:

- The X-gate, which flips the state of a qubit from |0> to |1> and vice versa. It is equivalent to a classical NOT gate. It can be represented by the matrix:

|0 1|
|1 0|

- The Y-gate, which flips the state of a qubit and adds a complex phase of i or -i. It can be represented by the matrix:

|0 -i|
|i 0|

- The Z-gate, which adds a phase of -1 to the state |1> and leaves the state |0> unchanged. It can be represented by the matrix:

|1 0|
|0 -1|

- The H-gate, which creates a superposition of |0> and |1> with equal probabilities. It is also known as the Hadamard gate. It can be represented by the matrix:

|1/sqrt(2) 1/sqrt(2)|
|1/sqrt(2) -1/sqrt(2)|

- The Phase Shift gate, which adds a phase of e^(i*theta) to the state |1> and leaves the state |0> unchanged. It can be represented by the matrix:

|1 0|
|0 e^(i*theta)|

## Measurement

A measurement is a non-unitary operation that collapses the state of a qubit to one of the basis states, according to the probability distribution given by the square of the amplitudes. A measurement can be performed in different bases, such as the computational basis (|0> and |1>), the Hadamard basis (|+> and |->), or any other orthogonal basis. A measurement can also be represented by a 2x2 matrix, but it is not reversible or linear.

Some examples of measurement matrices are:

- The computational basis measurement, which projects the state of a qubit onto |0> or |1> with probabilities |a|^2 and |b|^2, where a and b are the amplitudes of the superposition. It can be represented by the matrices:

|1 0| |0 0|
|0 0| |0 1|

- The Hadamard basis measurement, which projects the state of a qubit onto |+> or |-> with probabilities |a+b|^2/2 and |a-b|^2/2, where a and b are the amplitudes of the superposition. It can be represented by the matrices:

|1/sqrt(2) 1/sqrt(2)| |1/sqrt(2) -1/sqrt(2)|
|1/sqrt(2) 1/sqrt(2)| |1/sqrt(2) -1/sqrt(2)|