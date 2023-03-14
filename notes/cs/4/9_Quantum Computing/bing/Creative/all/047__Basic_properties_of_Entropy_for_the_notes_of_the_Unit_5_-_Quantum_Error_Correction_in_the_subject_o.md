### Basic properties of Entropy for the notes of the Unit 5 - Quantum Error Correction in the subject of Quantum Computing

- Entropy is a measure of the uncertainty and the information content in the state of a physical system. It quantifies the resources necessary to store or transmit information.
- In classical information theory, the Shannon entropy of an ensemble of letters is defined as the average number of bits needed to encode each letter. It is given by the formula:

  `H(A) = - sum(p(ax) * log(p(ax)))`

  where `p(ax)` is the probability of letter `ax` and `log` is base-2.

- In quantum information theory, the von Neumann entropy of a quantum state is defined as the average number of qubits needed to encode the state. It is given by the formula:

  `S(rho) = - tr(rho * log(rho))`

  where `rho` is the density matrix of the state and `tr` is the trace operator.

- The von Neumann entropy generalizes the Shannon entropy to quantum systems. It satisfies the following properties:

  - It is non-negative: `S(rho) >= 0` for any state `rho`.
  - It is zero for pure states: `S(rho) = 0` if and only if `rho` is a rank-1 matrix.
  - It is concave: `S(sum(p(i) * rho(i))) >= sum(p(i) * S(rho(i)))` for any convex combination of states `rho(i)`.
  - It is continuous: `S(rho) -> S(sigma)` as `rho -> sigma` in the trace norm.
  - It is invariant under unitary transformations: `S(U * rho * U^dagger) = S(rho)` for any unitary matrix `U`.
  - It is subadditive: `S(rho_AB) <= S(rho_A) + S(rho_B)` for any bipartite state `rho_AB`.
  - It is additive: `S(rho_AB) = S(rho_A) + S(rho_B)` if and only if `rho_AB` is a product state.

- The von Neumann entropy can be used to quantify the entanglement of a quantum state. The entanglement of formation of a bipartite state `rho_AB` is defined as the minimum average entropy of the reduced states of the subsystems A and B over all possible pure state decompositions of `rho_AB`. It is given by the formula:

  `E(rho_AB) = min(sum(p(i) * S(rho_A(i))))`

  where the minimum is taken over all ensembles `{p(i), psi_AB(i)}` such that `rho_AB = sum(p(i) * psi_AB(i) * psi_AB(i)^dagger)`.

- The von Neumann entropy can also be used to measure the quantum error correction capacity of a quantum channel. A quantum channel is a linear map that transforms a quantum state into another quantum state, possibly with some noise or decoherence. The quantum error correction capacity of a channel is the maximum rate at which quantum information can be reliably transmitted through the channel using quantum error correction codes. It is given by the formula:

  `Q(E) = max(S(rho) - S(E(rho)))`

  where the maximum is taken over all input states `rho` and `E` is the channel.

- A mnemonic to remember the formula for the von Neumann entropy is to think of it as the negative trace of the "log matrix" of the state. A log matrix is a matrix whose entries are the logarithms of the original matrix entries. For example, the log matrix of `[[1/2, 0], [0, 1/2]]` is `[[log(1/2), 0], [0, log(1/2)]]`. The trace of a matrix is the sum of its diagonal entries. The negative sign is to make the entropy non-negative.