### Quantum Bits for the notes of the Unit 1 - Fundamental Concepts in the subject of Quantum Computing

- A quantum bit, or qubit, is the basic unit of quantum information in quantum computing. It is the quantum analog of the classical bit, which can store either 0 or 1.  
- Unlike a classical bit, a qubit can exist in a superposition of both 0 and 1 states, meaning that it can have a certain probability of being 0 and a certain probability of being 1 at the same time.  
- A qubit can be represented by a two-dimensional column vector of unit norm, that is, the magnitude squared of its entries must sum to 1.   For example, a qubit can be written as:

  [α β] [ α β]

  where α and β are complex numbers satisfying |α|2 +|β|2 = 1 | α | 2 + | β | 2 = 1.

- The two basis vectors for the qubit's state space are [1 0] [ 1 0] and [0 1] [ 0 1], which correspond to the classical states 0 and 1, respectively. These are also called the computational basis states.  
- Any qubit state can be expressed as a linear combination of the basis states, that is:

  [α β] = α[1 0] + β[0 1] [ α β] = α [ 1 0] + β [ 0 1]

  where α and β are complex coefficients called amplitudes.

- When a qubit is measured, it collapses to one of the basis states with a probability given by the square of the amplitude.   For example, if a qubit is in the state:

  [α β] = 1/√2[1 0] + 1/√2[0 1] [ α β] = 1 / 2 [ 1 0] + 1 / 2 [ 0 1]

  then the probability of measuring 0 is |1/√2|2 = 1/2 | 1 / 2 | 2 = 1 / 2 and the probability of measuring 1 is |1/√2|2 = 1/2 | 1 / 2 | 2 = 1 / 2.

- A qubit can be manipulated by applying quantum gates, which are unitary matrices that act on the qubit's state vector.   For example, the NOT gate, which flips the qubit from 0 to 1 and vice versa, is represented by the matrix:

  X = [0 1] [1 0] X = [ 0 1 ] [ 1 0 ]

  and the Hadamard gate, which creates a superposition of 0 and 1 with equal probabilities, is represented by the matrix:

  H = 1/√2[1 1] [1 -1] H = 1 / 2 [ 1 1 ] [ 1 − 1 ]

- A qubit can also be visualized using the Bloch sphere, which is a unit sphere with the north pole representing the state [1 0] [ 1 0] and the south pole representing the state [0 1] [ 0 1]. Any other state can be represented by a point on the surface of the sphere, with the angle θ θ from the north pole indicating the relative amplitude of 0 and 1, and the angle ϕ ϕ from the x-axis indicating the relative phase of 0 and 1.   For example, the state:

  [α β] = cos(θ/2)[1 0] + eiϕsin(θ/2)[0 1] [ α β] = cos ( θ / 2) [ 1 0] + e i ϕ sin ( θ / 2) [ 0 1]

  can be represented by the point with coordinates (θ, ϕ) ( θ, ϕ) on the Bloch sphere.

- A mnemonic to remember the Bloch sphere representation