### Distance Measures for Quantum Information

- A distance measure quantifies the extent to which two quantum states behave in the same way .
- A distance measure is related to the problem of distinguishing two systems, i.e., how well one can tell them apart by performing measurements .
- A distance measure is a function d that maps two quantum states to a real number, i.e., d:\u2004S (H)\u2005×\u2005S (H)\u2004→\u2004R, where S (H) is the set of density matrices on a Hilbert space H.
- A distance measure is usually required to satisfy some basic properties, such as:
  - Positivity: d(ρ, σ)\u2004≥\u20040 with equality if and only if ρ = σ
  - Symmetry: d(ρ, σ) = d(σ, ρ)
  - Triangle inequality: d(ρ, τ) ≤ d(ρ, σ) + d(σ, τ)
  - Monotonicity: d(ρ, σ) ≥ d(E(ρ), E(σ)) for any trace-preserving quantum operation E .
- Some examples of distance measures for quantum information are:
  - Trace distance: T(ρ, σ) = (1/2) tr|ρ - σ|, where |A| = √(A†A) is the matrix norm. It gives the maximum probability of distinguishing ρ and σ by a single measurement .
  - Fidelity: F(ρ, σ) = tr√(√ρσ√ρ). It gives the minimum probability of error in distinguishing ρ and σ by a single measurement.
  - Quantum relative entropy: S(ρ||σ) = tr(ρ log ρ - ρ log σ). It measures the inefficiency of using σ instead of ρ as a resource for information processing .
  - Bures distance: D(ρ, σ) = √(2 - 2 F(ρ, σ)). It measures the statistical distance between two quantum states in terms of their purities.