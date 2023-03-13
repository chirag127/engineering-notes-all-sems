The following is a detailed ASCII diagram for distance measures for quantum information for the notes of the Unit 4 - Quantum Information in the subject of Quantum Computing.

### Distance Measures for Quantum Information

Distance measures are used to quantify the extent to which two quantum states behave in the same way. They are related to the problem of distinguishing two systems. There are various ways of introducing a notion of distance between two quantum states, such as the trace distance, the fidelity, the quantum relative entropy, and the Bures distance. Each of these distance measures has different properties and operational meanings.

The following diagram illustrates the basic definitions and relations of some of the distance measures for quantum states.

```
+----------------+  +----------------+  +----------------+  +----------------+
| Trace distance |  |   Fidelity     |  | Quantum        |  | Bures distance |
|                |  |                |  | relative       |  |                |
| T(ρ, σ) =      |  | F(ρ, σ) =      |  | entropy        |  | D(ρ, σ) =      |
| 1/2 ||ρ - σ||  |  | tr √(ρ^(1/2)σ  |  | S(ρ||σ) =      |  | √2(1 - F(ρ, σ))|
|                |  | ρ^(1/2))       |  | -tr(ρ log σ)   |  |                |
|                |  |                |  |                |  |                |
|                |  |                |  |                |  |                |
|                |  |                |  |                |  |                |
+----------------+  +----------------+  +----------------+  +----------------+
       |                   |                   |                   |
       |                   |                   |                   |
       |                   |                   |                   |
       |                   |                   |                   |
       |                   |                   |                   |
       |                   |                   |                   |
       |                   |                   |                   |
       |                   |                   |                   |
       |                   |                   |                   |
       |                   |                   |                   |
       |                   |                   |                   |
       |                   |                   |                   |
       |                   |                   |                   |
       |                   |                   |                   |
       |                   |                   |                   |
       |                   |                   |                   |
       |                   |                   |                   |
       |                   |                   |                   |
       |                   |                   |                   |
       +-------------------+-------------------+-------------------+
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   |
                                   +----------------+
                                   | Distinguish-   |
                                   | ability        |
                                   |                |
                                   | P(ρ, σ) =      |
                                   | 1/2 + 1/4 T(ρ, |
                                   | σ)             |
                                   |                |
                                   |                |
                                   |                |
                                   +----------------+
```

The trace distance is a metric on the space of density matrices and gives a measure of the distinguishability between two states. It is the quantum generalization of the Kolmogorov distance for classical probability distributions.

The fidelity is a measure of the overlap between two quantum states. It is related to the probability of success of the optimal state discrimination protocol.

The quantum relative entropy is a measure of the information gain or loss when using one quantum state instead of another. It is related to the data processing inequality and the quantum hypothesis testing.

The Bures distance is a measure of the statistical distance between two quantum states. It is related to the quantum Fisher information and the quantum Cramér-Rao bound.

The distinguishability is a measure of the probability of correctly identifying two quantum states given a single copy of either one. It is related to the Helstrom measurement and the quantum Chernoff bound.