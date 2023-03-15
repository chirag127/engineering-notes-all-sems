### Maxwell equations in integral and differential form

Maxwell equations are a set of four equations that describe the relationship between electric and magnetic fields, charges, and currents. They are the foundation of electromagnetic theory and have many applications in physics and engineering.

The integral form of Maxwell equations can be used to make statements about a region of charge or current, by integrating the fields over a closed surface or a closed loop. The differential form of Maxwell equations can be used to make statements about individual points in space, by using the differential operators div and curl.

The integral and differential forms of Maxwell equations are equivalent, and can be derived from each other using the Gauss's divergence theorem and the Stokes' theorem. Here are the integral and differential forms of Maxwell equations, along with their physical meanings and names:

- Gauss's law for electricity: The electric flux through any closed surface is equal to the net charge enclosed by the surface, divided by the permittivity of free space. This law states that electric charges are the sources of electric fields.

  - Integral form: $$\oint_S \mathbf{E} \cdot d\mathbf{A} = \frac{Q}{\epsilon_0}$$
  - Differential form: $$\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}$$

- Gauss's law for magnetism: The magnetic flux through any closed surface is zero. This law states that there are no magnetic charges or monopoles, and that magnetic fields are always solenoidal.

  - Integral form: $$\oint_S \mathbf{B} \cdot d\mathbf{A} = 0$$
  - Differential form: $$\nabla \cdot \mathbf{B} = 0$$

- Faraday's law of induction: The electromotive force (EMF) around any closed loop is equal to the negative rate of change of the magnetic flux through the loop. This law states that a changing magnetic field induces an electric field.

  - Integral form: $$\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d\Phi_B}{dt}$$
  - Differential form: $$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$

- Ampere's circuital law with Maxwell's correction: The magnetic field around any closed loop is equal to the sum of the current enclosed by the loop, multiplied by the permeability of free space, and the displacement current, which is the rate of change of the electric flux through the loop, multiplied by the permittivity of free space. This law states that electric currents and changing electric fields are the sources of magnetic fields.

  - Integral form: $$\oint_C \mathbf{B} \cdot d\mathbf{l} = \mu_0 \left( I + \epsilon_0 \frac{d\Phi_E}{dt} \right)$$
  - Differential form: $$\nabla \times \mathbf{B} = \mu_0 \left( \mathbf{J} + \epsilon_0 \frac{\partial \mathbf{E}}{\partial t} \right)$$

These equations can be written in a more compact and elegant way using the tensor notation, where $\mathbf{F}$ is the electromagnetic field tensor, $\mathbf{J}$ is the four-current vector, and $\partial_\mu$ is the four-gradient operator:

$$\partial_\mu F^{\mu \nu} = \mu_0 J^\nu$$

This form of Maxwell equations is invariant under the Lorentz transformations, and is compatible with the special theory of relativity.