# Poynting vector and Poynting theorem

- The **Poynting vector** is a vector quantity that represents the directional energy flux (the energy transfer per unit area per unit time) of an electromagnetic field.
- The Poynting vector is defined as the cross product of the electric field vector **E** and the magnetic field vector **H**, that is, **S = E x H** .
- The Poynting vector is named after its discoverer, J.H. Poynting, who derived it in 1884.
- The Poynting vector has the units of power per unit area, or watts per square meter (W/m^2^).
- The Poynting vector is used throughout electromagnetics in conjunction with **Poynting's theorem**, the continuity equation expressing conservation of electromagnetic energy, to calculate the power flow in electromagnetic fields.

- **Poynting's theorem** states that the net electromagnetic power flowing into a region of space may be either dissipated, or used to change the energy stored in electric and magnetic fields within that region.
- Poynting's theorem can be derived from Maxwell's equations and the Lorentz force law, and can be written in integral or differential form.
- The integral form of Poynting's theorem is:

  \[ \oint_S \mathbf{S} \cdot d\mathbf{a} = -\frac{d}{dt} \int_V \left( \frac{1}{2} \epsilon_0 E^2 + \frac{1}{2} \mu_0 H^2 \right) dV - \int_V \mathbf{J} \cdot \mathbf{E} dV \]

  where **S** is the Poynting vector, **a** is the surface element vector, **V** is the volume enclosed by the surface **S**, **E** is the electric field, **H** is the magnetic field, **J** is the current density, and **ε0** and **μ0** are the permittivity and permeability of free space, respectively.

- The differential form of Poynting's theorem is:

  \[ \nabla \cdot \mathbf{S} = -\frac{\partial}{\partial t} \left( \frac{1}{2} \epsilon_0 E^2 + \frac{1}{2} \mu_0 H^2 \right) - \mathbf{J} \cdot \mathbf{E} \]

  where **S**, **E**, **H**, **J**, **ε0**, and **μ0** are the same as above, and **∇** is the divergence operator.

- Poynting's theorem can be interpreted as follows: the net power crossing any closed surface is equal to the negative of the rate of change of the electromagnetic energy inside the surface, minus the power dissipated as heat or other forms of energy inside the surface.
- Poynting's theorem can be used to calculate the power radiated by an antenna, the power absorbed by a circuit element, the power transmitted by a waveguide, and the power reflected by a boundary, among other applications.