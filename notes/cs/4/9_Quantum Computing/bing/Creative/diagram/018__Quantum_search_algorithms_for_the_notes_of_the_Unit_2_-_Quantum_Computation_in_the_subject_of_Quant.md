The following diagram illustrates the basic architecture of a quantum search algorithm:

```
    |0> ---H---|---U_f---|---U_s---|---M---|---f(x)=1?
    |0> ---H---|---U_f---|---U_s---|---M---|---f(x)=1?
    |0> ---H---|---U_f---|---U_s---|---M---|---f(x)=1?
    |0> ---H---|---U_f---|---U_s---|---M---|---f(x)=1?
    |0> ---H---|---U_f---|---U_s---|---M---|---f(x)=1?
    |0> ---H---|---U_f---|---U_s---|---M---|---f(x)=1?
    |0> ---H---|---U_f---|---U_s---|---M---|---f(x)=1?
    |0> ---H---|---U_f---|---U_s---|---M---|---f(x)=1?
    |0> ---H---|---U_f---|---U_s---|---M---|---f(x)=1?
    |0> ---H---|---U_f---|---U_s---|---M---|---f(x)=1?

    H: Hadamard gate
    U_f: Oracle function
    U_s: Diffusion operator
    M: Measurement
    f(x): Binary function
```

The quantum search algorithm, created by Grover, is quadratically faster than its classical analogous, since only O(sqrt(N)) operations are needed. In a quantum computer, the number of elements to be searched is the number of possible states of the system N = 2^n, where n is the number of qubit system.

The algorithm works as follows:

- Initialize n qubits to the state |0>
- Apply the Hadamard gate H to each qubit to create a superposition of all possible states
- Repeat the following steps O(sqrt(N)) times:
  - Apply the oracle function U_f to the qubits, which flips the sign of the state that satisfies f(x) = 1
  - Apply the diffusion operator U_s to the qubits, which amplifies the amplitude of the state that satisfies f(x) = 1
- Measure the qubits and obtain the state that satisfies f(x) = 1 with high probability

The oracle function U_f and the diffusion operator U_s are the key components of the algorithm, and they can be implemented using quantum gates.