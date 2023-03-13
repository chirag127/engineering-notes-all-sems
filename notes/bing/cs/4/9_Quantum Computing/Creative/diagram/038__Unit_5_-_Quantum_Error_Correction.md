## Unit 5 - Quantum Error Correction

Quantum error correction (QEC) is a technique to protect quantum information from errors due to decoherence, noise, and faulty operations. QEC involves encoding a logical qubit into a larger number of physical qubits, and performing measurements and corrections to detect and correct errors.

One of the simplest QEC codes is the three-qubit bit-flip code, which can correct a single bit-flip error in a logical qubit. The encoding circuit for this code is:

```
|0> ---[H]---[CNOT]---[CNOT]---|0>
|0> ---[H]---|0> ---[CNOT]---|0>
|0> ---[H]---|0> ---|0> ---[CNOT]---|0>
```

where H is the Hadamard gate and CNOT is the controlled-NOT gate. The logical qubit is encoded into the state |000> + |111>, which is a superposition of three physical qubits. If a bit-flip error occurs on any of the physical qubits, the logical qubit can be recovered by measuring the parity of the first and second qubits, and the parity of the second and third qubits. The parity measurement circuit is:

```
|0> ---[H]---[CNOT]---[CNOT]---|0> ---[CNOT]---[H]---[M]
|0> ---[H]---|0> ---[CNOT]---|0> ---[CNOT]---|0> ---[M]
|0> ---[H]---|0> ---|0> ---[CNOT]---|0> ---|0> ---|0>
```

where M is the measurement gate. The measurement outcomes indicate the location of the error, and the correction can be done by applying a bit-flip gate (X) to the corresponding qubit. The correction circuit is:

```
|0> ---[H]---[CNOT]---[CNOT]---|0> ---[CNOT]---[H]---[M]---[X]---|0>
|0> ---[H]---|0> ---[CNOT]---|0> ---[CNOT]---|0> ---[M]---[X]---|0>
|0> ---[H]---|0> ---|0> ---[CNOT]---|0> ---|0> ---|0> ---[X]---|0>
```

The following diagram illustrates the basic architecture of a quantum error correction protocol:

```
  Logical qubit
    |
    | Encoding
    V
  Physical qubits
    |
    | Error
    V
  Corrupted qubits
    |
    | Syndrome measurement
    V
  Parity qubits
    |
    | Correction
    V
  Recovered qubits
    |
    | Decoding
    V
  Logical qubit
```