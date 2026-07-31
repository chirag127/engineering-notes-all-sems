### Green’s theorem and Stoke’s theorem (without proof) and their applications

- Green's theorem and Stoke's theorem are generalizations of the Fundamental Theorem of Calculus to higher dimensions .
- Green's theorem relates a line integral around a simple closed curve in a plane to a double integral over the enclosed region . It can be written as:

$$\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_R \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right) dA$$

where $\mathbf{F} = P\mathbf{i} + Q\mathbf{j}$ is a vector field, $C$ is the boundary of the region $R$, and $d\mathbf{r}$ is the differential arc length along $C$.

- Stoke's theorem relates a surface integral of the curl of a vector field over a surface in space to a line integral around the boundary of the surface . It can be written as:

$$\iint_S \nabla \times \mathbf{F} \cdot d\mathbf{S} = \oint_C \mathbf{F} \cdot d\mathbf{r}$$

where $\mathbf{F}$ is a vector field, $S$ is a surface, $C$ is the boundary of $S$, and $d\mathbf{S}$ is the differential surface element.

- Some applications of Green's theorem and Stoke's theorem are:

  - Computing the area of a plane region using a line integral around its boundary.
  - Computing the work done by a force field along a closed curve using a double integral over the enclosed region.
  - Computing the circulation of a fluid around a curve using a surface integral over the region bounded by the curve.
  - Computing the flux of the curl of a vector field through a surface using a line integral around the boundary of the surface.
  - Verifying the conservation of mass, momentum, and energy in fluid dynamics using the divergence theorem and Stoke's theorem.