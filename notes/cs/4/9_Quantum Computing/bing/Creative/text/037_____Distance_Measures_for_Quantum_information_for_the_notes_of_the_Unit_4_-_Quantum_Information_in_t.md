### Distance Measures for Quantum Information

- A distance measure quantifies the extent to which two quantum states behave in the same way .
- A distance measure is related to the problem of distinguishing two systems, i.e., how well one can tell apart two quantum states by performing measurements .
- A distance measure is represented by a two-argument function d: S(H) x S(H) -> R, where S(H) is the set of density matrices on a Hilbert space H and R is the set of real numbers.
- A distance measure usually satisfies the following properties:
  - Positivity: d(ρ, σ) ≥ 0 with equality if and only if ρ = σ
  - Symmetry: d(ρ, σ) = d(σ, ρ)
  - Triangle inequality: d(ρ, τ) ≤ d(ρ, σ) + d(σ, τ)
  - Contractivity: d(E(ρ), E(σ)) ≤ d(ρ, σ) for any quantum operation E
- A distance measure that satisfies the above properties is called a metric.
- Some examples of distance measures for quantum information are   :
  - Trace distance: d_T(ρ, σ) = (1/2) tr|ρ - σ|, where |X| = (X^†X)^1/2 is the absolute value of X
  - Fidelity: F(ρ, σ) = tr(ρ^1/2σρ^1/2)^1/2
  - Quantum relative entropy: S(ρ||σ) = tr(ρ log ρ - ρ log σ)
  - Bures distance: d_B(ρ, σ) = 2(1 - F(ρ, σ))
  - Quantum Jensen-Shannon divergence: J(ρ||σ) = (1/2) S(ρ||(ρ + σ)/2) + (1/2) S(σ||(ρ + σ)/2)
- Different distance measures have different operational meanings and applications in quantum information theory, such as quantum state estimation, quantum hypothesis testing, quantum error correction, quantum cryptography, etc  .