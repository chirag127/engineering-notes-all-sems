# Distance Measures for Quantum Information

- Distance measures are used to quantify the extent to which two quantum states behave in the same way or how distinguishable they are .
- Distance measures are represented by two-argument functions that map pairs of quantum states to real numbers.
- Distance measures usually satisfy some basic properties, such as positivity, symmetry, triangle inequality, and monotonicity.
- Some common distance measures for quantum states are:
  - Trace distance: the maximum probability of distinguishing two states by a single measurement . It is defined as $$T(\rho, \sigma) = \frac{1}{2} \mathrm{Tr}|\rho - \sigma|$$ where $|\rho - \sigma|$ is the absolute value of the difference of the two density matrices.
  - Fidelity: the overlap or similarity between two states . It is defined as $$F(\rho, \sigma) = \mathrm{Tr} \sqrt{\sqrt{\rho} \sigma \sqrt{\rho}}$$ for mixed states and $$F(\psi, \phi) = |\langle \psi | \phi \rangle|^2$$ for pure states.
  - Quantum relative entropy: the information divergence or the amount of information lost when one state is approximated by another state . It is defined as $$S(\rho || \sigma) = \mathrm{Tr}(\rho \log \rho - \rho \log \sigma)$$ where $\log$ is the logarithm to base 2.
  - Bures distance: the geodesic distance between two states on the manifold of density matrices. It is defined as $$D_B(\rho, \sigma) = \sqrt{2 - 2 \sqrt{F(\rho, \sigma)}}$$ where $F$ is the fidelity.