### Distance Measures for Quantum Information

Distance measures are used to quantify the extent to which two quantum states behave in the same way. These measures are usually given by certain mathematical expressions and often possess a simple operational meaning, i.e., they are related to the problem of distinguishing two systems .

In mathematical terms, a distance measure is represented by a two-argument function d: S(H) × S(H) → R. The basic properties associated with a distance measure d are that it is a metric, i.e., it satisfies positivity: d(ρ, σ) ≥ 0 with equality if and only if ρ = σ.

In quantum mechanics, and especially quantum information and the study of open quantum systems, the trace distance T is a metric on the space of density matrices and gives a measure of the distinguishability between two states. It is the quantum generalization of the Kolmogorov distance for classical probability distributions.

Given that quantum systems suffer noise in practice, distance measures can be used to determine how well a protocol is performing. The simplest way to do so is to compare the output of an ideal protocol to the output of the actual protocol using a distance measure of the two respective output quantum states.

Both information divergence and distance are measures of closeness of two quantum states which are widely used in the theory of information processing and quantum cryptography. For example, the quantum relative entropy and trace distance are well known.