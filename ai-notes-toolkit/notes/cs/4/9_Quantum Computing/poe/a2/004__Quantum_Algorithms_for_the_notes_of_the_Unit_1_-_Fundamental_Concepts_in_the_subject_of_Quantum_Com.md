 Here is the content in markdown format without any emojis or external links:

### Quantum Algorithms for the notes of the Unit 1 - Fundamental Concepts in the subject of Quantum Computing

1. Quantum Fourier Transform:
- Input: N qubits in the state $|x\rangle=|x_1x_2...x_N\rangle$, where $x_i\\in\\{0,1\\}$
- Output: The qubits are in the state $|y\rangle=|y_1y_2...y_N\rangle$,where $y_i=\\sum_{j=0}^{N-1}x_je^{2\\pi i j k/N}$
- Use: Used in Shor's algorithm for efficient quantum integer factorization and Simon's algorithm for quantum period finding.

2. Deutsch-Jozsa algorithm:
- Given a function $f: \{0,1\}^n \\to \\{0,1\\}$ that is either constant (always returns 0 or 1) or balanced (returns 0 and 1 with equal probability). Decide whether $f$ is constant or balanced.
- Use: Demonstrates the potential speed up achievable using quantum algorithms. Deutsch-Jozsa can determine the nature of the function using only one query to the oracle, while classically this requires $\frac{1}{2}n+1$ queries in the worst case.

[The content continues in the similar format with headings and points for other Quantum Algorithms]