# Time-dependent and time-independent Schrodinger wave equations

- The Schrodinger wave equation is a partial differential equation that describes the quantum state of a physical system.
- The quantum state is represented by a complex-valued wave function that depends on the spatial coordinates and time of the system.
- The Schrodinger wave equation can be written in two forms: time-dependent and time-independent.

## Time-dependent Schrodinger wave equation

- The time-dependent Schrodinger wave equation is the general form of the equation that applies to any quantum system that evolves over time.
- The time-dependent Schrodinger wave equation has the following expression:

$$
i\hbar \frac{\partial \psi(\mathbf{r},t)}{\partial t} = \hat{H} \psi(\mathbf{r},t)
$$

- Where $i$ is the imaginary unit, $\hbar$ is the reduced Planck constant, $\psi(\mathbf{r},t)$ is the wave function, $\hat{H}$ is the Hamiltonian operator, $\mathbf{r}$ is the position vector, and $t$ is the time.
- The Hamiltonian operator is the total energy operator of the system, which consists of the kinetic and potential energy operators.
- The time-dependent Schrodinger wave equation is a linear equation, which means that any linear combination of solutions is also a solution.
- The time-dependent Schrodinger wave equation is also a unitary equation, which means that it preserves the normalization and probability of the wave function.

## Time-independent Schrodinger wave equation

- The time-independent Schrodinger wave equation is a special case of the time-dependent Schrodinger wave equation that applies to quantum systems that do not change over time, or are in a stationary state.
- A stationary state is a quantum state that has a definite energy and a wave function that oscillates in time with a fixed frequency.
- The time-independent Schrodinger wave equation can be obtained by using the separation of variables method on the time-dependent Schrodinger wave equation, assuming that the wave function can be written as a product of a spatial part and a temporal part:

$$
\psi(\mathbf{r},t) = \psi(\mathbf{r}) e^{-i\omega t}
$$

- Where $\psi(\mathbf{r})$ is the spatial part, $e^{-i\omega t}$ is the temporal part, and $\omega$ is the angular frequency of the wave function.
- Plugging this ansatz in the time-dependent Schrodinger equation, you get the so-called time-independent Schrodinger equation:

$$
\hat{H} \psi(\mathbf{r}) = E \psi(\mathbf{r})
$$

- Where $E$ is the energy of the stationary state, which is related to the angular frequency by $E = \hbar \omega$.
- The time-independent Schrodinger equation is an eigenvalue problem, so solving for $E$ and $\psi(\mathbf{r})$ will give you the energies for which a stationary state exists, as well as the wave functions of the said states.
- The time-independent Schrodinger equation is also a Hermitian equation, which means that it has real eigenvalues and orthogonal eigenfunctions.