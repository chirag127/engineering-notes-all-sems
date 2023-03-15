### Particle in a one-dimensional box

- A particle in a one-dimensional box is a fundamental quantum mechanical approximation describing the translational motion of a single particle confined inside an infinitely deep well from which it cannot escape   .
- The walls of a one-dimensional box may be seen as regions of space with an infinitely large potential energy.
- The particle can only move along a straight line (the x-axis) with impenetrable barriers at either end (x = 0 and x = L).
- The potential energy of the particle is zero inside the box and infinite outside the box   .
- The potential energy function V(x) is given by:

```
V(x) = { 0, 0 < x < L
       { ∞, otherwise
```

- The Schrödinger equation for the particle is:

```
-ħ²/2m d²ψ/dx² + V(x)ψ = Eψ
```

- Where ħ is the reduced Planck constant, m is the mass of the particle, ψ is the wavefunction, and E is the energy of the particle   .
- To solve the Schrödinger equation, we need to apply the boundary conditions that ψ(0) = ψ(L) = 0, since the wavefunction must vanish outside the box   .
- The general solution of the Schrödinger equation is:

```
ψ(x) = A sin(kx) + B cos(kx)
```

- Where A and B are constants, and k is a wave number related to the energy by:

```
E = ħ²k²/2m
```

- Applying the boundary conditions, we get:

```
ψ(0) = A sin(0) + B cos(0) = B = 0
ψ(L) = A sin(kL) + B cos(kL) = A sin(kL) = 0
```

- The second equation implies that kL must be a multiple of π, or:

```
kL = nπ
```

- Where n is a positive integer   .
- Therefore, the wave number k and the energy E are quantized, meaning they can only take discrete values:

```
k = nπ/L
E = n²π²ħ²/2mL²
```

- The wavefunction ψ(x) is then given by:

```
ψ(x) = A sin(nπx/L)
```

- Where A is determined by the normalization condition:

```
∫|ψ(x)|² dx = 1
```

- Which gives:

```
A = √(2/L)
```

- The final solution for the wavefunction is:

```
ψ(x) = √(2/L) sin(nπx/L)
```

- The wavefunction ψ(x) represents the probability amplitude of finding the particle at a given position x   .
- The probability density |ψ(x)|² is the square of the wavefunction, and it shows the spatial distribution of the particle inside the box   .
- The probability density |ψ(x)|² has n-1 nodes, or points where it is zero, inside the box   .
- The quantum number n determines the energy level and the shape of the wavefunction of the particle   .
- The lowest energy level (n = 1) is called the ground state, and the higher energy levels (n > 1) are called the excited states   .
- The energy difference between two adjacent levels is:

```
ΔE = E(n+1) - E(n) = (n+1)²π²