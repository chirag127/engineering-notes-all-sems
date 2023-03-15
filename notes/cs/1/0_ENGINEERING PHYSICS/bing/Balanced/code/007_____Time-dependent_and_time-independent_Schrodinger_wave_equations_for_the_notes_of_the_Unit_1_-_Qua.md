```markdown
### Time-dependent and time-independent Schrodinger wave equations

- The Schrodinger wave equation is a partial differential equation that describes the quantum state of a physical system.
- The quantum state is represented by a complex-valued wave function that depends on the spatial coordinates and time of the system.
- The Schrodinger wave equation can be written in two forms: time-dependent and time-independent.

#### Time-dependent Schrodinger wave equation

- The time-dependent Schrodinger wave equation (TDSE) depicts a system that evolves over time and is thus dependent on the physical state of that system.
- The TDSE has the following expression:

$$
i\hbar \frac{\partial \psi(\mathbf{r},t)}{\partial t} = \hat{H} \psi(\mathbf{r},t)
$$

- where $i$ is the imaginary unit, $\hbar$ is the reduced Planck constant, $\psi(\mathbf{r},t)$ is the wave function, $\hat{H}$ is the Hamiltonian operator, $\mathbf{r}$ is the position vector, and $t$ is the time.
- The Hamiltonian operator is the total energy operator of the system, which consists of the kinetic and potential energy operators:

$$
\hat{H} = \hat{T} + \hat{V}
$$

- The TDSE can be derived from the equation that describes the motion of a wave in classical mechanics:

$$
\psi(\mathbf{r},t) = \exp\left[i(\mathbf{k} \cdot \mathbf{r} - \omega t)\right]
$$

- where $\mathbf{k}$ is the wave vector, and $\omega$ is the angular frequency of the wave.
- By applying the momentum and energy operators to the wave function, and equating them to the corresponding eigenvalues, we obtain the TDSE.

#### Time-independent Schrodinger wave equation

- The time-independent Schrodinger wave equation (TISE) describes a system that does not change over time and is thus independent of the physical state of that system.
- The TISE can be obtained from the TDSE by using the method of separation of variables, which assumes that the wave function can be written as a product of a space-only function and a time-only function:

$$
\psi(\mathbf{r},t) = \psi(\mathbf{r})\phi(t)
$$

- By substituting this into the TDSE, and dividing both sides by $\psi(\mathbf{r},t)$, we obtain:

$$
i\hbar \frac{1}{\phi(t)} \frac{d\phi(t)}{dt} = \frac{1}{\psi(\mathbf{r})} \hat{H} \psi(\mathbf{r})
$$

- Since the left-hand side depends only on time, and the right-hand side depends only on space, they must be equal to a constant, which we denote by $E$, the total energy of the system.
- This gives us two ordinary differential equations:

$$
i\hbar \frac{d\phi(t)}{dt} = E \phi(t)
$$

$$
\hat{H} \psi(\mathbf{r}) = E \psi(\mathbf{r})
$$

- The first equation can be easily solved to give:

$$
\phi(t) = \exp\left(-\frac{iEt}{\hbar}\right)
$$

- The second equation is the TISE, which has the following expression:

$$
\hat{H} \psi(\mathbf{r}) = E \psi(\mathbf{r})
$$

- The TISE is an eigenvalue equation, where the eigenvalues are the possible energy levels of the system, and the eigenfunctions are the corresponding stationary states or wave functions.
- The TISE can be solved for different types of potentials, such as the harmonic oscillator, the hydrogen atom, the infinite square well, etc.
- The solutions of the TISE are important as they form a complete basis for the Hilbert space of the system, and any state can be expressed as a linear combination of them.
```