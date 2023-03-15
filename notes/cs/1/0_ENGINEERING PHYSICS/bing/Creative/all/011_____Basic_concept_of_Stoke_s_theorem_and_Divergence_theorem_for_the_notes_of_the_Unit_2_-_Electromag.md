# Basic concept of Stoke’s theorem and Divergence theorem

- Stoke's theorem and Divergence theorem are two important theorems in vector calculus that relate different types of integrals over different types of regions.
- Stoke's theorem (also known as Kelvin-Stoke's theorem) relates a surface integral of the curl of a vector field to a line integral of the vector field along the boundary of the surface.
- Divergence theorem (also known as Gauss's theorem) relates a volume integral of the divergence of a vector field to a surface integral of the vector field over the boundary of the volume.
- Both theorems are generalizations of the fundamental theorem of calculus, which relates a definite integral of a function to the values of its antiderivative at the endpoints of the interval of integration.
- Both theorems can be used to simplify the calculation of integrals over complicated regions by transforming them into integrals over simpler regions.
- Both theorems have important applications in physics, such as electromagnetism, fluid dynamics, and heat transfer.

## Stoke's theorem

- The statement of Stoke's theorem is:

  $$\iint_S \nabla \times \mathbf{F} \cdot d\mathbf{S} = \oint_{\partial S} \mathbf{F} \cdot d\mathbf{r}$$

  where $\mathbf{F}$ is a vector field, $S$ is an oriented surface, $\partial S$ is the boundary curve of $S$, and $\nabla \times \mathbf{F}$ is the curl of $\mathbf{F}$.
- The surface $S$ must be smooth, closed (i.e., without holes), and orientable (i.e., having two distinct sides). The orientation of $S$ determines the orientation of $\partial S$ by the right-hand rule: if the fingers of the right hand point along the surface normal, then the thumb points along the positive direction of the boundary curve.
- The curl of a vector field $\mathbf{F} = (P, Q, R)$ is defined as:

  $$\nabla \times \mathbf{F} = \left( \frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z}, \frac{\partial P}{\partial z} - \frac{\partial R}{\partial x}, \frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y} \right)$$

  where $\nabla = (\frac{\partial}{\partial x}, \frac{\partial}{\partial y}, \frac{\partial}{\partial z})$ is the del operator.
- The curl of a vector field measures the tendency of the field to rotate around a point. It is a vector that is perpendicular to the plane of rotation and has a magnitude equal to the angular velocity of the rotation.
- The surface integral of the curl of a vector field over a surface $S$ measures the net circulation of the field around the boundary of $S$. It is a scalar that is positive if the circulation is in the same direction as the orientation of $\partial S$, and negative otherwise.
- The line integral of a vector field along a curve $C$ measures the work done by the field along the curve. It is a scalar that is positive if the field is in the same direction as the orientation of $C$, and negative otherwise.
- The physical interpretation of Stoke's theorem is that the work done by a vector field along a closed curve is equal to the net circulation of the field over any surface that has the curve as its boundary.

## Divergence theorem

- The statement of Divergence theorem is:

  $$\iiint_V \nabla \cdot \mathbf{F} dV = \iint_{\partial V} \mathbf{F} \cdot d\mathbf{S}$$

  where $\mathbf{F}$ is a vector field, $V$ is a solid region, $\partial V$ is the boundary surface of $V$, and $\nabla \cdot \mathbf{F}$ is the divergence of $\mathbf{F}$.
- The solid region $V$ must be closed (i.e., bounded) and have a smooth surface. The orientation of $\partial V$ is outward, meaning that the surface normal points away from the interior of $V$.
- The divergence of a vector field $\mathbf{F} = (P, Q, R)$ is