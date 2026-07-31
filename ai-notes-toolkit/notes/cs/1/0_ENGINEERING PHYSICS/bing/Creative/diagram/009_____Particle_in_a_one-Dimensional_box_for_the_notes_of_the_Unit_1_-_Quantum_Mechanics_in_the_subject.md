Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is a summary of the topic of particle in a one-dimensional box for the notes of the unit 1 - quantum mechanics in the subject of engineering physics.

### Particle in a one-dimensional box

- A particle in a one-dimensional box is a fundamental quantum mechanical approximation describing the translational motion of a single particle confined inside an infinitely deep well from which it cannot escape  .
- The potential energy of the particle is zero inside the box and infinite outside the box. The box has a length L and the particle can only move along the x-axis.
- The Schrödinger equation for the particle is given by:

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi$$

where $\hbar$ is the reduced Planck's constant, $m$ is the mass of the particle, $\psi$ is the wavefunction, and $E$ is the energy of the particle.
- The boundary conditions for the wavefunction are:

$$\psi(0) = \psi(L) = 0$$

which means that the wavefunction vanishes at the walls of the box.
- The general solution of the Schrödinger equation is:

$$\psi(x) = A\sin(kx) + B\cos(kx)$$

where $A$ and $B$ are constants and $k$ is the wave number given by:

$$k = \frac{\sqrt{2mE}}{\hbar}$$
- Applying the boundary conditions, we get:

$$B = 0$$

and

$$kL = n\pi$$

where $n$ is a positive integer.
- The normalized wavefunction is then:

$$\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)$$

where $n = 1, 2, 3, ...$
- The energy of the particle is quantized and given by:

$$E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}$$

where $n = 1, 2, 3, ...$
- The lowest energy state is called the ground state and has $n = 1$. The higher energy states are called the excited states and have $n > 1$.
- The probability density of finding the particle at a given position is given by:

$$|\psi_n(x)|^2 = \frac{2}{L}\sin^2\left(\frac{n\pi x}{L}\right)$$

which shows that the particle has zero probability of being found at the walls of the box and has maximum probability of being found at the center of the box for the ground state and at the nodes for the excited states.