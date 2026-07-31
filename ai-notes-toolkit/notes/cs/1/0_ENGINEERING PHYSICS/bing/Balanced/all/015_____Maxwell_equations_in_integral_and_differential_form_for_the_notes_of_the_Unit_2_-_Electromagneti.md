# Maxwell equations in integral and differential form

Maxwell equations are a set of four equations that describe the relationship between electric and magnetic fields, charges, and currents. They are the foundation of electromagnetic theory and have many applications in physics and engineering.

## Integral form

The integral form of Maxwell equations can be used to make statements about a region of charge or current. They are:

- Gauss's law: The electric flux through any closed surface is equal to the net electric charge enclosed by the surface divided by the permittivity of free space. Mathematically,

$$\oint_S \mathbf{E} \cdot d\mathbf{A} = \frac{Q}{\epsilon_0}$$

where $\mathbf{E}$ is the electric field, $d\mathbf{A}$ is the differential area element, $Q$ is the net charge, and $\epsilon_0$ is the permittivity of free space.

- Gauss's law for magnetism: The magnetic flux through any closed surface is zero. This implies that there are no magnetic monopoles. Mathematically,

$$\oint_S \mathbf{B} \cdot d\mathbf{A} = 0$$

where $\mathbf{B}$ is the magnetic field.

- Faraday's law of induction: The electromotive force (EMF) around any closed loop is equal to the negative rate of change of the magnetic flux through the loop. This explains how a changing magnetic field can induce an electric current. Mathematically,

$$\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \int_S \mathbf{B} \cdot d\mathbf{A}$$

where $C$ is the closed loop, $d\mathbf{l}$ is the differential line element, and $S$ is the surface bounded by $C$.

- Ampere's circuital law: The magnetic field around any closed loop is proportional to the net current flowing through the loop plus the displacement current, which is proportional to the rate of change of the electric flux. This explains how a changing electric field can induce a magnetic field. Mathematically,

$$\oint_C \mathbf{B} \cdot d\mathbf{l} = \mu_0 \left( I + \epsilon_0 \frac{d}{dt} \int_S \mathbf{E} \cdot d\mathbf{A} \right)$$

where $\mu_0$ is the permeability of free space, $I$ is the net current, and $S$ is the surface bounded by $C$.

## Differential form

To make local statements and evaluate Maxwell equations at individual points in space, one can recast Maxwell equations in their differential form, which use the differential operators div and curl. They are:

- Gauss's law: The divergence of the electric field is equal to the electric charge density divided by the permittivity of free space. Mathematically,

$$\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}$$

where $\nabla \cdot$ is the divergence operator, and $\rho$ is the charge density.

- Gauss's law for magnetism: The divergence of the magnetic field is zero. This implies that there are no magnetic monopoles. Mathematically,

$$\nabla \cdot \mathbf{B} = 0$$

- Faraday's law of induction: The curl of the electric field is equal to the negative rate of change of the magnetic field. This explains how a changing magnetic field can induce an electric current. Mathematically,

$$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$

where $\nabla \times$ is the curl operator, and $\frac{\partial}{\partial t}$ is the partial derivative with respect to time.

- Ampere's circuital law: The curl of the magnetic field is equal to the current density plus the displacement current density, which is proportional to the rate of change of the electric field. This explains how a changing electric field can induce a magnetic field. Mathematically,

$$\nabla \times \mathbf{B} = \mu_0 \left( \mathbf{J} + \epsilon_0 \frac{\partial \mathbf{E}}{\partial t} \right)$$

where $\mathbf{