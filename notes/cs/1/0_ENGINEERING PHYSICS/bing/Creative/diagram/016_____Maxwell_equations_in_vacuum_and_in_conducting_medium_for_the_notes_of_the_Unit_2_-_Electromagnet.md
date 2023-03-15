### Maxwell equations in vacuum and in conducting medium

- Maxwell equations are a set of four partial differential equations that describe the behavior of electric and magnetic fields in vacuum and in matter.
- They are derived from the conservation laws of electric charge and magnetic flux, as well as the experimental laws of Faraday, Ampere and Gauss.
- They can be written in two equivalent forms: the integral form and the differential form.
- The integral form relates the flux of electric and magnetic fields through a closed surface to the enclosed charge and current, and the circulation of electric and magnetic fields around a closed loop to the rate of change of magnetic and electric flux, respectively.
- The differential form relates the divergence and curl of electric and magnetic fields to the charge and current densities, and the rate of change of electric and magnetic fields, respectively.
- In vacuum, the charge and current densities are zero, and the electric and magnetic fields are related only by their rates of change. The Maxwell equations in vacuum are:

  - Gauss's law for electricity: $$\oint_S \mathbf{E} \cdot d\mathbf{A} = \frac{Q}{\epsilon_0}$$ or $$\nabla \cdot \mathbf{E} = 0$$
  - Gauss's law for magnetism: $$\oint_S \mathbf{B} \cdot d\mathbf{A} = 0$$ or $$\nabla \cdot \mathbf{B} = 0$$
  - Faraday's law of induction: $$\oint_C \mathbf{E} \cdot d\mathbf{l} = - \frac{d}{dt} \int_S \mathbf{B} \cdot d\mathbf{A}$$ or $$\nabla \times \mathbf{E} = - \frac{\partial \mathbf{B}}{\partial t}$$
  - Ampere-Maxwell law: $$\oint_C \mathbf{B} \cdot d\mathbf{l} = \mu_0 \epsilon_0 \frac{d}{dt} \int_S \mathbf{E} \cdot d\mathbf{A}$$ or $$\nabla \times \mathbf{B} = \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t}$$

  where $\mathbf{E}$ and $\mathbf{B}$ are the electric and magnetic fields, $Q$ is the total electric charge, $\epsilon_0$ and $\mu_0$ are the permittivity and permeability of vacuum, $S$ is a closed surface, $C$ is a closed loop, and $d\mathbf{A}$ and $d\mathbf{l}$ are the differential area and length elements.

- In a conducting medium, the charge and current densities are non-zero, and the electric and magnetic fields are affected by the properties of the medium, such as conductivity, permittivity and permeability. The Maxwell equations in a conducting medium are:

  - Gauss's law for electricity: $$\oint_S \mathbf{D} \cdot d\mathbf{A} = Q$$ or $$\nabla \cdot \mathbf{D} = \rho$$
  - Gauss's law for magnetism: $$\oint_S \mathbf{B} \cdot d\mathbf{A} = 0$$ or $$\nabla \cdot \mathbf{B} = 0$$
  - Faraday's law of induction: $$\oint_C \mathbf{E} \cdot d\mathbf{l} = - \frac{d}{dt} \int_S \mathbf{B} \cdot d\mathbf{A}$$ or $$\nabla \times \mathbf{E} = - \frac{\partial \mathbf{B}}{\partial t}$$
  - Ampere-Maxwell law: $$\oint_C \mathbf{H} \cdot d\mathbf{l} = I + \frac{d}{dt} \int_S \mathbf{D} \cdot d\mathbf{A}$$ or $$\nabla \times \mathbf{H} = \mathbf{J} + \frac{\partial \mathbf{D}}{\partial t}$$

  where $\mathbf{D}$ and $\mathbf{H}$ are the electric displacement and magnetic field intensity, $\