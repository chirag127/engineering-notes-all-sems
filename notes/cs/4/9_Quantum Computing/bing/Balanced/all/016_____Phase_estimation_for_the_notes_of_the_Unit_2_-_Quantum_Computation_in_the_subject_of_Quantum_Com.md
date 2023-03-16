# Phase estimation

Phase estimation is a quantum algorithm that estimates the phase (or eigenvalue) of an eigenvector of a unitary operator. It is a central building block for many quantum algorithms, such as Shor's algorithm, quantum Fourier transform, and quantum machine learning . It also implements a measurement for essentially any Hermitian operator.

The objective of the algorithm is the following: Given a unitary operator U and an eigenvector |ψ⟩ of U, the algorithm estimates θ in U|ψ⟩ = e<sup>2πiθ</sup>|ψ⟩. Here, θ is a fraction between 0 and 1, and e<sup>2πiθ</sup> is the corresponding eigenvalue of U.

The algorithm uses two quantum registers: a control register of n qubits, initialized to |0⟩<sup>⊗n</sup>, and a target register of m qubits, initialized to |ψ⟩. The algorithm consists of the following steps:

- Apply a Hadamard gate to each qubit in the control register, creating an equal superposition of all possible states.
- Apply a controlled-U<sup>2<sup>k</sup></sup> gate to the target register for each qubit in the control register, where k is the index of the control qubit, starting from 0. This creates a superposition of states with different phases proportional to 2<sup>k</sup>θ.
- Apply an inverse quantum Fourier transform to the control register, which converts the phases into binary digits of the estimate of θ.
- Measure the control register, which gives an n-bit approximation of θ.

The accuracy of the algorithm depends on the number of qubits in the control register and the precision of the controlled-U operations. The algorithm can be improved by using phase kickback, iterative methods, or post-processing techniques.