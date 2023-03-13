The following is a detailed ASCII diagram for strong subadditivity of quantum entropy for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing.

Strong subadditivity of quantum entropy (SSA) is the relation among the von Neumann entropies of various quantum subsystems of a larger quantum system consisting of three subsystems (or of one quantum system with three degrees of freedom) . It is a basic theorem in modern quantum information theory .

The SSA states that for any tripartite quantum state ρ_ABC, the following inequality holds :

S(AB) + S(BC) ≥ S(ABC) + S(B)

where S(X) denotes the von Neumann entropy of the reduced state ρ_X obtained by tracing out the other subsystems .

The SSA implies subadditivity, namely that S(A) + S(B) ≥ S(AB), which is another way of saying that the quantum mutual information is always positive. To see this result, just make the state on system "B" pure.

The SSA can be illustrated by the following ASCII diagram :

```
+-----------------+-----------------+
|                 |                 |
|                 |                 |
|                 |                 |
|        A        |        B        |
|                 |                 |
|                 |                 |
|                 |                 |
+-----------------+-----------------+
|                 |                 |
|                 |                 |
|                 |                 |
|        C        |                 |
|                 |                 |
|                 |                 |
|                 |                 |
+-----------------+-----------------+
```

The diagram shows the three subsystems A, B, and C of the larger quantum system ABC. The SSA states that the sum of the entropies of the regions AB and BC (the shaded areas) is greater than or equal to the sum of the entropies of the regions ABC and B (the whole rectangle and the middle column) .

```
+-----------------+-----------------+
|                 |                 |
|                 |                 |
|                 |                 |
|        A        |        B        |
|                 |                 |
|                 |                 |
|                 |                 |
+-----------------+-----------------+
|                 |                 |
|                 |                 |
|                 |                 |
|        C        |                 |
|                 |                 |
|                 |                 |
|                 |                 |
+-----------------+-----------------+
|                 |                 |
|                 |                 |
|                 |                 |
|                 |                 |
|                 |                 |
|                 |                 |
|                 |                 |
+-----------------+-----------------+
```

The SSA has many applications and implications in quantum information theory, such as quantum error correction, quantum cryptography, quantum entanglement, quantum thermodynamics, and quantum complexity theory  .