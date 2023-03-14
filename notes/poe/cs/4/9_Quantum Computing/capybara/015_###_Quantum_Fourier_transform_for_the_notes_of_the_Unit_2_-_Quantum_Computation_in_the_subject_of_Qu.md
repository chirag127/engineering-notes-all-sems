### Quantum Fourier Transform for the notes of Unit 2 - Quantum Computation in the subject of Quantum Computing

The Quantum Fourier Transform (QFT) is a fundamental operation in quantum computing, used in many quantum algorithms. It is a quantum analog of the classical discrete Fourier transform and is used to transform a quantum state from the time domain to the frequency domain.

#### Definition:

The QFT is defined as:

$$QFT|j\rangle = \frac{1}{\sqrt{N}} \sum_{k=0}^{N-1} e^{2\pi ijk/N}|k\rangle$$

where $N$ is the dimension of the Hilbert space and $j$ is an integer between $0$ and $N-1$.

#### Mnemonic:

An easy way to remember the QFT formula is by using the mnemonic "Queen's Fort".

#### Steps:

The QFT can be implemented using a circuit composed of Hadamard gates and phase gates. The steps involved in the QFT are as follows:

1. Apply a Hadamard gate to the first qubit.

2. Apply a controlled phase shift gate between the first qubit and the second qubit with a phase angle of $\frac{\pi}{2}$.

3. Apply a controlled phase shift gate between the first qubit and the third qubit with a phase angle of $\frac{\pi}{4}$.

4. Repeat step 3 for each subsequent qubit, doubling the phase angle each time.

5. Swap the first and last qubits.

#### Example:

Let's consider a simple example of the QFT on a 2-qubit system.

Suppose we have the state $|01\rangle$. We can apply the QFT as follows:

1. Apply a Hadamard gate to the first qubit:

$$H|01\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)|1\rangle$$

2. Apply a controlled phase shift gate between the first qubit and the second qubit with a phase angle of $\frac{\pi}{2}$:

$$\frac{1}{\sqrt{2}}(|0\rangle + e^{i\pi/2}|1\rangle)(|0\rangle + |1\rangle)$$

3. Swap the first and last qubits:

$$\frac{1}{\sqrt{2}}(|1\rangle + e^{i\pi/2}|0\rangle)(|0\rangle + |1\rangle)$$

4. Apply a Hadamard gate to the first qubit:

$$\frac{1}{2}[(|0\rangle + e^{i\pi/2}|1\rangle) + (|0\rangle - e^{i\pi/2}|1\rangle)][(|0\rangle + |1\rangle)]$$

$$= \frac{1}{2}(|00\rangle + i|01\rangle - |10\rangle - i|11\rangle)$$

Thus, the QFT of the state $|01\rangle$ is $\frac{1}{2}(|00\rangle + i|01\rangle - |10\rangle - i|11\rangle)$.

#### Applications:

The QFT is used in many quantum algorithms, including Shor's algorithm for factorization, quantum phase estimation, and quantum simulation.

#### Advantages:

The QFT is able to efficiently transform a quantum state from the time domain to the frequency domain, allowing for efficient calculation of Fourier transforms on quantum computers.

#### Disadvantages:

The QFT requires a large number of gates, making it difficult to implement on current quantum hardware.

In conclusion, the Quantum Fourier Transform is a fundamental operation in quantum computing used in many quantum algorithms. It enables efficient calculation of Fourier transforms on quantum computers, and its implementation involves a circuit composed of Hadamard gates and phase gates.