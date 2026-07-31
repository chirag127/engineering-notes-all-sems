### Maxwell equations in integral and differential form

Maxwell equations are a set of four equations that describe the relationship between electric and magnetic fields, charges and currents. They are the foundation of electromagnetic theory and have many applications in physics and engineering.

The integral form of Maxwell equations can be used to make statements about a region of charge or current, by integrating the fields over a closed surface or a closed loop. The differential form of Maxwell equations can be used to make statements about individual points in space, by using the differential operators div and curl.

The integral and differential forms of Maxwell equations are equivalent, and can be derived from each other using the Gauss's divergence theorem and the Stokes' theorem.

The integral form of Maxwell equations are:

- Gauss's law: The electric flux through any closed surface is equal to the net charge enclosed by the surface divided by the permittivity of free space. Mathematically,

$$\oint_S \mathbf{E} \cdot d\mathbf{A} = \frac{Q}{\epsilon_0}$$

where $\mathbf{E}$ is the electric field, $d\mathbf{A}$ is the differential area element, $Q$ is the net charge and $\epsilon_0$ is the permittivity of free space.

- Gauss's law for magnetism: The magnetic flux through any closed surface is zero, implying that there are no magnetic monopoles. Mathematically,

$$\oint_S \mathbf{B} \cdot d\mathbf{A} = 0$$

where $\mathbf{B}$ is the magnetic field.

- Faraday's law of induction: The electromotive force (EMF) around any closed loop is equal to the negative rate of change of magnetic flux through the loop. Mathematically,

$$\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \int_S \mathbf{B} \cdot d\mathbf{A}$$

where $d\mathbf{l}$ is the differential length element, and $C$ and $S$ are the loop and the surface bounded by the loop, respectively.

- Ampere's circuital law with Maxwell's correction: The magnetic field around any closed loop is equal to the sum of the current enclosed by the loop and the displacement current, which is proportional to the rate of change of electric flux. Mathematically,

$$\oint_C \mathbf{B} \cdot d\mathbf{l} = \mu_0 \left( I + \epsilon_0 \frac{d}{dt} \int_S \mathbf{E} \cdot d\mathbf{A} \right)$$

where $\mu_0$ is the permeability of free space, and $I$ is the current.

The differential form of Maxwell equations are:

- Gauss's law: The divergence of the electric field at any point is equal to the charge density at that point divided by the permittivity of free space. Mathematically,

$$\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}$$

where $\nabla \cdot$ is the divergence operator, and $\rho$ is the charge density.

- Gauss's law for magnetism: The divergence of the magnetic field at any point is zero, implying that there are no magnetic monopoles. Mathematically,

$$\nabla \cdot \mathbf{B} = 0$$

- Faraday's law of induction: The curl of the electric field at any point is equal to the negative rate of change of the magnetic field at that point. Mathematically,

$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$

where $\nabla \times$ is the curl operator, and $\frac{\partial}{\partial t}$ is the partial derivative with respect to time.

- Ampere's circuital law with Maxwell's correction: The curl of the magnetic field at any point is equal to the sum of the current density and the displacement current density at that point. Mathematically,

$$\nabla \times \mathbf{B} = \mu_0 \left( \mathbf{J} + \epsilon_0 \frac{\partial \mathbf{E}}{\partial t} \right)$$

where $\mathbf{J}$ is the current density, and $\epsilon_0 \frac