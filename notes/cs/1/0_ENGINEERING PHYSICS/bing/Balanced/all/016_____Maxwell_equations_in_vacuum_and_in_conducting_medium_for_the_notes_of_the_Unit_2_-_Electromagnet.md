# Maxwell equations in vacuum and in conducting medium

- Maxwell equations are a set of four partial differential equations that describe the behavior of electric and magnetic fields in vacuum and in matter.
- They are derived from the experimental laws of Gauss, Faraday, Ampere and Maxwell, and they are consistent with the principle of conservation of charge and energy.
- They can be written in two equivalent forms: the integral form and the differential form.
- The integral form relates the flux of electric and magnetic fields through a closed surface to the total charge and current enclosed by the surface.
- The differential form relates the divergence and curl of electric and magnetic fields at a point to the charge and current density at that point.
- In vacuum, the electric and magnetic fields are independent of the properties of the medium, and they satisfy the following equations:

  - Gauss's law for electricity: $$\oint_S \mathbf{E} \cdot d\mathbf{A} = \frac{Q}{\epsilon_0}$$
  - Gauss's law for magnetism: $$\oint_S \mathbf{B} \cdot d\mathbf{A} = 0$$
  - Faraday's law of induction: $$\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \int_S \mathbf{B} \cdot d\mathbf{A}$$
  - Ampere-Maxwell law: $$\oint_C \mathbf{B} \cdot d\mathbf{l} = \mu_0 \left( I + \epsilon_0 \frac{d}{dt} \int_S \mathbf{E} \cdot d\mathbf{A} \right)$$

  where $\mathbf{E}$ and $\mathbf{B}$ are the electric and magnetic fields, $Q$ and $I$ are the total charge and current, $\epsilon_0$ and $\mu_0$ are the permittivity and permeability of vacuum, $S$ is a closed surface, and $C$ is a closed loop.

- In a conducting medium, the electric and magnetic fields are affected by the presence of free charges and currents, and they satisfy the following equations:

  - Gauss's law for electricity: $$\oint_S \mathbf{D} \cdot d\mathbf{A} = Q_f$$
  - Gauss's law for magnetism: $$\oint_S \mathbf{B} \cdot d\mathbf{A} = 0$$
  - Faraday's law of induction: $$\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d}{dt} \int_S \mathbf{B} \cdot d\mathbf{A}$$
  - Ampere-Maxwell law: $$\oint_C \mathbf{H} \cdot d\mathbf{l} = I_f + \frac{d}{dt} \int_S \mathbf{D} \cdot d\mathbf{A}$$

  where $\mathbf{D}$ and $\mathbf{H}$ are the electric displacement and magnetic field intensity, $Q_f$ and $I_f$ are the free charge and current, and the other symbols are the same as before.

- The electric displacement and magnetic field intensity are related to the electric and magnetic fields by the constitutive relations:

  - $$\mathbf{D} = \epsilon \mathbf{E}$$
  - $$\mathbf{H} = \frac{1}{\mu} \mathbf{B}$$

  where $\epsilon$ and $\mu$ are the permittivity and permeability of the medium, which may depend on the frequency, direction and position of the fields.

- Maxwell equations can be used to derive the wave equation for electromagnetic waves, which shows that they propagate at a constant speed in vacuum and in non-conducting mediums, and that they can reflect, refract, interfere and diffract in different mediums.