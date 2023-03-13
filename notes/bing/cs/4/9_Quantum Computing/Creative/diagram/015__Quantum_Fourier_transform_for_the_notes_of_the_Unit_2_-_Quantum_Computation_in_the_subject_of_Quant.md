The quantum Fourier transform (QFT) is the quantum implementation of the discrete Fourier transform over the amplitudes of a quantum state. It is part of many quantum algorithms, most notably Shor's factoring algorithm and quantum phase estimation. The QFT can be implemented using Hadamard gates and controlled phase shift gates. The following diagram illustrates the basic architecture of a QFT circuit for n qubits:

### Quantum Fourier transform

```
|0> ---H---R2---R3---...---Rn---SWAP---|y0>
|0> ---H---R2---R3---...---Rn-1---SWAP---|y1>
|0> ---H---R2---R3---...---SWAP---|y2>
|0> ---H---R2---...---SWAP---|y3>
|0> ---H---...---SWAP---|y4>
|0> ---...---SWAP---|y5>
|0> ---...---|yn-1>
```

Where H is the Hadamard gate, Rk is the controlled phase shift gate with angle 2π/2^k, and SWAP is the swap gate that exchanges the qubits. The input state is |0>^n and the output state is |y0y1...yn-1>, which is the QFT of the input state. The QFT circuit can be decomposed into smaller subcircuits that perform the QFT on smaller subsets of qubits. The QFT circuit has a complexity of O(n^2) gates.