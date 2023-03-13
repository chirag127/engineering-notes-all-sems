### Time-dependent and time-independent Schrodinger wave equations for the notes of the Unit 1 - Quantum Mechanics in the subject of ENGINEERING PHYSICS

- The Schrodinger wave equation is a partial differential equation that describes the wave function of a quantum system, such as an electron, an atom, or a molecule.
- The wave function contains all the information about the physical state of the system, such as its position, momentum, energy, and spin.
- The Schrodinger wave equation can be written in two forms: time-dependent and time-independent.
- The time-dependent Schrodinger wave equation (TDSE) depicts a system that evolves over time and is thus dependent on the physical state of that system. The TDSE has the following expression:

$$
i\hbar \frac{\partial \psi(\mathbf{r},t)}{\partial t} = \hat{H} \psi(\mathbf{r},t)
$$

where $i$ is the imaginary unit, $\hbar$ is the reduced Planck constant, $\psi(\mathbf{r},t)$ is the wave function of the system as a function of position $\mathbf{r}$ and time $t$, and $\hat{H}$ is the Hamiltonian operator, which represents the total energy of the system.

- The time-independent Schrodinger wave equation (TISE) depicts a system that does not change over time and is thus independent of the physical state of that system. The TISE can be obtained from the TDSE by assuming that the wave function can be separated into two parts: a space-only part and a time-only part:

$$
\psi(\mathbf{r},t) = \psi(\mathbf{r}) e^{-iEt/\hbar}
$$

where $\psi(\mathbf{r})$ is the space-only part, $E$ is the total energy of the system, and $e^{-iEt/\hbar}$ is the time-only part.

- Substituting this expression into the TDSE and dividing both sides by $\psi(\mathbf{r},t)$, we get:

$$
i\hbar \frac{1}{\psi(\mathbf{r})} \frac{\partial \psi(\mathbf{r})}{\partial t} e^{-iEt/\hbar} + i\hbar \frac{1}{e^{-iEt/\hbar}} \frac{\partial e^{-iEt/\hbar}}{\partial t} = \frac{\hat{H} \psi(\mathbf{r}) e^{-iEt/\hbar}}{\psi(\mathbf{r}) e^{-iEt/\hbar}}
$$

- Simplifying and rearranging, we get:

$$
\frac{\hat{H} \psi(\mathbf{r})}{\psi(\mathbf{r})} = E + i\hbar \frac{1}{\psi(\mathbf{r})} \frac{\partial \psi(\mathbf{r})}{\partial t}
$$

- Since the left-hand side of this equation is independent of time, and the right-hand side is dependent on time, the only way for this equation to be true for all values of $t$ is if both sides are equal to a constant. We can choose this constant to be $E$, the total energy of the system. Therefore, we get:

$$
\hat{H} \psi(\mathbf{r}) = E \psi(\mathbf{r})
$$

which is the TISE.

- The TISE is an eigenvalue equation, which means that it has solutions only for certain values of $E$, called the eigenvalues, and corresponding functions $\psi(\mathbf{r})$, called the eigenfunctions. The eigenvalues represent the possible energy levels of the system, and the eigenfunctions represent the possible wave functions of the system at those energy levels.
- The TISE can be solved for different types of quantum systems, such as a particle in a box, a harmonic oscillator, a hydrogen atom, etc. The solutions depend on the form of the Hamiltonian operator, which in turn depends on the potential energy function of the system.
- The TDSE and the TISE are two ways of looking at the same quantum system. The TDSE describes how the system changes over time, while the TISE describes the stationary states of the system. The TDSE can be used to find the probability of finding the system in a certain state at a certain time, while the