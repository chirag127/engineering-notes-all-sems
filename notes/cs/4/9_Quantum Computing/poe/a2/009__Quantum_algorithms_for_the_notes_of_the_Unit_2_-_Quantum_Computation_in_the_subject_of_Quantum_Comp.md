 Here is the content in markdown format without any emojis or external links in a formal tone:

### Quantum algorithms for the notes of the Unit 2 - Quantum Computation in the subject of Quantum Computing.

1. Deutsch-Jozsa algorithm:
-Takes as input an oracle function f that is either constant (always 0 or 1) or balanced (output 0 and 1 with equal probability).
-The goal is to determine whether the function is constant or balanced in a single query to the oracle.
-It uses an interferometer with one input qubit and one output qubit. If the output qubit ends up in the $\lvert + \rangle$ state, the function is constant. If it ends up in the $\lvert -\rangle$ state, the function is balanced.

2. Simon's algorithm:
-Takes as input a black-box that computes a function $f: \{0,1\}^n → \{0,1\}^n$ such that $f(x) = x^2 \mod N$ for some secret $N$.
-The goal is to determine the period $r = \gcd(N, 2^n − 1)$.
-It uses a quantum Fourier transform on $n$ qubits to solve the problem in a single invocation of the black-box function. The period can then be extracted via classical post-processing.

[Other quantum algorithms like Shor's algorithm, Grover's algorithm, etc. can be added in a similar formal tone with points.]