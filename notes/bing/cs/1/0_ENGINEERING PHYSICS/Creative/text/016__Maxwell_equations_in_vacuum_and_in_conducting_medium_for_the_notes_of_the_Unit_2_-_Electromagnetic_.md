### Maxwell equations in vacuum and in conducting medium

- Maxwell equations are a set of four partial differential equations that describe the relationship between electric and magnetic fields in space and time.
- They are derived from the experimental laws of Gauss, Faraday, and Ampere, with a modification by Maxwell to account for the displacement current.
- Maxwell equations can be written in two forms: the differential form and the integral form. The differential form uses the operators of divergence and curl, while the integral form uses the concepts of flux and circulation.
- In a vacuum, the Maxwell equations are:

\begin{aligned}
\nabla \cdot \mathbf{E} &= \frac{\rho}{\epsilon_0} & \text{(Gauss's law for electricity)} \\
\nabla \cdot \mathbf{B} &= 0 & \text{(Gauss's law for magnetism)} \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} & \text{(Faraday's law of induction)} \\
\nabla \times \mathbf{B} &= \mu_0 \mathbf{J} + \mu_0 \epsilon_0 \frac{\partial \mathbf{E}}{\partial t} & \text{(Ampere-Maxwell law)}
\end{aligned}

- Here, $\mathbf{E}$ is the electric field, $\mathbf{B}$ is the magnetic field, $\rho$ is the charge density, $\mathbf{J}$ is the current density, $\epsilon_0$ is the permittivity of free space, and $\mu_0$ is the permeability of free space.
- In a conducting medium, the Maxwell equations are modified by the presence of charges and currents inside the material. The material properties are characterized by the electric permittivity $\epsilon$, the magnetic permeability $\mu$, and the electric conductivity $\sigma$.
- In a conducting medium, the Maxwell equations are:

\begin{aligned}
\nabla \cdot \mathbf{D} &= \rho_f & \text{(Gauss's law for electricity)} \\
\nabla \cdot \mathbf{B} &= 0 & \text{(Gauss's law for magnetism)} \\
\nabla \times \mathbf{E} &= -\frac{\partial \mathbf{B}}{\partial t} & \text{(Faraday's law of induction)} \\
\nabla \times \mathbf{H} &= \mathbf{J}_f + \frac{\partial \mathbf{D}}{\partial t} & \text{(Ampere-Maxwell law)}
\end{aligned}

- Here, $\mathbf{D}$ is the electric displacement field, $\mathbf{H}$ is the magnetic field intensity, $\rho_f$ is the free charge density, and $\mathbf{J}_f$ is the free current density.
- The relation between the fields and the material properties are:

\begin{aligned}
\mathbf{D} &= \epsilon \mathbf{E} \\
\mathbf{B} &= \mu \mathbf{H} \\
\mathbf{J} &= \mathbf{J}_f + \mathbf{J}_p \\
\mathbf{J}_p &= \sigma \mathbf{E}
\end{aligned}

- Here, $\mathbf{J}_p$ is the polarization current density, which is proportional to the electric field by the conductivity $\sigma$.
- Maxwell equations can be used to derive the electromagnetic wave equation, which shows how electromagnetic waves propagate in vacuum and in media with different speeds and wavelengths.