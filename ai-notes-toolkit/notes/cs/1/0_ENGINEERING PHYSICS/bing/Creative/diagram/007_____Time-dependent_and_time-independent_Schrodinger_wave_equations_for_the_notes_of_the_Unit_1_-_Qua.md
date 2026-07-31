### Time-dependent and time-independent Schrodinger wave equations

- The Schrodinger wave equation is a partial differential equation that describes the quantum state of a physical system.
- The equation can be written in two forms: the time-dependent form and the time-independent form.
- The time-dependent form depicts a system that evolves over time and is thus dependent on the physical state of that system. The time-dependent form of Schrodinger's wave equation has the following expression:

$$
i\hbar\frac{\partial \psi(\mathbf{r},t)}{\partial t} = \hat{H}\psi(\mathbf{r},t)
$$

- where $i$ is the imaginary unit, $\hbar$ is the reduced Planck constant, $\psi(\mathbf{r},t)$ is the wave function of the system, and $\hat{H}$ is the Hamiltonian operator, which represents the total energy of the system.
- The time-dependent form can be solved for any initial condition and any potential function, but it is often difficult to do so analytically.
- The time-independent form assumes that the system is in a stationary state, meaning that the wave function does not change with time, except for a phase factor. The time-independent form of Schrodinger's wave equation has the following expression:

$$
\hat{H}\psi(\mathbf{r}) = E\psi(\mathbf{r})
$$

- where $E$ is the energy eigenvalue of the stationary state, and $\psi(\mathbf{r})$ is the corresponding eigenfunction of the Hamiltonian operator.
- The time-independent form is an eigenvalue problem, which can be solved for discrete or continuous values of $E$ and $\psi(\mathbf{r})$, depending on the nature of the potential function.
- The time-independent form can be derived from the time-dependent form by using the separation of variables technique, which assumes that the wave function can be written as a product of a space-only function and a time-only function:

$$
\psi(\mathbf{r},t) = \psi(\mathbf{r})e^{-i\omega t}
$$

- where $\omega$ is the angular frequency of the wave. Plugging this ansatz in the time-dependent Schrodinger equation, we get the time-independent Schrodinger equation:

$$
\hat{H}\psi(\mathbf{r}) = \hbar\omega\psi(\mathbf{r})
$$

- where we identify $E = \hbar\omega$ as the energy eigenvalue of the stationary state.
- The time-independent form is simpler to solve than the time-dependent form, and it gives us the possible energy levels and wave functions of the system. However, it does not tell us how the system transitions from one state to another, or how it responds to external perturbations. For that, we need to use the time-dependent form.