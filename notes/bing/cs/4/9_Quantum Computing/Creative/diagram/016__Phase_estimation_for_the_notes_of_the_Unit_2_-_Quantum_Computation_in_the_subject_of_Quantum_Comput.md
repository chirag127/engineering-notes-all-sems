Phase estimation is a quantum algorithm to estimate the phase or eigenvalue of an eigenvector of a unitary operator. It is a central building block for many quantum algorithms, such as Shor's algorithm, quantum Fourier transform, and quantum simulation. The basic idea of the algorithm is to use a quantum register of n qubits to store the phase information of the unitary operator, and then apply a series of controlled unitary operations and inverse quantum Fourier transforms to extract the phase estimation.

The following diagram illustrates the basic architecture of a phase estimation algorithm using markdown syntax:

```
|0> ---H---U^(2^0)---*----------------------*----------------------*---QFT^-1---|phi_0>
|0> ---H---U^(2^1)---|---U^(2^0)---*--------|--------*-------------|---QFT^-1---|phi_1>
|0> ---H---U^(2^2)---|---U^(2^1)---|---U^(2^0)---*---|---*---------|---QFT^-1---|phi_2>
|0> ---H---U^(2^3)---|---U^(2^2)---|---U^(2^1)---|---U^(2^0)---*---|---QFT^-1---|phi_3>
|psi>----------------|-------------|-------------|-------------|---U^(2^0)---|psi>
```

Here, H is the Hadamard gate, U is the unitary operator, QFT^-1 is the inverse quantum Fourier transform, and |psi> is the eigenvector of U with eigenvalue e^(2*pi*i*theta). The phase estimation algorithm outputs the n-bit approximation of theta as |phi> = |phi_0 phi_1 phi_2 phi_3>. The accuracy of the estimation depends on the number of qubits in the quantum register and the choice of U.