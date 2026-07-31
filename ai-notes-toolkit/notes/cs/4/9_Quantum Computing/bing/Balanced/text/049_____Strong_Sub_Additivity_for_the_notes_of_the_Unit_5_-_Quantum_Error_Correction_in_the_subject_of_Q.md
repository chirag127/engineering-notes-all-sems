### Strong Subadditivity for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Strong subadditivity (SSA) of quantum entropy is a fundamental theorem in quantum information theory that relates the von Neumann entropies of different quantum subsystems of a larger quantum system .
- SSA states that for any tripartite quantum state rho _ {ABC}, the following inequality holds:

  S(rho _ {AB}) + S(rho _ {BC}) <= S(rho _ {A}) + S(rho _ {ABC})

  where S(rho) is the von Neumann entropy of the state rho.

- SSA implies that the mutual information between two quantum systems A and B cannot increase by adding a third system C, i.e.,

  I(A:B) >= I(A:B|C)

  where I(A:B) = S(rho _ {A}) + S(rho _ {B}) - S(rho _ {AB}) is the mutual information between A and B, and I(A:B|C) = S(rho _ {AC}) + S(rho _ {BC}) - S(rho _ {ABC}) - S(rho _ {C}) is the conditional mutual information between A and B given C.

- SSA has many applications in quantum information theory, such as bounding the quantum capacity of noisy channels, proving the security of quantum cryptography protocols, and characterizing the entanglement properties of quantum states .