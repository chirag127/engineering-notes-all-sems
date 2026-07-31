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

- where $i$ is the imaginary unit, $\hbar$ is the reduced Planck constant, $\psi(\mathbf{r},t)$ is the wave function of the system, $\hat{H}$ is the Hamiltonian operator that represents the total energy of the system, $\mathbf{r}$ is the position vector, and $t$ is the time.
- The Hamiltonian operator can be written as the sum of the kinetic energy operator and the potential energy operator:

$$
\hat{H} = \hat{T} + \hat{V}
$$

- For a single particle of mass $m$ in three dimensions, the kinetic energy operator is given by:

$$
\hat{T} = -\frac{\hbar^2}{2m} \nabla^2
$$

- where $\nabla^2$ is the Laplacian operator. The potential energy operator depends on the specific system and the external forces acting on the particle.
- The time-dependent Schrodinger wave equation is a linear equation, which means that if $\psi_1(\mathbf{r},t)$ and $\psi_2(\mathbf{r},t)$ are solutions, then any linear combination of them is also a solution:

$$
\psi(\mathbf{r},t) = c_1 \psi_1(\mathbf{r},t) + c_2 \psi_2(\mathbf{r},t)
$$

- where $c_1$ and $c_2$ are complex constants.

## Time-independent Schrodinger wave equation

- The time-independent Schrodinger wave equation is a special case of the time-dependent Schrodinger wave equation that applies to quantum systems that do not change over time, or are in a stationary state.
- A stationary state is a quantum state that has a definite energy and does not evolve over time.
- To find the stationary states of a quantum system, we can use the method of separation of variables, which assumes that the wave function can be written as the product of a spatial part and a temporal part:

$$
\psi(\mathbf{r},t) = \psi(\mathbf{r}) \phi(t)
$$

- Plugging this ansatz into the time-dependent Schrodinger wave equation, we get:

$$
i\hbar \frac{\partial}{\partial t} (\psi(\mathbf{r}) \phi(t)) = \hat{H} (\psi(\mathbf{r}) \phi(t))
$$

- Dividing both sides by $\psi(\mathbf{r}) \phi(t)$, we get:

$$
i\hbar \frac{1}{\phi(t)} \frac{\partial \phi(t)}{\partial t} = \frac{1}{\psi(\mathbf{r})} \hat{H} \psi(\mathbf{r})
$$

- The left-hand side of this equation depends only on time, while the right-hand side depends only on space. Since they are equal, they must be equal to a constant, which we call $E$, the energy of the stationary state:

$$
i\hbar \frac{1}{\phi(t)} \frac{\partial \phi(t)}{\partial t} = E = \frac{1}{\psi(\mathbf{r})} \hat{H} \psi(\mathbf{r})
$$

- Solving for $\phi(t)$, we get:

$$
\phi(t) = e^{-iEt/\hbar}
$$

- Solving for $\psi(\mathbf{r})$, we get the time-independent Schrodinger wave equation[^1^