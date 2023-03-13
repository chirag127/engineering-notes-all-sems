### Particle in a one-Dimensional box for the notes of the Unit 1 - Quantum Mechanics in the subject of ENGINEERING PHYSICS

- A particle in a one-dimensional box is a simple model that describes the quantum mechanical behavior of a particle confined in a rigid box of length L.
- The potential energy of the particle is zero inside the box and infinite outside the box, so the particle cannot escape the box.
- The Schrödinger equation for the particle in the box is given by

```
-d^2ψ/dx^2 = (2mE/ħ^2)ψ
```

where ψ is the wave function of the particle, m is its mass, E is its energy, and ħ is the reduced Planck constant.

- The boundary conditions for the wave function are ψ(0) = ψ(L) = 0, which means the wave function vanishes at the walls of the box.
- The general solution of the Schrödinger equation is

```
ψ(x) = A sin(kx) + B cos(kx)
```

where A and B are constants and k is the wave number.

- Applying the boundary conditions, we get B = 0 and k = nπ/L, where n is a positive integer.
- The normalized wave function is then

```
ψ(x) = sqrt(2/L) sin(nπx/L)
```

where n = 1, 2, 3, ...

- The energy of the particle is given by

```
E = ħ^2k^2/2m = n^2π^2ħ^2/2mL^2
```

where n = 1, 2, 3, ...

- The energy levels are discrete and depend on the size of the box and the quantum number n.
- The lowest energy level is E1 = π^2ħ^2/2mL^2, which is called the ground state.
- The energy difference between two adjacent levels is ΔE = (n+1)^2π^2ħ^2/2mL^2 - n^2π^2ħ^2/2mL^2 = (2n+1)π^2ħ^2/2mL^2, which is constant for large n.
- The probability density of finding the particle at a given position x is given by

```
P(x) = |ψ(x)|^2 = 2/L sin^2(nπx/L)
```

- The probability density has n-1 nodes, or points where it is zero, inside the box.
- The probability density is symmetric about the center of the box, x = L/2.
- The expectation value of the position of the particle is given by

```
<x> = int_0^L x P(x) dx = L/2
```

which means the particle is most likely to be found at the center of the box.
- The expectation value of the momentum of the particle is given by

```
<p> = -iħ int_0^L ψ*(x) dψ/dx dx = 0
```

which means the particle has no net momentum in the box.
- The uncertainty in the position of the particle is given by

```
Δx = sqrt(<x^2> - <x>^2) = L/sqrt(12) sqrt(1 - 6/n^2π^2)
```

which means the particle is more localized for higher n.
- The uncertainty in the momentum of the particle is given by

```
Δp = sqrt(<p^2> - <p>^2) = ħ sqrt(n^2π^2/3 - 2/L^2)
```

which means the particle has more momentum spread for higher n.
- The uncertainty principle for the particle in the box is given by

```
Δx Δp >= ħ/2
```

which is satisfied for all n.

- Some mnemonics and learning tricks for the particle in a box are:

  - The wave function is a sine wave with n peaks inside the box, where n is the quantum number.
  - The energy is proportional to n^2, where n is the quantum number.
  - The probability density is a sine-squared function with n-1 nodes inside the box, where n is the quantum number.
  - The expectation value of the position is always L/2, where L is the length of the box.
  - The expectation value of the momentum is always zero.
  - The uncertainty