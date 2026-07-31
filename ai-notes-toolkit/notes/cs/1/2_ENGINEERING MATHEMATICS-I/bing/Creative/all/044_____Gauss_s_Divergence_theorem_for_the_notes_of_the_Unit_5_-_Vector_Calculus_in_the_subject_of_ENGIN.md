# Gauss's Divergence Theorem

- Gauss's divergence theorem, also known as Gauss's theorem or Ostrogradsky's theorem, is a theorem in vector calculus that relates the flux of a vector field through a closed surface to the divergence of the field in the volume enclosed.
- The flux of a vector field is the amount of the field that passes through a given surface per unit time. The divergence of a vector field is a measure of how much the field diverges or spreads out from a given point.
- The theorem can be stated as follows: Let **V** be a region in space with boundary **S**, and let **F** be a vector field that is continuously differentiable in **V**. Then

$$\iint_S \mathbf{F} \cdot d\mathbf{S} = \iiint_V \nabla \cdot \mathbf{F} \, dV$$

- The left-hand side of the equation is the surface integral of **F** over **S**, which represents the net flux of **F** out of the region **V**. The right-hand side of the equation is the volume integral of the divergence of **F** over **V**, which represents the net source or sink of **F** inside the region **V**.
- The theorem can be interpreted as a conservation law: the net flux of **F** out of a region is equal to the net source or sink of **F** inside the region.
- The theorem can be proved using the divergence theorem in two dimensions, also known as Green's theorem, and applying it to each face of a small rectangular box that is contained in **V**. By taking the limit as the box shrinks to a point, the theorem follows.
- The theorem can be generalized to higher dimensions and to more general surfaces and vector fields, as long as certain conditions are met. For example, the theorem holds for surfaces that are piecewise smooth and orientable, and for vector fields that are continuously differentiable and have compact support.
- The theorem has many applications in physics and engineering, such as calculating the electric flux through a closed surface using Gauss's law, or calculating the mass flow rate through a pipe using the continuity equation.