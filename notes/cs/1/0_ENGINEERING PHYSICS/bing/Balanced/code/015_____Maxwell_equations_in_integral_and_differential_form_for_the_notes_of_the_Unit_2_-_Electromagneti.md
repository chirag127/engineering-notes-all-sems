# Maxwell equations in integral and differential form

- Maxwell equations are a set of four equations that describe the relationship between electric and magnetic fields, charges and currents.
- They are the foundation of electromagnetic theory and have many applications in physics and engineering.
- They can be written in two equivalent forms: the integral form and the differential form.

## Integral form

- The integral form of Maxwell equations can be used to make statements about a region of charge or current, by integrating the electric or magnetic field over a closed surface or a closed loop.
- The integral form of Maxwell equations are:

  - Gauss's law: The electric flux through any closed surface is equal to the net charge enclosed by the surface divided by the permittivity of free space.

    $$\oint_S \mathbf{E} \cdot d\mathbf{A} = \frac{Q}{\epsilon_0}$$

  - Gauss's law for magnetism: The magnetic flux through any closed surface is zero, which implies that there are no magnetic monopoles.

    $$\oint_S \mathbf{B} \cdot d\mathbf{A} = 0$$

  - Faraday's law of induction: The electromotive force (EMF) around any closed loop is equal to the negative rate of change of the magnetic flux through the loop.

    $$\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \int_S \mathbf{B} \cdot d\mathbf{A}$$

  - Ampere's circuital law with Maxwell's correction: The magnetic field around any closed loop is equal to the sum of the current enclosed by the loop and the displacement current, which is proportional to the rate of change of the electric flux through the loop.

    $$\oint_C \mathbf{B} \cdot d\mathbf{l} = \mu_0 \left( I + \epsilon_0 \frac{d}{dt} \int_S \mathbf{E} \cdot d\mathbf{A} \right)$$

- In these equations, $\mathbf{E}$ is the electric field, $\mathbf{B}$ is the magnetic field, $Q$ is the net charge, $I$ is the current, $\epsilon_0$ is the permittivity of free space, $\mu_0$ is the permeability of free space, $S$ is a closed surface, $C$ is a closed loop, and $d\mathbf{A}$ and $d\mathbf{l}$ are the differential surface and line elements, respectively.

## Differential form

- The differential form of Maxwell equations can be used to make local statements and evaluate Maxwell equations at individual points in space, by using the differential operators div and curl.
- The differential form of Maxwell equations are:

  - Gauss's law: The divergence of the electric field at any point is equal to the charge density at that point divided by the permittivity of free space.

    $$\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}$$

  - Gauss's law for magnetism: The divergence of the magnetic field at any point is zero, which implies that there are no magnetic monopoles.

    $$\nabla \cdot \mathbf{B} = 0$$

  - Faraday's law of induction: The curl of the electric field at any point is equal to the negative rate of change of the magnetic field at that point.

    $$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$

  - Ampere's circuital law with Maxwell's correction: The curl of the magnetic field at any point is equal to the sum of the current density and the displacement current density at that point, which is proportional to the rate of change of the electric field at that point.

    $$\nabla \times \mathbf{B} = \mu_0 \left( \mathbf{J} + \epsilon_0 \frac{\partial \mathbf{E}}{\partial t} \right)$$

- In these equations, $\mathbf{E}$ is the electric field, $\mathbf{B}$ is the magnetic field, $\rho$ is the charge density, $\mathbf{J}$ is the current density, $\epsilon_0$ is the permittivity of free space, $\mu