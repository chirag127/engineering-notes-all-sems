# Distance Measures for Quantum Information

- Distance measures are used to quantify the extent to which two quantum states behave in the same way or can be distinguished by measurements .
- Distance measures are also useful for evaluating the performance of quantum protocols, such as quantum error correction, quantum cryptography, and quantum metrology.
- A distance measure is a function that takes two quantum states as inputs and outputs a non-negative real number that satisfies some basic properties, such as positivity, symmetry, and triangle inequality.
- There are many different distance measures for quantum states, each with its own advantages and disadvantages. Some of the most common ones are:

  - **Trace distance**: This is the quantum generalization of the Kolmogorov distance for classical probability distributions. It is defined as the half of the trace norm of the difference between two density matrices. It has the operational meaning of being the maximum probability of distinguishing two states by a single measurement.
  - **Fidelity**: This is a measure of the overlap or similarity between two quantum states. It is defined as the square root of the product of the two density matrices, after taking the square root of one of them. It has the operational meaning of being the maximum probability of correctly identifying two states by a single measurement.
  - **Quantum relative entropy**: This is the quantum generalization of the Kullback-Leibler divergence for classical probability distributions. It is defined as the difference between the von Neumann entropy of one state and the cross entropy of the two states. It has the operational meaning of being the maximum amount of information that can be extracted from one state when the other state is given as a prior.
  - **Bures distance**: This is a measure of the distance between two quantum states based on the fidelity. It is defined as the square root of two minus the fidelity. It has the operational meaning of being the minimum amount of noise that needs to be added to one state to make it indistinguishable from the other state.

- These distance measures have different properties and applications, and they are related to each other by various inequalities and bounds. For example, the trace distance and the fidelity are related by the Fuchs-van de Graaf inequality:

  - $$T(\rho, \sigma) \leq \sqrt{1 - F(\rho, \sigma)^2}$$

- The quantum relative entropy and the trace distance are related by the Pinsker inequality:

  - $$D(\rho || \sigma) \geq \frac{1}{2} T(\rho, \sigma)^2$$

- The Bures distance and the fidelity are related by the Uhlmann inequality:

  - $$B(\rho, \sigma) \leq \sqrt{2 - 2 F(\rho, \sigma)}$$

- These inequalities can be used to compare and bound different distance measures for quantum states.