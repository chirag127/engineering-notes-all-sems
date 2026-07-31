### Maxwell equations in vacuum and in conducting medium

- Maxwell equations are a set of four partial differential equations that describe the behavior of electric and magnetic fields in vacuum and in matter.
- They are derived from the experimental laws of Gauss, Faraday, Ampere and Maxwell, and they are consistent with the principle of charge conservation and the special theory of relativity.
- They can be written in two equivalent forms: the integral form and the differential form. The integral form relates the flux or circulation of the fields through a closed surface or a closed loop to the enclosed charge or current. The differential form relates the divergence or curl of the fields at a point to the charge density or current density at that point.
- In vacuum, the Maxwell equations are:

  - Gauss's law for electricity: $$\oint_S \mathbf{E} \cdot d\mathbf{A} = \frac{Q}{\epsilon_0}$$ or $$\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}$$
  - Gauss's law for magnetism: $$\oint_S \mathbf{B} \cdot d\mathbf{A} = 0$$ or $$\nabla \cdot \mathbf{B} = 0$$
  - Faraday's law of induction: $$\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \int_S \mathbf{B} \cdot d\mathbf{A}$$ or $$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$
  - Ampere-Maxwell law: $$\oint_C \mathbf{B} \cdot d\mathbf{l} = \mu_0 I + \mu_0 \epsilon_0 \frac{d}{dt} \int_S \mathbf{E} \cdot d\mathbf{A}$$ or $$\nabla \times \mathbf{B} = \mu_0 \mathbf{J} + \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}$$

  where $\mathbf{E}$ is the electric field, $\mathbf{B}$ is the magnetic field, $\mathbf{J}$ is the current density, $\rho$ is the charge density, $\epsilon_0$ is the permittivity of vacuum, $\mu_0$ is the permeability of vacuum, $Q$ is the total charge enclosed by the surface $S$, and $I$ is the total current passing through the surface $S$.

- In a conducting medium, the Maxwell equations are modified by the presence of free charges and currents that can move under the influence of the fields. The free charge density and current density are denoted by $\rho_f$ and $\mathbf{J}_f$, respectively. The Maxwell equations in a conducting medium are:

  - Gauss's law for electricity: $$\oint_S \mathbf{E} \cdot d\mathbf{A} = \frac{Q_f}{\epsilon_0}$$ or $$\nabla \cdot \mathbf{E} = \frac{\rho_f}{\epsilon_0}$$
  - Gauss's law for magnetism: $$\oint_S \mathbf{B} \cdot d\mathbf{A} = 0$$ or $$\nabla \cdot \mathbf{B} = 0$$
  - Faraday's law of induction: $$\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \int_S \mathbf{B} \cdot d\mathbf{A}$$ or $$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$
  - Ampere-Maxwell law: $$\oint_C \mathbf{B} \cdot d\mathbf{l} = \mu_0 I_f + \mu_0 \epsilon_0 \frac{d}{dt} \int_S \mathbf{E} \cdot d\mathbf{A}$$ or $$\nabla \times \mathbf{B} = \mu_0 \mathbf{J}_f + \mu_0 \epsilon_0 \frac