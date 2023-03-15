# Particle in a one-dimensional box

- A particle in a one-dimensional box is a fundamental quantum mechanical approximation describing the translational motion of a single particle confined inside an infinitely deep well from which it cannot escape  .
- The simplest form of the particle in a box model considers a one-dimensional system. Here, the particle may only move backwards and forwards along a straight line with impenetrable barriers at either end. The walls of a one-dimensional box may be seen as regions of space with an infinitely large potential energy.
- The particle in a box model can be used to explain various phenomena, such as the absorption spectra of conjugated molecules, the electronic structure of quantum dots, and the quantum confinement of electrons in nanowires.
- The particle in a box model can be solved by applying the Schrödinger equation, which is a differential equation that relates the wavefunction of the particle to its energy and potential. The wavefunction is a mathematical function that describes the probability of finding the particle at a given position and time.
- The solution of the Schrödinger equation for the particle in a box model involves the following steps:
  - Step 1: Define the potential energy V. A particle in a 1D infinite potential well of dimension L. The potential energy is zero inside the box and infinite outside the box.
  - Step 2: Solve the Schrödinger equation. The Schrödinger equation can be written as:

  ```
  -h^2/(2m) d^2ψ/dx^2 + Vψ = Eψ
  ```

  where h is the Planck constant, m is the mass of the particle, ψ is the wavefunction, x is the position, V is the potential energy, and E is the energy. The equation can be simplified by separating the regions where V is zero and where V is infinite.
  - Step 3: Define the wavefunction. The solution to the Schrödinger equation we found above is the general form of the wavefunction:

  ```
  ψ(x) = A sin(kx) + B cos(kx)
  ```

  where A and B are constants, and k is the wave number, which is related to the energy by:

  ```
  E = h^2k^2/(8m)
  ```

  - Step 4: Apply the boundary conditions. The wavefunction must satisfy the boundary conditions that ψ(0) = 0 and ψ(L) = 0, which means that the particle cannot exist outside the box. These conditions imply that B = 0 and k = nπ/L, where n is a positive integer. Therefore, the wavefunction becomes:

  ```
  ψ(x) = A sin(nπx/L)
  ```

  - Step 5: Normalize the wavefunction. The wavefunction must be normalized, which means that the integral of the square of the wavefunction over the entire space must be equal to one. This condition ensures that the total probability of finding the particle is one. The normalization condition gives:

  ```
  ∫|ψ(x)|^2 dx = 1
  ```

  which leads to:

  ```
  A = √(2/L)
  ```

  Therefore, the final form of the wavefunction is:

  ```
  ψ(x) = √(2/L) sin(nπx/L)
  ```

  - Step 6: Find the energy levels. The energy levels of the particle are given by substituting the value of k into the energy equation:

  ```
  E = h^2k^2/(8m) = h^2n^2π^2/(8mL^2)
  ```

  where n is a positive integer. The energy levels are discrete and quantized, which means that the particle can only have certain values of energy and not any value in between. The energy levels depend on the size of the box and the mass of the particle. The lowest energy level is called the ground state, and the higher energy levels are called the excited states. The energy difference between two adjacent levels is:

  ```
  ΔE = h^2π^2/(8mL^2)
  ```

  which is independent of n. This means that the energy levels are equally spaced. The energy difference is also inversely proportional to the mass of the particle and the square of the length of the box. This