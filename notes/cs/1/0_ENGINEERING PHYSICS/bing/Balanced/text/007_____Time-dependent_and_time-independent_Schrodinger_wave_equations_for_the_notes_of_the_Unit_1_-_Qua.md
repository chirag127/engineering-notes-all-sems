### Time-dependent and time-independent Schrodinger wave equations

- The Schrodinger wave equation is a partial differential equation that describes the quantum state of a physical system.
- The equation can be written in two forms: time-dependent and time-independent.
- The time-dependent Schrodinger equation (TDSE) applies to a system that evolves over time and is affected by the potential energy of the system. The TDSE has the following expression:

$$
i\hbar \frac{\partial \psi(\mathbf{r},t)}{\partial t} = \hat{H} \psi(\mathbf{r},t)
$$

where $\psi(\mathbf{r},t)$ is the wave function of the system, $\hat{H}$ is the Hamiltonian operator, $i$ is the imaginary unit, and $\hbar$ is the reduced Planck constant.

- The time-independent Schrodinger equation (TISE) applies to a system that does not change over time and has a constant potential energy. The TISE can be derived from the TDSE by using the separation of variables method, assuming that the wave function can be written as a product of a spatial function and a temporal function :

$$
\psi(\mathbf{r},t) = \psi(\mathbf{r}) e^{-i\omega t}
$$

where $\psi(\mathbf{r})$ is the spatial part of the wave function, $\omega$ is the angular frequency, and $e^{-i\omega t}$ is the temporal part of the wave function.

- Plugging this ansatz in the TDSE, we get the TISE:

$$
\hat{H} \psi(\mathbf{r}) = E \psi(\mathbf{r})
$$

where $E$ is the energy eigenvalue of the system, and $\psi(\mathbf{r})$ is the energy eigenfunction of the system.

- The TISE is an eigenvalue problem that can be solved for the allowed energy levels and the corresponding wave functions of the system. The TISE is simpler to solve than the TDSE, but it only applies to stationary states, which are states that do not change over time. The TDSE can describe any state of the system, including superpositions of stationary states.