### Gauss's Divergence Theorem

- Gauss's divergence theorem, also known as Gauss's theorem or Ostrogradsky's theorem, is a theorem in vector calculus that relates the flux of a vector field through a closed surface to the divergence of the field in the volume enclosed.
- The flux of a vector field is the amount of the field that passes through a given surface per unit time. The divergence of a vector field is a measure of how much the field diverges from a point, or how much it acts as a source or a sink of the field.
- The theorem can be stated as follows: Let **V** be a region in space with boundary **S**, and let **F** be a vector field that is continuously differentiable in **V**. Then:

$$\iint_S \mathbf{F} \cdot d\mathbf{S} = \iiint_V \nabla \cdot \mathbf{F} \, dV$$

- The left-hand side of the equation is the surface integral of **F** over **S**, which represents the net flux of **F** out of the region **V**. The right-hand side of the equation is the volume integral of the divergence of **F** over **V**, which represents the net amount of **F** that is generated or absorbed inside **V**.
- The theorem can be interpreted as a conservation law: the net flux of **F** out of a region is equal to the net source of **F** inside the region.
- The theorem can be proved using the divergence theorem in two dimensions, also known as Green's theorem, and applying it to each face of a small rectangular box that is contained in **V**. By taking the limit as the box shrinks to a point, the theorem follows.