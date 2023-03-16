# Quantum Fourier transform

The quantum Fourier transform (QFT) is the quantum implementation of the discrete Fourier transform (DFT) over the amplitudes of a wavefunction. It is part of many quantum algorithms, most notably Shor's factoring algorithm and quantum phase estimation.

## Definition

The DFT acts on a vector $(x_0, ..., x_{N-1})$ and maps it to the vector $(y_0, ..., y_{N-1})$ by the formula:

$$
y_k = \frac{1}{\sqrt{N}} \sum_{j=0}^{N-1} x_j e^{2\pi ijk/N}
$$

The QFT acts on a quantum state vector $|\psi\rangle$ and maps it to the quantum state vector $|\phi\rangle$ by the formula:

$$
|\phi\rangle = \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} e^{2\pi ijk/N} |k\rangle
$$

where $|k\rangle$ is the binary representation of the integer $k$ in a quantum register of $n$ qubits, and $N = 2^n$.

## Circuit

The QFT can be implemented by a quantum circuit consisting of Hadamard gates and controlled phase shift gates. The circuit for a 3-qubit QFT is shown below:

![QFT circuit](https://qiskit.org/textbook/ch-algorithms/images/qft_3.png)

The general circuit for an $n$-qubit QFT is shown below:

![QFT circuit](https://qiskit.org/textbook/ch-algorithms/images/qft_general.png)

The circuit can be simplified by omitting the phase shift gates that have a negligible effect on the output. The circuit can also be reversed to perform the inverse QFT.

## Properties

The QFT has the following properties:

- It is a unitary transformation, meaning that it preserves the norm of the quantum state vector.
- It is reversible, meaning that it can be inverted by applying the inverse QFT.
- It is linear, meaning that it obeys the superposition principle.
- It is symmetric, meaning that it does not depend on the order of the qubits in the quantum register.
- It is periodic, meaning that it repeats itself after $N$ applications.
- It is basis-independent, meaning that it does not depend on the choice of the computational basis.

## Applications

The QFT is a part of many quantum algorithms, notably:

- Shor's algorithm for factoring and computing the discrete logarithm
- The quantum phase estimation algorithm for estimating the eigenvalues of a unitary operator
- Algorithms for the hidden subgroup problem

The QFT can also be used to perform quantum signal processing, quantum state tomography, and quantum error correction.