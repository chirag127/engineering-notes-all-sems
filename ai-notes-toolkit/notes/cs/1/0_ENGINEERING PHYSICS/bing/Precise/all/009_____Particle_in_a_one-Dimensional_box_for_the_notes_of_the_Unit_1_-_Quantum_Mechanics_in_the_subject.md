# Particle in a One-Dimensional Box

The particle in a one-dimensional box is a fundamental problem in quantum mechanics. It is used to illustrate the basic principles of quantum mechanics and is often used as a starting point for more complex problems.

The problem involves a particle that is confined to a one-dimensional box of length L. The potential energy of the particle is zero inside the box and infinite outside the box. This means that the particle is free to move inside the box, but cannot escape from it.

The wave function of the particle must satisfy the Schrödinger equation, which can be written as:

`-ħ²/2m * d²ψ(x)/dx² + V(x)ψ(x) = Eψ(x)`

where ħ is the reduced Planck constant, m is the mass of the particle, V(x) is the potential energy, and E is the total energy of the particle.

Since the potential energy is zero inside the box, the Schrödinger equation can be simplified to:

`-ħ²/2m * d²ψ(x)/dx² = Eψ(x)`

This is a second-order differential equation, which has the general solution:

`ψ(x) = A * sin(kx) + B * cos(kx)`

where A and B are constants and k is a constant related to the energy of the particle.

The boundary conditions of the problem require that the wave function must be zero at the edges of the box, i.e., ψ(0) = ψ(L) = 0. This means that B must be zero and that k must satisfy the condition:

`kL = nπ`

where n is a positive integer.

The energy of the particle is given by:

`E = ħ²k²/2m = n²π²ħ²/2mL²`

This shows that the energy of the particle is quantized, i.e., it can only take on certain discrete values. The lowest energy state, called the ground state, corresponds to n = 1. The energy of the ground state is:

`E₁ = π²ħ²/2mL²`

The next energy level, called the first excited state, corresponds to n = 2. The energy of the first excited state is:

`E₂ = 4π²ħ²/2mL²`

In general, the energy of the nth excited state is:

`Eₙ = n²π²ħ²/2mL²`

The wave function of the particle in the nth energy state is given by:

`ψₙ(x) = √(2/L) * sin(nπx/L)`
