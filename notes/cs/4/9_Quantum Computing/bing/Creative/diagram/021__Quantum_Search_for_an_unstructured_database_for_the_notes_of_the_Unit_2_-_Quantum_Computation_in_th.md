The following diagram illustrates the basic architecture of a quantum search for an unstructured database, based on the Grover's algorithm   . The diagram is drawn using ASCII characters for simplicity.

```
+-----------------+     +-----------------+     +-----------------+
| Quantum         |     | Quantum         |     | Quantum         |
| Register        |     | Register        |     | Register        |
| (n qubits)      |     | (n qubits)      |     | (n qubits)      |
|                 |     |                 |     |                 |
| |0>^n           |     | |psi>           |     | |psi'>          |
|                 |     |                 |     |                 |
+-----------------+     +-----------------+     +-----------------+
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       |                      |                      |
       v                      v                      v
+-----------------+     +-----------------+     +-----------------+
| Hadamard        |     | Oracle          |     | Inversion       |
| Transformation  |     | (O(f))          |     | about the mean  |
| (H^N)           |     |                 |     | (I-2|psi><psi|) |
|                 |     |                 |     |                 |
| H|0> = |+>      |     | O(f)|x> = -|x>  |     | I-2|+><+| = Z   |
|                 |     | if f(x) = 1     |     |                 |
+-----------------+     +-----------------+     +-----------------+
```

The quantum search algorithm consists of three main steps:

1. Initialize the quantum register to the equal superposition state |psi> = H^N|0>^n, where H is the Hadamard gate and N is the number of qubits.
2. Apply the oracle O(f) to the quantum register, where f is a Boolean function that marks the target element in the database by flipping its sign, i.e. O(f)|x> = -|x> if f(x) = 1 and O(f)|x> = |x> otherwise.
3. Apply the inversion about the mean operation to the quantum register, which is equivalent to applying the Z gate to each qubit after applying the Hadamard gate, i.e. I-2|psi><psi| = H^N Z^N H^N.
4. Repeat steps 2 and 3 for about sqrt(N) times, where N is the size of the database, to amplify the amplitude of the target element and reduce the amplitudes of the other elements.
5. Measure the quantum register to obtain the target element with high probability.

The quantum search algorithm can find the target element in an unstructured database with O(sqrt(N)) queries to the oracle, whereas the classical search algorithm requires O(N) queries in the worst case. This gives a quadratic speedup over the classical search algorithm.