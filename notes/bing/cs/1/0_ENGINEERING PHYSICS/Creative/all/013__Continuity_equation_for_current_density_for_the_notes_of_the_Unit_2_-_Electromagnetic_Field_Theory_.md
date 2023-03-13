### Continuity equation for current density for the notes of the Unit 2 - Electromagnetic Field Theory in the subject of ENGINEERING PHYSICS

- Current density is a measure of the amount of electric current flowing through a unit area of a conductor. It is denoted by J and has the unit of A/m^2. The formula for current density is given as:

  J = I / A

  Where, I = current flowing through the conductor in Amperes
  A = cross-sectional area of the conductor in m^2

- The continuity equation for current density is a mathematical expression that relates the change in charge density (ρ) to the divergence of current density (J). It is derived from the conservation of electric charge principle, which states that the net charge in a closed volume cannot change unless there is a net current flowing through the surface of the volume. The continuity equation for current density is given as :

  ∂ρ/∂t + ∇⋅J = 0

  Where, t = time in seconds
  ρ = charge density in C/m^3
  J = current density in A/m^2
  ∇⋅ = divergence operator

- The continuity equation for current density can be interpreted as follows: The rate of change of charge density at any point in space is equal to the negative of the net current density flowing out of that point. This means that if the charge density increases at a point, there must be more current flowing into that point than out of it, and vice versa. The continuity equation for current density ensures that the electric charge is conserved in any situation.

- A mnemonic to remember the continuity equation for current density is:

  **C**harge **C**hange **C**auses **C**urrent **C**onvergence

  This means that a change in charge density causes a convergence or divergence of current density, depending on the sign of the change.

- An example of applying the continuity equation for current density is:

  Suppose a cylindrical wire of radius R carries a current I that varies with time as I = I_0 sin(ωt), where I_0 and ω are constants. Find the charge density and the current density in the wire.

  Solution:

  The current density in the wire is given by:

  J = I / A = I_0 sin(ωt) / (πR^2)

  The charge density in the wire is given by:

  ρ = ε_0 ∇⋅E

  Where, ε_0 = permittivity of free space
  E = electric field in the wire

  To find E, we use the Ampere's law, which states that:

  ∫ B⋅dl = μ_0 I_enc

  Where, B = magnetic field in the wire
  dl = differential length element along a closed loop
  μ_0 = permeability of free space
  I_enc = current enclosed by the loop

  Assuming that the magnetic field is uniform and parallel to the axis of the wire, we can choose a circular loop of radius r < R as the path of integration. Then, we have:

  B 2πr = μ_0 I_enc

  Solving for B, we get:

  B = μ_0 I_enc / (2πr)

  The current enclosed by the loop is given by:

  I_enc = J A = J πr^2

  Substituting J from above, we get:

  I_enc = I_0 sin(ωt) r^2 / R^2

  Therefore, the magnetic field is given by:

  B = μ_0 I_0 sin(ωt) r / (2 R^2)

  To find E, we use the Faraday's law, which states that:

  ∫ E⋅dl = - dΦ_B / dt

  Where, Φ_B = magnetic flux through the loop

  Assuming that the electric field is uniform and radial in the wire, we can choose the same circular loop as the path of integration. Then, we have:

  E 2πr = - dΦ_B / dt

  Solving for E, we get:

  E = - dΦ_B / (dt 2πr)

  The magnetic flux through the loop is given by:

  Φ_B = B A = B πr^2

  Substituting B from