## Unit 5 - Quantum Error Correction

Quantum error correction (QEC) is a technique to protect quantum information from errors due to decoherence and other quantum noise. QEC is essential to achieve fault-tolerant quantum computing that can reduce the effects of noise on stored quantum information, faulty quantum gates, faulty quantum preparation, and faulty measurements. 

QEC codes use entanglement to spread the information of one logical qubit onto several physical qubits. This way, the logical qubit can be recovered even if some of the physical qubits are corrupted by noise. QEC codes can be classified into different types, such as stabilizer codes, bosonic codes, topological codes, etc. 

One of the simplest QEC codes is the bit flip code, which can correct for errors that flip the state of a qubit from |0> to |1> or vice versa. The bit flip code encodes one logical qubit into three physical qubits using the following encoding circuit:

```
|0> ---[H]---[CNOT]---[CNOT]---|0L>
|0> ---[H]---|0> ---[CNOT]---|0L>
|0> ---[H]---|0> ---|0> ---|0L>
```

where H is the Hadamard gate and CNOT is the controlled-NOT gate. The logical qubit |0L> is the entangled state |000> + |111>, and the logical qubit |1L> is the entangled state |001> + |110>. If one of the physical qubits is flipped by noise, the logical qubit can be recovered by measuring the parity of the physical qubits and applying a correction if needed. The following diagram illustrates the basic architecture of a bit flip code:

```
|0L> ---[E]---[M]---[C]---|0L>
|0L> ---[E]---[M]---[C]---|0L>
|0L> ---[E]---[M]---[C]---|0L>
```

where E is the error channel, M is the parity measurement, and C is the correction. For example, if the error channel flips the first qubit, the state becomes |100> + |011>. The parity measurement will detect a mismatch between the first and second qubits, and the correction will flip the first qubit back to its original state, restoring the logical qubit |0L>.  

: Quantum error correction - Wikipedia
: Quantum Error Correction, an informal introduction