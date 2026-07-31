# Phase estimation

Phase estimation is a quantum algorithm that estimates the phase (or eigenvalue) of an eigenvector of a unitary operator. It is a central building block for many quantum algorithms, such as Shor's algorithm, quantum Fourier transform, and quantum machine learning . It also implements a measurement for essentially any Hermitian operator.

The objective of the algorithm is the following: Given a unitary operator U and an eigenvector |ψ⟩ of U, the algorithm estimates θ in U|ψ⟩ = e<sup>2πiθ</sup>|ψ⟩.

The algorithm consists of the following steps:

- Prepare two quantum registers: one with n qubits initialized to |0⟩, and another with one qubit initialized to |ψ⟩.
- Apply a Hadamard gate to each qubit in the first register, creating an equal superposition of all possible states.
- Apply a controlled-U<sup>2<sup>k</sup></sup> gate to the k-th qubit in the first register and the qubit in the second register, for k = 0, ..., n-1. This creates a superposition of states with different phases proportional to 2<sup>k</sup>θ.
- Apply an inverse quantum Fourier transform to the first register, which maps the phases to the amplitudes of the computational basis states.
- Measure the first register, which gives an n-bit approximation of θ.

The algorithm has a success probability of at least 4/π<sup>2</sup> ≈ 40.5%, which can be improved by repeating the algorithm or using phase kickback techniques. The algorithm requires O(n) qubits and O(n<sup>2</sup>) gates.