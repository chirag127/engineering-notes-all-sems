### Time-dependent and time-independent Schrodinger wave equations

- The Schrodinger wave equation is a mathematical equation that describes the behavior of quantum mechanical systems, such as electrons, atoms, and molecules.
- The equation relates the wave function of the system, which is a complex-valued function that contains all the information about the system, to the energy and potential of the system, which are physical quantities that affect the system's dynamics.
- The equation can be written in two forms: the time-dependent form and the time-independent form.
- The time-dependent form of the Schrodinger wave equation is given by:

$$
i\hbar \frac{\partial \psi}{\partial t} = \hat{H} \psi
$$

where $i$ is the imaginary unit, $\hbar$ is the reduced Planck constant, $\psi$ is the wave function, $t$ is time, and $\hat{H}$ is the Hamiltonian operator, which represents the total energy of the system.

- The time-dependent form of the equation describes how the wave function changes over time, and is applicable to any quantum system, whether it is stationary or not.
- The time-independent form of the Schrodinger wave equation is obtained by assuming that the wave function can be separated into a product of a spatial part and a temporal part, such that:

$$
\psi(x,t) = \psi(x) e^{-i\omega t}
$$

where $x$ is the position, $\omega$ is the angular frequency, and $e^{-i\omega t}$ is a complex exponential function that oscillates with time.

- Substituting this form of the wave function into the time-dependent equation and dividing by $\psi(x)$, we get:

$$
i\hbar \frac{e^{-i\omega t}}{\psi(x)} \frac{\partial \psi(x)}{\partial t} = \hat{H} e^{-i\omega t}
$$

- Since the left-hand side of the equation depends only on time, and the right-hand side depends only on position, they must be equal to a constant, which we call $E$, the energy eigenvalue of the system. Thus, we have:

$$
i\hbar \frac{1}{e^{-i\omega t}} \frac{\partial e^{-i\omega t}}{\partial t} = E
$$

and

$$
\hat{H} \psi(x) = E \psi(x)
$$

- The first equation implies that $\omega = E/\hbar$, and the second equation is the time-independent form of the Schrodinger wave equation, which describes the spatial distribution of the wave function for a given energy level.
- The time-independent form of the equation is applicable to quantum systems that are in a stationary state, meaning that their energy and potential do not change over time.
- The solutions of the time-independent equation are called the eigenfunctions and eigenvalues of the Hamiltonian operator, and they form a complete set of basis functions that can be used to express any wave function of the system.