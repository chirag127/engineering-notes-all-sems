### Distance Measures for Quantum Information for the Notes of the Unit 4 - Quantum Information in the Subject of Quantum Computing

- Distance measures for quantum information are used to quantify how close or how distinguishable two quantum states are. They are widely used in the theory of quantum information processing and quantum cryptography  .
- A distance measure is a function that takes two quantum states as inputs and outputs a non-negative real number that represents their distance. A distance measure should satisfy some basic properties, such as positivity, symmetry, and triangle inequality. These properties make a distance measure a metric on the space of quantum states  .
- There are various ways of introducing a distance measure for quantum states, depending on the operational meaning or the mathematical expression of the measure. Some of the most common distance measures are:

  - **Trace distance**: The trace distance between two quantum states ρ and σ is defined as

    T(ρ, σ) = (1/2) tr|ρ - σ|,

    where |ρ - σ| is the absolute value of the difference of the two density matrices, i.e., the positive square root of (ρ - σ)^(†)(ρ - σ). The trace distance is the quantum generalization of the Kolmogorov distance for classical probability distributions. It has the following properties  :

      - It is bounded by 0 and 1, i.e., 0 ≤ T(ρ, σ) ≤ 1, with equality if and only if ρ = σ or ρ and σ are orthogonal, respectively.
      - It is contractive under quantum operations, i.e., if Λ is a completely positive and trace-preserving (CPTP) map, then T(Λ(ρ), Λ(σ)) ≤ T(ρ, σ) for any ρ and σ. This means that quantum operations cannot increase the distinguishability of quantum states.
      - It is related to the fidelity F(ρ, σ) by the Fuchs-van de Graaf inequality, i.e.,

        1 - √F(ρ, σ) ≤ T(ρ, σ) ≤ √1 - F(ρ, σ).

      - It is related to the probability of distinguishing two quantum states by a single measurement, i.e.,

        (1/2) + (1/4) T(ρ, σ) ≤ P(ρ, σ) ≤ (1/2) T(ρ, σ),

        where P(ρ, σ) is the optimal probability of correctly identifying ρ or σ when they are given with equal prior probabilities.

  - **Fidelity**: The fidelity between two quantum states ρ and σ is defined as

    F(ρ, σ) = tr|√ρ √σ|^(2),

    where √ρ and √σ are the positive square roots of the density matrices. The fidelity is a measure of how similar two quantum states are. It has the following properties  :

      - It is bounded by 0 and 1, i.e., 0 ≤ F(ρ, σ) ≤ 1, with equality if and only if ρ = σ or ρ and σ are orthogonal, respectively.
      - It is invariant under unitary transformations, i.e., if U is a unitary operator, then F(UρU^(†), UσU^(†)) = F(ρ, σ) for any ρ and σ. This means that fidelity does not depend on the choice of basis or the phase of the quantum states.
      - It is monotonic under quantum operations, i.e., if Λ is a CPTP map, then F(Λ(ρ), Λ(σ)) ≤ F(ρ, σ) for any ρ and σ. This means that quantum operations cannot increase the similarity of quantum states.
      - It is related to the trace distance T(ρ, σ) by the Fuchs-van de Graaf inequality, as mentioned above.
      - It is related to the probability of successfully transforming one quantum state into another by a single quantum operation, i.e.,

        F(ρ, σ) ≤ P(ρ → σ) ≤ √F(ρ, σ),

        where P(ρ → σ) is the optimal probability of transforming ρ into σ by a CPTP map.

  - **Relative entropy**: The relative entropy between two quantum states ρ and σ is defined