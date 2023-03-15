# Green’s theorem and Stoke’s theorem (without proof) and their applications

## Green’s theorem

- Green’s theorem is a special case of the Kelvin–Stokes theorem, when applied to a region in the xy-plane.
- Green’s theorem exhibits the connection between line integrals and area integrals.
- Green’s theorem states that if L is a positively oriented, piecewise smooth, simple closed curve in a plane, and D is the region bounded by L, then

$$\oint_L (P dx + Q dy) = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dA$$

where P and Q have continuous partial derivatives on an open region that contains D.

- Green’s theorem is primarily utilised for the integration of lines and grounds.
- Green’s theorem can be used to calculate the area of a plane region, the circulation and curl of a vector field, and the work done by a force field along a closed curve.

## Stoke’s theorem

- Stoke’s theorem is a generalization of Green’s theorem to higher dimensions.
- Stoke’s theorem relates a vector surface integral over a surface S in space to a line integral around the boundary of S.
- Stoke’s theorem states that if S is an oriented piecewise smooth surface that is bounded by a simple, closed, piecewise smooth boundary curve C with positive orientation, and F is a vector field whose components have continuous partial derivatives on an open region in R^3^ that contains S, then

$$\iint_S \text{curl} \mathbf{F} \cdot d\mathbf{S} = \oint_C \mathbf{F} \cdot d\mathbf{r}$$

where curl F is the vector field defined by

$$\text{curl} \mathbf{F} = \left(\frac{\partial F_z}{\partial y} - \frac{\partial F_y}{\partial z}\right) \mathbf{i} + \left(\frac{\partial F_x}{\partial z} - \frac{\partial F_z}{\partial x}\right) \mathbf{j} + \left(\frac{\partial F_y}{\partial x} - \frac{\partial F_x}{\partial y}\right) \mathbf{k}$$

and dS is the surface element with outward orientation.

- Stoke’s theorem can be used to calculate the flux of the curl of a vector field, the circulation of a vector field along a curve, and the work done by a force field on a moving particle along a curve.

## Applications

- Green’s theorem and Stoke’s theorem are useful tools for evaluating integrals that arise in real life situations, such as physics, engineering, and geometry .
- Some examples of applications are:

  - Finding the area of a region bounded by a curve using Green’s theorem.
  - Finding the work done by a force field along a closed curve using Green’s theorem or Stoke’s theorem .
  - Finding the circulation of a fluid around a curve using Green’s theorem or Stoke’s theorem .
  - Finding the flux of a magnetic field through a surface using Stoke’s theorem.
  - Finding the curl of a vector field at a point using Stoke’s theorem.
  - Finding the divergence of a vector field at a point using the divergence theorem, which is another generalization of Green’s theorem.