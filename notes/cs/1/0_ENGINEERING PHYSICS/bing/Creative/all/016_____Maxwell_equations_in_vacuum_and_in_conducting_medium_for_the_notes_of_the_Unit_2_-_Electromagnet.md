# Maxwell equations in vacuum and in conducting medium

- Maxwell equations are a set of four partial differential equations that describe the relationship between electric and magnetic fields in space and time.
- They are derived from the conservation laws of electric charge and magnetic flux, as well as the experimental laws of Faraday, Ampere and Gauss.
- Maxwell equations can be written in two forms: integral and differential. The integral form relates the flux or circulation of the fields through a closed surface or loop to the enclosed charge or current. The differential form relates the divergence or curl of the fields at a point to the charge or current density at that point.
- Maxwell equations in vacuum are:

  - Gauss's law for electricity: $$\oint_S \mathbf{E} \cdot d\mathbf{A} = \frac{Q}{\epsilon_0}$$ or $$\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}$$
  - Gauss's law for magnetism: $$\oint_S \mathbf{B} \cdot d\mathbf{A} = 0$$ or $$\nabla \cdot \mathbf{B} = 0$$
  - Faraday's law of induction: $$\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \int_S \mathbf{B} \cdot d\mathbf{A}$$ or $$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$
  - Ampere-Maxwell law: $$\oint_C \mathbf{B} \cdot d\mathbf{l} = \mu_0 I + \mu_0 \epsilon_0 \frac{d}{dt} \int_S \mathbf{E} \cdot d\mathbf{A}$$ or $$\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}$$

  where $\mathbf{E}$ is the electric field, $\mathbf{B}$ is the magnetic field, $\mathbf{J}$ is the electric current density, $\rho$ is the electric charge density, $\epsilon_0$ is the permittivity of free space, $\mu_0$ is the permeability of free space, $Q$ is the total electric charge, $I$ is the total electric current, $S$ is a closed surface, $C$ is a closed loop, and $d\mathbf{A}$ and $d\mathbf{l}$ are the differential area and length elements.

- Maxwell equations in a conducting medium are:

  - Gauss's law for electricity: $$\oint_S \mathbf{D} \cdot d\mathbf{A} = Q_f$$ or $$\nabla \cdot \mathbf{D} = \rho_f$$
  - Gauss's law for magnetism: $$\oint_S \mathbf{B} \cdot d\mathbf{A} = 0$$ or $$\nabla \cdot \mathbf{B} = 0$$
  - Faraday's law of induction: $$\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \int_S \mathbf{B} \cdot d\mathbf{A}$$ or $$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$
  - Ampere-Maxwell law: $$\oint_C \mathbf{H} \cdot d\mathbf{l} = I_f + \frac{d}{dt} \int_S \mathbf{D} \cdot d\mathbf{A}$$ or $$\nabla \times \mathbf{H} = \mathbf{J}_f + \frac{\partial \mathbf{D}}{\partial t}$$

  where $\mathbf{D}$ is the electric displacement field, $\mathbf{H}$ is the magnetic field intensity, $\mathbf{J}_f$ is the free electric current density, $\rho_f$ is the free electric charge density, $Q_f$ is the total free electric charge, $I_f