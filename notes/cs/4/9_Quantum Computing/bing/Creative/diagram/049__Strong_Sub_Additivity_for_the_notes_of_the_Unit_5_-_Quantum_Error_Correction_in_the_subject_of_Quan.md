According to the Wikipedia article on Strong subadditivity of quantum entropy, the relation is defined as follows:

Let A, B, and C be three quantum systems, and let ρ_ABC be a density matrix on the tensor product H_A ⊗ H_B ⊗ H_C. Then the strong subadditivity (SSA) of quantum entropy is the inequality:

S(ρ_AB) + S(ρ_BC) ≥ S(ρ_ABC) + S(ρ_B)

where S(ρ) is the von Neumann entropy of ρ.

A possible ASCII diagram to illustrate this relation is:

    +-----------------+-----------------+
    |                 |                 |
    |        A        |        B        |
    |                 |                 |
    +-----------------+-----------------+-----------------+
    |                 |                 |                 |
    |        B        |        C        |        A        |
    |                 |                 |                 |
    +-----------------+-----------------+-----------------+
    |                 |                 |
    |        C        |        A        |
    |                 |                 |
    +-----------------+-----------------+

The diagram shows the three quantum systems A, B, and C, and their tensor products AB, BC, and CA. The SSA inequality can be interpreted as saying that the total entropy of AB and BC is greater than or equal to the total entropy of ABC and B. This means that the entropy of B cannot be reduced by splitting ABC into AB and BC, or equivalently, that the correlation between A and C cannot be increased by splitting ABC into AB and BC. This is a non-trivial property of quantum entropy that does not hold for classical entropy.