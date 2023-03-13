Nuclear magnetic resonance quantum computing (NMRQC) is one of the several proposed approaches for constructing a quantum computer, that uses the spin states of nuclei within molecules as qubits. The quantum states are probed through the nuclear magnetic resonances, allowing the system to be implemented as a variation of nuclear magnetic resonance spectroscopy.

A basic diagram of a NMR quantum computer is shown below, using the example of a 5-qubit system based on the molecule of alanine. The qubits are implemented by the spin states of the carbon atoms, which are labeled as C1, C2, C3, C4, and C5. The hydrogen atoms are not used as qubits, but they provide the coupling between the carbon atoms. The diagram shows the structure of the molecule, the spin states of the nuclei, the coupling constants between the nuclei, and the radio frequency pulses that are used to manipulate the qubits.

```
    H1
    |
    C1 - H2
    |    |
    C2 - H3
    |
    C3 - H4
    |
    C4 - H5
    |
    C5 - H6
    |
    H7

    C1: |0> or |1>
    C2: |0> or |1>
    C3: |0> or |1>
    C4: |0> or |1>
    C5: |0> or |1>

    Coupling constants (in Hz):
    J(C1,C2) = 35.1
    J(C2,C3) = 54.5
    J(C3,C4) = 35.1
    J(C4,C5) = 54.5

    Radio frequency pulses (in MHz):
    C1: 125.76
    C2: 125.77
    C3: 125.78
    C4: 125.79
    C5: 125.80
```

The radio frequency pulses are applied to the nuclei through a probe head, which is a device that generates and detects the magnetic fields. The probe head can also measure the signal from the nuclei, which is used to read out the final state of the qubits.

The NMR quantum computer can perform various quantum algorithms, such as quantum Fourier transform, Grover's search, Shor's factoring, and quantum machine learning. However, the NMR quantum computer also faces some limitations, such as the scalability, the decoherence, and the signal-to-noise ratio. Therefore, the NMR quantum computer is mainly used as a proof-of-principle demonstration of quantum information processing, rather than a practical device for large-scale computation.