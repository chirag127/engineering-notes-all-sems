### Maxwell equations in integral and differential form

- Maxwell equations are a set of four equations that describe the relationship between electric and magnetic fields, charges and currents.
- They are the foundation of electromagnetic theory and have many applications in physics and engineering.
- They can be written in two equivalent forms: integral and differential.
- The integral form relates the electric and magnetic fields to the charges and currents enclosed by a closed surface or a closed loop.
- The differential form relates the electric and magnetic fields to the charges and currents at a point in space using the differential operators divergence and curl.
- The integral and differential forms are connected by the mathematical theorems of Gauss and Stokes.
- The four equations are:

  - Gauss's law for electricity: The electric flux through any closed surface is equal to the net charge enclosed by the surface divided by the permittivity of free space.

    - Integral form: $$\oint_S \mathbf{E} \cdot d\mathbf{A} = \frac{Q}{\epsilon_0}$$
    - Differential form: $$\nabla \cdot \mathbf{E} = \frac{\rho}{\epsilon_0}$$
    - Where $\mathbf{E}$ is the electric field, $d\mathbf{A}$ is the differential area element, $Q$ is the net charge, $\epsilon_0$ is the permittivity of free space, $\nabla$ is the divergence operator, and $\rho$ is the charge density.

  - Gauss's law for magnetism: The magnetic flux through any closed surface is zero, which implies that there are no magnetic monopoles.

    - Integral form: $$\oint_S \mathbf{B} \cdot d\mathbf{A} = 0$$
    - Differential form: $$\nabla \cdot \mathbf{B} = 0$$
    - Where $\mathbf{B}$ is the magnetic field.

  - Faraday's law of induction: The electromotive force (EMF) around any closed loop is equal to the negative rate of change of the magnetic flux through the loop.

    - Integral form: $$\oint_C \mathbf{E} \cdot d\mathbf{l} = -\frac{d\Phi_B}{dt}$$
    - Differential form: $$\nabla \times \mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t}$$
    - Where $d\mathbf{l}$ is the differential line element, $\Phi_B$ is the magnetic flux, $\nabla \times$ is the curl operator, and $\frac{\partial}{\partial t}$ is the partial derivative with respect to time.

  - Ampere's circuital law: The magnetic field around any closed loop is equal to the sum of the current enclosed by the loop and the displacement current, which is proportional to the rate of change of the electric flux.

    - Integral form: $$\oint_C \mathbf{B} \cdot d\mathbf{l} = \mu_0 \left( I + \epsilon_0 \frac{d\Phi_E}{dt} \right)$$
    - Differential form: $$\nabla \times \mathbf{B} = \mu_0 \left( \mathbf{J} + \epsilon_0 \frac{\partial \mathbf{E}}{\partial t} \right)$$
    - Where $\mu_0$ is the permeability of free space, $I$ is the current, $\Phi_E$ is the electric flux, $\mathbf{J}$ is the current density, and $\frac{d}{dt}$ is the total derivative with respect to time.

- These equations can be written in a more compact form using the notation of tensors and differential forms, which generalizes them to higher dimensions and curved spacetimes.