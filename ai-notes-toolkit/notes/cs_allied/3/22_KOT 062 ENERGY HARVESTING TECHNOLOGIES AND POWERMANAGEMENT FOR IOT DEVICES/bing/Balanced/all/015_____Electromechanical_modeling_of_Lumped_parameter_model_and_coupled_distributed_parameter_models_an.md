# Electromechanical modeling of Lumped parameter model and coupled distributed parameter models and closed-form solutions

- Electromechanical modeling is the process of describing the dynamic behavior of systems that involve both electrical and mechanical components, such as piezoelectric devices, motors, sensors, etc.
- Lumped parameter model is a simplified representation of a system that assumes that the physical properties of the system are constant or uniform throughout the system, and that the system can be divided into a finite number of discrete elements connected by nodes.
- Coupled distributed parameter model is a more realistic representation of a system that takes into account the spatial variation of the physical properties of the system, and that the system can be described by partial differential equations or integral equations.
- Closed-form solution is an analytical expression that can be obtained for the output or response of a system, without the need of numerical methods or approximations.

## Lumped parameter model of piezoelectric devices

- Piezoelectric devices are devices that can convert mechanical energy into electrical energy, or vice versa, by exploiting the piezoelectric effect, which is the property of certain materials to generate electric charges when subjected to mechanical stress, or to deform when subjected to electric fields.
- A lumped parameter model of a piezoelectric device can be derived by applying the Kirchhoff's laws of electric circuits and the Newton's laws of motion to the device, and by assuming that the device can be modeled as a mass-spring-damper system with a voltage source and a capacitor.
- The lumped parameter model can be represented by the following equations:

  - Mechanical equation: $$m\ddot{x} + c\dot{x} + kx = F + V_cC_p\dot{x}$$
  - Electrical equation: $$V_c = V - R_iI - \frac{1}{C_p}\int I dt$$
  - Constitutive equation: $$I = C_p\dot{V_c} + xC_p\dot{V}$$

  where:

  - $m$ is the mass of the device
  - $c$ is the damping coefficient of the device
  - $k$ is the stiffness of the device
  - $x$ is the displacement of the device
  - $F$ is the external force applied to the device
  - $V_c$ is the voltage across the capacitor
  - $V$ is the external voltage applied to the device
  - $R_i$ is the internal resistance of the device
  - $I$ is the current flowing through the device
  - $C_p$ is the piezoelectric capacitance of the device

- The lumped parameter model can be used to analyze the performance of the piezoelectric device in different modes of operation, such as sensing, actuation, or energy harvesting, and to design the optimal parameters of the device for a given application.

## Coupled distributed parameter model of piezoelectric devices

- A coupled distributed parameter model of a piezoelectric device can be derived by applying the Maxwell's equations of electromagnetism and the Navier's equations of elasticity to the device, and by taking into account the spatial variation of the electric potential, electric displacement, stress, strain, and displacement of the device.
- A coupled distributed parameter model of a piezoelectric device can be represented by the following equations:

  - Electromechanical coupling equation: $$\nabla \cdot \mathbf{D} = \rho_e$$
  - Constitutive equation: $$\mathbf{D} = \epsilon \mathbf{E} + e \mathbf{S}$$
  - Constitutive equation: $$\mathbf{S} = s \mathbf{E} + d \mathbf{E}$$
  - Equilibrium equation: $$\nabla \cdot \mathbf{T} + \mathbf{F} = \rho \ddot{\mathbf{u}}$$

  where:

  - $\mathbf{D}$ is the electric displacement vector
  - $\mathbf{E}$ is the electric field vector
  - $\mathbf{S}$ is the mechanical strain tensor
  - $\mathbf{T}$ is the mechanical stress tensor
  - $\mathbf{u}$ is the mechanical displacement vector
  - $\rho_e$ is the electric charge density
  - $\rho$ is the mass density
  - $\mathbf{F}$ is the external force vector
  - $\epsilon$