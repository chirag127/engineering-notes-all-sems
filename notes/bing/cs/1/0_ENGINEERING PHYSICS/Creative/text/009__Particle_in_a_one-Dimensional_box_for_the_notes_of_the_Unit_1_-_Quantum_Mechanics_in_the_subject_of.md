### Particle in a one-Dimensional box

- A particle in a one-dimensional box is a fundamental quantum mechanical approximation describing the translational motion of a single particle confined inside an infinitely deep well from which it cannot escape   .
- The walls of a one-dimensional box may be seen as regions of space with an infinitely large potential energy, so the particle cannot penetrate or tunnel through them.
- The potential energy of the particle inside the box is zero, and outside the box is infinite   .
- The one-dimensional box is defined by the interval [0, L], where L is the length of the box   .
- The Schrödinger equation for the particle in a one-dimensional box is given by:

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi$$

where $\hbar$ is the reduced Planck constant, $m$ is the mass of the particle, $x$ is the position coordinate, $\psi$ is the wavefunction, and $E$ is the energy of the particle   .

- The boundary conditions for the wavefunction are:

$$\psi(0) = \psi(L) = 0$$

which means that the wavefunction vanishes at the walls of the box   .

- The general solution of the Schrödinger equation is:

$$\psi(x) = A\sin(kx) + B\cos(kx)$$

where $A$ and $B$ are constants, and $k$ is the wave number given by:

$$k = \frac{\sqrt{2mE}}{\hbar}$$

- Applying the boundary conditions, we get:

$$B = 0$$

and

$$kL = n\pi$$

where $n$ is a positive integer   .

- The normalized wavefunction is then:

$$\psi_n(x) = \sqrt{\frac{2}{L}}\sin\left(\frac{n\pi x}{L}\right)$$

where $n = 1, 2, 3, ...$   .

- The energy of the particle is quantized, meaning that it can only take discrete values given by:

$$E_n = \frac{n^2\pi^2\hbar^2}{2mL^2}$$

where $n = 1, 2, 3, ...$   .

- The lowest energy state, called the ground state, corresponds to $n = 1$, and has an energy of:

$$E_1 = \frac{\pi^2\hbar^2}{2mL^2}$$

which is nonzero, unlike the classical case where the particle can have zero kinetic energy at rest   .

- The higher energy states, called the excited states, correspond to $n > 1$, and have increasing energy gaps as $n$ increases   .

- The probability density of finding the particle at a given position $x$ is given by:

$$|\psi_n(x)|^2 = \frac{2}{L}\sin^2\left(\frac{n\pi x}{L}\right)$$

which shows that the particle is more likely to be found near the center of the box for odd values of $n$, and near the edges of the box for even values of $n$   .

- The particle in a one-dimensional box model can be used to describe various physical phenomena, such as the electronic states of atoms and molecules, the vibrational modes of molecules, the energy levels of quantum dots, and the absorption and emission spectra of various materials  [^3