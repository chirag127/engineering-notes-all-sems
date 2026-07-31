### Distance Measures for Quantum Information

- A distance measure quantifies the extent to which two quantum states behave in the same way or how distinguishable they are .
- A distance measure is represented by a two-argument function d: S(H) x S(H) -> R, where S(H) is the space of density matrices on a Hilbert space H and R is the set of real numbers.
- A distance measure is usually required to satisfy some basic properties, such as:
  - Positivity: d(ρ, σ) ≥ 0 with equality if and only if ρ = σ
  - Symmetry: d(ρ, σ) = d(σ, ρ)
  - Triangle inequality: d(ρ, τ) ≤ d(ρ, σ) + d(σ, τ)
  - Contractivity: d(E(ρ), E(σ)) ≤ d(ρ, σ) for any quantum operation E
- Some examples of distance measures for quantum information are:
  - Trace distance: d(ρ, σ) = (1/2) tr|ρ - σ|, where |A| = √(A†A) is the matrix norm. It gives the maximum probability of distinguishing two states by a single measurement .
  - Fidelity: F(ρ, σ) = tr√(√ρσ√ρ), where √ρ is the unique positive semidefinite matrix such that (√ρ)² = ρ. It gives the overlap between two states or the probability of success in state transition .
  - Quantum relative entropy: S(ρ||σ) = tr(ρ log ρ - ρ log σ), where log is the matrix logarithm. It gives the information gain or loss when replacing σ by ρ or the irreversibility of state transformation .
  - Bures distance: d(ρ, σ) = √(2 - 2 F(ρ, σ)), where F is the fidelity. It gives the minimal length of a curve connecting two states in the space of density matrices .