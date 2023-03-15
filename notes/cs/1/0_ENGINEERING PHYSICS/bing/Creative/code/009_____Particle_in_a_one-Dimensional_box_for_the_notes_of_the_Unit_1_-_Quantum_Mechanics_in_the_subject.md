Hello, I am Sydney, your AI assistant. I can help you with your study material. Here is the content I have generated for the topic of particle in a one-dimensional box for the notes of the unit 1 - quantum mechanics in the subject of engineering physics.

### Particle in a one-dimensional box

- A particle in a one-dimensional box is a fundamental quantum mechanical approximation describing the translational motion of a single particle confined inside an infinitely deep well from which it cannot escape  .
- The potential energy of the particle is zero inside the box and infinite outside the box. The box has a length L and the particle can only move along the x-axis.
- The Schrödinger equation for the particle is given by:

```math
-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} = E\psi
```

where $\hbar$ is the reduced Planck constant, $m$ is the mass of the particle, $\psi$ is the wavefunction of the particle, and $E$ is the energy of the particle.

- The boundary conditions for the wavefunction are:

```math
\psi(0) = \psi(L) = 0
```

which means that the wavefunction vanishes at the walls of the box.

- The general solution of the Schrödinger equation is:

```math
\psi(x) = A\sin(kx) + B\cos(kx)
```

where $A$ and $B$ are constants and $k$ is the wave number of the particle.

- Applying the boundary conditions, we get:

```math
\psi(0) = A\sin(0) + B\cos(0) = B = 0
```

and

```math
\psi(L) = A\sin(kL) + B\cos(kL) = A\sin(kL) = 0
```

which implies that

```math
kL = n\pi
```

where $n$ is a positive integer.

- Therefore, the wavefunction of the particle is:

```math
\psi_n(x) = A_n\sin(\frac{n\pi x}{L})
```

where $A_n$ is a normalization constant and $n$ is the quantum number of the particle.

- The energy of the particle is given by:

```math
E_n = \frac{\hbar^2 k^2}{2m} = \frac{\hbar^2 n^2 \pi^2}{2mL^2}
```

which shows that the energy is quantized and depends on the quantum number $n$.

- The lowest energy state is called the ground state and has $n = 1$. The higher energy states are called the excited states and have $n > 1$.

- The probability density of finding the particle at a given position $x$ is given by:

```math
|\psi_n(x)|^2 = |A_n|^2 \sin^2(\frac{n\pi x}{L})
```

which shows that the particle has zero probability of being found outside the box and has a sinusoidal distribution inside the box.

- The particle in a one-dimensional box is a simple model that illustrates some of the basic concepts of quantum mechanics, such as the wave-particle duality, the uncertainty principle, the quantization of energy, and the superposition of states.