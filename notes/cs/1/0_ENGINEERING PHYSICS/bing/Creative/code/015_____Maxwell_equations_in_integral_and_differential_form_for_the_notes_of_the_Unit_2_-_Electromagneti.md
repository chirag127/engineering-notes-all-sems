# Maxwell equations in integral and differential form

Maxwell equations are a set of four equations that describe the relationship between electric and magnetic fields, charges and currents. They are the foundation of electromagnetic theory and have many applications in physics and engineering.

The integral form of Maxwell equations can be used to make statements about a region of charge or current, by integrating the fields over a closed surface or a closed loop. The differential form of Maxwell equations can be used to make statements about individual points in space, by using the differential operators div and curl.

The integral and differential forms of Maxwell equations are equivalent, and can be derived from each other using the Gauss's divergence theorem and the Stokes' theorem.

The integral form of Maxwell equations are:

- Gauss's law: The electric flux through any closed surface is equal to the net charge enclosed by the surface divided by the permittivity of free space.

$$\oint_S \mathbf{E} \cdot d\mathbf{A} = \frac{Q}{\epsilon_0}$$

- Gauss's law for magnetism: The magnetic flux through any closed surface is zero, which implies that there are no magnetic monopoles.

$$\oint_S \mathbf{B} \cdot d\mathbf{A} = 0$$

- Faraday's law of induction: The electromotive force around any closed loop is equal to the negative rate of change of the magnetic flux through the loop.

$$\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \int_S \mathbf{B} \cdot d\mathbf{A}$$

- Ampere's law with Maxwell's correction: The magnetic field around any closed loop is equal to the sum of the current enclosed by the loop and the displacement current, which is proportional to the rate of change of the electric flux.

$$\oint_C \mathbf{B} \cdot d\mathbf{l} = \mu_0 \left( I + \epsilon_0 \frac{d}{dt} \int_S \mathbf{E} \cdot d\mathbf{A} \right)$$

The differential form of Maxwell equations are:

- Gauss's law: The divergence of the electric field at any point is equal to the charge density at that point divided by the permittivity of free space.

$$\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}$$

- Gauss's law for magnetism: The divergence of the magnetic field at any point is zero, which implies that there are no magnetic monopoles.

$$\nabla \cdot \mathbf{B} = 0$$

- Faraday's law of induction: The curl of the electric field at any point is equal to the negative rate of change of the magnetic field at that point.

$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$

- Ampere's law with Maxwell's correction: The curl of the magnetic field at any point is equal to the sum of the current density and the displacement current density, which is proportional to the rate of change of the electric field.

$$\nabla \times \mathbf{B} = \mu_0 \left( \mathbf{J} + \epsilon_0 \frac{\partial \mathbf{E}}{\partial t} \right)$$